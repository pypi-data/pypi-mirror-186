import asyncio
import sys
import json
import logging
import pathlib
import re
import time
import typing
from dataclasses import dataclass
from decimal import Decimal
from typing import Literal

import base58
from anchorpy import Provider, Wallet
from pyserum.market import AsyncMarket, OrderBook
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Processed
from solana.rpc.websocket_api import connect
from solana.transaction import AccountMeta, Transaction
from solders.rpc.responses import AccountNotification

from mango_explorer_v4.types.side import Bid, Ask
from mango_explorer_v4.accounts.bank import Bank
from mango_explorer_v4.accounts.book_side import BookSide
from mango_explorer_v4.accounts.mango_account import MangoAccount
from mango_explorer_v4.accounts.mint_info import MintInfo
from mango_explorer_v4.accounts.serum3_market import Serum3Market
from mango_explorer_v4.accounts.perp_market import PerpMarket
from mango_explorer_v4.types.inner_node import InnerNode
from mango_explorer_v4.types.leaf_node import LeafNode
from mango_explorer_v4.types.perp_open_order import PerpOpenOrder
from mango_explorer_v4.instructions.serum3_cancel_all_orders import Serum3CancelAllOrdersAccounts, Serum3CancelAllOrdersArgs, serum3_cancel_all_orders
from mango_explorer_v4.instructions.serum3_create_open_orders import Serum3CreateOpenOrdersAccounts, serum3_create_open_orders
from mango_explorer_v4.instructions.serum3_place_order import Serum3PlaceOrderArgs, Serum3PlaceOrderAccounts, serum3_place_order
from mango_explorer_v4.instructions.perp_place_order import PerpPlaceOrderArgs, PerpPlaceOrderAccounts, perp_place_order
from mango_explorer_v4.instructions.perp_cancel_all_orders import PerpCancelAllOrdersArgs, PerpCancelAllOrdersAccounts, perp_cancel_all_orders
from mango_explorer_v4.program_id import SERUM_PROGRAM_ID, MANGO_PROGRAM_ID
from mango_explorer_v4.types import serum3_side, serum3_self_trade_behavior, serum3_order_type
from mango_explorer_v4.types import place_order_type


# logging.basicConfig(
#     level=logging.DEBUG
# )


@dataclass
class MangoClient():
    provider: Provider
    mango_account_pk: str
    group_config: dict
    mango_account: MangoAccount
    serum_markets: [Serum3Market]
    serum_markets_external: [AsyncMarket]
    banks: [Bank]
    mint_infos: [MintInfo]
    perp_markets: [PerpMarket]
    rpc_url: str
    symbols: [str]

    @staticmethod
    async def connect(
        secret_key: str | bytes,
        # ^ Can be the output from Phantom's "Export Private Key" - this for easy onboarding
        # as with the V3 lib folks used to get confused about how to turn it into something
        # like the output from `solana-keygen new -o scratch.json`, which is also supported
        mango_account_pk: str,
        # ^ A SOL wallet can have multiple Mango accounts - let the user pick the one he's
        # looking to use. Specifying it beforehand spares a lot of redundancy
        rpc_url: str = 'https://mango.rpcpool.com/0f9acc0d45173b51bf7d7e09c1e5'
        # ^ Can use the default RPC endpoint or whichever so desired
    ):
        provider = Provider(
            AsyncClient(rpc_url, Processed),
            Wallet(
                Keypair.from_secret_key(
                    base58.b58decode(secret_key)
                    if type(secret_key == str) else
                    Wallet(Keypair.from_secret_key(secret_key))
                )
            )
            if secret_key is not None else Wallet.dummy()
        )

        mango_account = await MangoAccount.fetch(
            provider.connection,
            PublicKey(mango_account_pk)
        )

        if mango_account.owner != provider.wallet.public_key:
            raise ValueError('Mango account is not owned by the secret key entered')

        ids = json.loads(open(pathlib.Path(__file__).parent / 'ids.json').read())

        group_config = [group_config for group_config in ids['groups'] if PublicKey(group_config['publicKey']) == mango_account.group][0]

        serum_markets = await Serum3Market.fetch_multiple(
            provider.connection,
            [
                PublicKey(serum3_market_config['publicKey'])
                for serum3_market_config in group_config['serum3Markets']
                if serum3_market_config['active']
            ]
        )

        serum_markets_external = await asyncio.gather(*[
            AsyncMarket.load(provider.connection, serum_market.serum_market_external, SERUM_PROGRAM_ID)
            for serum_market in serum_markets
        ])

        banks_config = [
            {
                'tokenIndex': token_config['tokenIndex'],
                'publicKey': PublicKey(token_config['banks'][0]['publicKey'])
            }
            for token_config in group_config['tokens']
            if token_config['active']
        ]

        banks = await Bank.fetch_multiple(
            provider.connection,
            [bank_config['publicKey'] for bank_config in banks_config]
        )

        mint_infos_configs = [
            {
                'tokenIndex': token_config['tokenIndex'],
                'publicKey': PublicKey(token_config['mintInfo'])
            }
            for token_config in group_config['tokens']
            if token_config['active']
            if token_config['tokenIndex'] in [token.token_index for token in mango_account.tokens if token.token_index != 65535]
        ]

        mint_infos_configs = list(sorted(mint_infos_configs, key=lambda mint_info_config: mint_info_config['tokenIndex']))

        mint_infos = await MintInfo.fetch_multiple(
            provider.connection,
            [mint_info_config['publicKey'] for mint_info_config in mint_infos_configs]
        )

        perp_markets = await PerpMarket.fetch_multiple(
            provider.connection,
            [perp_market['publicKey'] for perp_market in group_config['perpMarkets']]
        )

        symbols = [
            *[perp_market_config['name'] for perp_market_config in group_config['perpMarkets']],
            *[serum3_market_config['name'] for serum3_market_config in group_config['serum3Markets']]
        ]

        return MangoClient(
            provider,
            mango_account_pk,
            mango_account=mango_account,
            group_config=group_config,
            serum_markets=serum_markets,
            serum_markets_external=serum_markets_external,
            banks=banks,
            mint_infos=mint_infos,
            perp_markets=perp_markets,
            rpc_url=rpc_url,
            symbols=symbols
        )

    async def symbols(self):
        # Can't make it static yet because need to know which group
        # to use, and group is inferred from the Mango account
        return [
            {
                'name': market_config['name'],
                'baseCurrency': market_config['name'].split('/')[0],
                'quoteCurrency': market_config['name'].split('/')[1],
                'makerFees': - (0.5 / 1e4),
                'takerFees': (1 / 1e4)
            }
            for market_config in self.group_config['serum3Markets']
        ]

    async def orderbook_l2(self, symbol: str, depth: int = 100):
        market_type = {'PERP': 'perpetual', 'USDC': 'spot'}[re.split(r"[-|/]", symbol)[1]]

        match market_type:
            case 'spot':
                serum_market_config = [serum3_market_config for serum3_market_config in self.group_config['serum3Markets'] if serum3_market_config['name'] == symbol][0]

                serum_market_index = serum_market_config['marketIndex']

                serum_market = [
                    serum_market
                    for serum_market in self.serum_markets
                    if serum_market.market_index == serum_market_index
                ][0]

                serum_market_external = [
                    serum_market_external
                    for serum_market_external in self.serum_markets_external
                    if serum_market_external.state.public_key() == serum_market.serum_market_external
                ][0]

                response = await self.provider.connection.get_multiple_accounts([
                    serum_market_external.state.bids(),
                    serum_market_external.state.asks()
                ])

                [raw_bids, raw_asks] = response.value

                [bids, asks] = [
                    OrderBook.from_bytes(serum_market_external.state, raw_bids.data),
                    OrderBook.from_bytes(serum_market_external.state, raw_asks.data)
                ]

                orderbook = {
                    'symbol': symbol,
                    'bids': [[bid.price, bid.size] for bid in bids.get_l2(depth)],
                    'asks': [[ask.price, ask.size] for ask in asks.get_l2(depth)]
                }

                return orderbook
            case 'perpetual':
                perp_market_config = [perp_market_config for perp_market_config in self.group_config['perpMarkets'] if perp_market_config['name'] == symbol][0]

                perp_market = [perp_market for perp_market in self.perp_markets if perp_market.perp_market_index == perp_market_config['marketIndex']][0]

                [bids, asks] = await BookSide.fetch_multiple(self.provider.connection, [perp_market.bids, perp_market.asks])

                def to_inner_node(data):
                    pass

                def items(book_side: BookSide, side: Literal['bids', 'asks']):
                    def fixed_items():
                        if book_side.roots[0].leaf_count == 0:
                            return

                        stack = [book_side.roots[0].maybe_node]

                        while len(stack) > 0:
                            index = stack.pop()

                            node = book_side.nodes.nodes[index]

                            [left, right] = [1, 0] if side == 'bids' else [0, 1]

                            match node.tag:
                                case 1:
                                    inner_node = InnerNode.from_decoded([1] + node.data)

                                    stack.extend([inner_node.children[right], inner_node.children[left]])
                                case 2:
                                    leaf_node = LeafNode.from_decoded([2] + node.data)

                                    yield

                            yield node.tag

                    return fixed_items()


                return list(items(asks, 'asks'))



    async def snapshots_l2(self, symbol: str, depth: int = 50):
        serum_market_config = [serum3_market_config for serum3_market_config in self.group_config['serum3Markets'] if serum3_market_config['name'] == symbol][0]

        serum_market_index = serum_market_config['marketIndex']

        serum_market = [
            serum_market
            for serum_market in self.serum_markets
            if serum_market.market_index == serum_market_index
        ][0]

        serum_market_external = [
            serum_market_external
            for serum_market_external in self.serum_markets_external
            if serum_market_external.state.public_key() == serum_market.serum_market_external
        ][0]

        orderbook = {
            'symbol': symbol,
            'bids': None,
            'asks': None
        }

        yield await self.orderbook_l2(symbol, depth)

        # async with connect(self.rpc_url.replace('https://', 'wss://')) as websocket:
        async with connect('wss://mango.rpcpool.com/0f9acc0d45173b51bf7d7e09c1e5') as websocket:
            remap = {}

            await websocket.account_subscribe(serum_market_external.state.bids(), Processed, 'jsonParsed')

            remap[(await websocket.recv())[0].result] = 'bids'

            await websocket.account_subscribe(serum_market_external.state.asks(), Processed, 'jsonParsed')

            remap[(await websocket.recv())[0].result] = 'asks'

            async for message in websocket:
                for submessage in message:
                    if not isinstance(submessage, AccountNotification):
                        continue

                    side = OrderBook.from_bytes(serum_market_external.state, submessage.result.value.data)

                    orderbook[remap[submessage.subscription]] = [[order.price, order.size] for order in side.get_l2(depth)]

                    if not all([orderbook['bids'], orderbook['asks']]):
                        continue

                    yield orderbook

    def _health_remaining_accounts(
        self,
        retriever: Literal['fixed', 'scanning'],
        banks: [Bank],
        perp_markets: [PerpMarket]
    ) -> [AccountMeta]:
        health_remaining_account_pks = []

        match retriever:
            case 'fixed':
                token_indices = [token.token_index for token in self.mango_account.tokens]

                if len(banks) > 0:
                    for bank in banks:
                        if bank.token_index not in token_indices:
                            index = [
                                idx for idx, token in enumerate(self.mango_account.tokens)
                                if token.token_index == 65535
                                if token_indices[idx] == 65535
                            ][0]

                            token_indices[index] = bank.token_index

                mint_infos = [
                    mint_info for mint_info in self.mint_infos
                    if mint_info.token_index in [token_index for token_index in token_indices if token_index != 65535]
                ]

                health_remaining_account_pks.extend([mint_info.banks[0] for mint_info in mint_infos])

                health_remaining_account_pks.extend([mint_info.oracle for mint_info in mint_infos])

                perp_market_indices = [perp.market_index for perp in self.mango_account.perps]

                if len(perp_markets) > 0:
                    for perp_market in perp_markets:
                        if perp_market.perp_market_index not in perp_market_indices:
                            index = [
                                idx for idx, perp in enumerate(self.mango_account.perps)
                                if perp.market_index == 65535
                                if perp_market_indices[idx] == 65535
                            ][0] = perp_market.perp_market_index

                            perp_market_indices[index] = perp_market.perp_market_index

                perp_markets = [
                    perp_market for perp_market in self.perp_markets
                    if perp_market.perp_market_index in [perp_index for perp_index in perp_market_indices if perp_index != 65535]
                ]

                perp_market_pks = [
                    PublicKey(perp_market_config['publicKey']) for perp_market_config in self.group_config['perpMarkets']
                    if perp_market_config['marketIndex'] in [perp_market.perp_market_index for perp_market in perp_markets]
                ]

                health_remaining_account_pks.extend(perp_market_pks)

                health_remaining_account_pks.extend([perp_market.oracle for perp_market in perp_markets])

                health_remaining_account_pks.extend([serum3.open_orders for serum3 in self.mango_account.serum3 if serum3.market_index != 65535])
            case 'scanning':
                raise NotImplementedError()

        remaining_accounts: [AccountMeta] = [
            AccountMeta(pubkey=remaining_account_pk, is_writable=False, is_signer=False)
            for remaining_account_pk in health_remaining_account_pks
        ]

        return remaining_accounts


    def make_serum3_place_order_ix(self, symbol: str, side: Literal['bids', 'asks'], price: float, size: float):
        serum_market_config = [serum3_market_config for serum3_market_config in self.group_config['serum3Markets'] if serum3_market_config['name'] == symbol][0]

        serum_market_index = serum_market_config['marketIndex']

        serum_market = [
            serum_market
            for serum_market in self.serum_markets
            if serum_market.market_index == serum_market_index
        ][0]

        serum_market_external = [
            serum_market_external
            for serum_market_external in self.serum_markets_external
            if serum_market_external.state.public_key() == serum_market.serum_market_external
        ][0]

        limit_price = serum_market_external.state.price_number_to_lots(price)

        max_base_qty = serum_market_external.state.base_size_number_to_lots(size)

        order_type = {'limit': serum3_order_type.Limit(), 'immediate_or_cancel': serum3_order_type.ImmediateOrCancel()}['limit']

        max_native_quote_qty_without_fees = limit_price * max_base_qty

        is_maker = order_type == serum3_order_type.PostOnly()

        fees = {True: - (0.5 / 1e4), False: (1 / 1e4)}[is_maker]

        max_native_quote_qty_including_fees = max_native_quote_qty_without_fees + round(max_native_quote_qty_without_fees * fees)

        client_order_id = round(time.time_ns() / 1e6)

        serum3_place_order_args: Serum3PlaceOrderArgs = {
            'side': {'bids': serum3_side.Bid(), 'asks': serum3_side.Ask()}[side],
            'limit_price': limit_price,
            'max_base_qty': max_base_qty,
            'max_native_quote_qty_including_fees': max_native_quote_qty_including_fees,
            'self_trade_behavior': serum3_self_trade_behavior.DecrementTake(),
            'order_type': order_type,
            'client_order_id': client_order_id,
            'limit': 10
        }

        serum3 = [serum3 for serum3 in self.mango_account.serum3 if serum3.market_index == serum_market_index][0]

        if serum3 is None:
            raise Exception('serum3 account not found')

        payer_token_index = {
            'bids': serum_market.quote_token_index,
            'asks': serum_market.base_token_index
        }[side]

        bank = [bank for bank in self.banks if bank.token_index == payer_token_index][0]

        banks_config = [
            {
                'tokenIndex': token_config['tokenIndex'],
                'publicKey': PublicKey(token_config['banks'][0]['publicKey'])
            }
            for token_config in self.group_config['tokens']
            if token_config['active']
        ]

        bank_config = [bank_config for bank_config in banks_config if bank_config['tokenIndex'] == bank.token_index][0]

        serum_market_external_vault_signer_address = PublicKey.create_program_address([
            bytes(serum_market.serum_market_external),
            serum_market_external.state.vault_signer_nonce().to_bytes(8, 'little')
        ], SERUM_PROGRAM_ID)

        serum3_place_order_accounts: Serum3PlaceOrderAccounts = {
            'group': self.mango_account.group,
            'account': PublicKey(self.mango_account_pk),
            'owner': self.mango_account.owner,
            'open_orders': serum3.open_orders,
            'serum_market': PublicKey(serum_market_config['publicKey']),
            'serum_program': SERUM_PROGRAM_ID,
            'serum_market_external': serum_market.serum_market_external,
            'market_bids': serum_market_external.state.bids(),
            'market_asks': serum_market_external.state.asks(),
            'market_event_queue': serum_market_external.state.event_queue(),
            'market_request_queue': serum_market_external.state.request_queue(),
            'market_base_vault': serum_market_external.state.base_vault(),
            'market_quote_vault': serum_market_external.state.quote_vault(),
            'market_vault_signer': serum_market_external_vault_signer_address,
            'payer_bank': bank_config['publicKey'],
            'payer_vault': bank.vault,
            'payer_oracle': bank.oracle
        }

        remaining_accounts = self._health_remaining_accounts('fixed', [], [])

        serum3_place_order_ix = serum3_place_order(
            serum3_place_order_args,
            serum3_place_order_accounts,
            remaining_accounts=remaining_accounts
        )

        return serum3_place_order_ix

    def make_serum3_create_open_orders_ix(self, symbol):
        serum_market_config = [serum3_market_config for serum3_market_config in self.group_config['serum3Markets'] if serum3_market_config['name'] == symbol][0]

        serum_market_index = serum_market_config['marketIndex']

        serum_market = [
            serum_market
            for serum_market in self.serum_markets
            if serum_market.market_index == serum_market_index
        ][0]

        [open_orders_pk, nonce] = PublicKey.find_program_address(
            [
                bytes('Serum3OO', 'utf-8'),
                bytes(PublicKey(self.mango_account_pk)),
                bytes(PublicKey(serum_market_config['publicKey']))
            ],
            MANGO_PROGRAM_ID
        )

        serum3_create_open_orders_accounts: Serum3CreateOpenOrdersAccounts = {
            'group': self.mango_account.group,
            'account': PublicKey(self.mango_account_pk),
            'owner': self.provider.wallet.public_key,
            'serum_market': PublicKey(serum_market_config['publicKey']),
            'serum_program': serum_market.serum_program,
            'serum_market_external': serum_market.serum_market_external,
            'open_orders': open_orders_pk,
            'payer': self.provider.wallet.public_key,
        }

        serum3_create_open_orders_ix = serum3_create_open_orders(serum3_create_open_orders_accounts)

        return serum3_create_open_orders_ix

    def make_perp_place_order_ix(self, symbol, side, price, size):
        perp_market_config = [perp_market_config for perp_market_config in self.group_config['perpMarkets'] if perp_market_config['name'] == symbol][0]

        perp_market = [perp_market for perp_market in self.perp_markets if perp_market.perp_market_index == perp_market_config['marketIndex']][0]

        quote_decimals = 6

        def to_native(ui_amount: float, decimals: float) -> int:
            return int(ui_amount * 10 ** decimals)

        def ui_price_to_lots(perp_market: PerpMarket, price: float) -> int:
            return int(to_native(price, quote_decimals) * perp_market.base_lot_size / (perp_market.quote_lot_size * 10 ** perp_market.base_decimals))

        def ui_base_to_lots(perp_market: PerpMarket, size: float) -> int:
            return int(to_native(size, perp_market.base_decimals) // perp_market.base_lot_size)

        perp_place_order_args: PerpPlaceOrderArgs = {
            'side': {'bids': Bid, 'asks': Ask}[side],
            'price_lots': ui_price_to_lots(perp_market, price),
            'max_base_lots': ui_base_to_lots(perp_market, size),
            'max_quote_lots': sys.maxsize,
            'client_order_id': int(time.time() * 1e3),
            'order_type': place_order_type.Limit(),
            'reduce_only': False,
            'expiry_timestamp': 0,
            'limit': 10
        }

        perp_place_order_accounts: PerpPlaceOrderAccounts = {
            'group': perp_market.group,
            'account': PublicKey(self.mango_account_pk),
            'owner': self.provider.wallet.public_key,
            'perp_market': PublicKey(perp_market_config['publicKey']),
            'bids': perp_market.bids,
            'asks': perp_market.asks,
            'event_queue': perp_market.event_queue,
            'oracle': perp_market.oracle
        }

        remaining_accounts = self._health_remaining_accounts('fixed', [[bank for bank in self.banks if bank.token_index == 0][0]], [perp_market])

        perp_place_order_ix = perp_place_order(
            perp_place_order_args,
            perp_place_order_accounts,
            remaining_accounts=remaining_accounts
        )

        return perp_place_order_ix

    async def place_order(
        self,
        symbol: str,
        side: Literal['bids', 'asks'],
        price: float,
        size: float
    ):
        market_type = {'PERP': 'perpetual', 'USDC': 'spot'}[re.split(r"[-|/]", symbol)[1]]

        match market_type:
            case 'spot':
                serum_market_config = [serum3_market_config for serum3_market_config in self.group_config['serum3Markets'] if serum3_market_config['name'] == symbol][0]

                serum_market_index = serum_market_config['marketIndex']

                try:
                    serum3 = [serum3 for serum3 in self.mango_account.serum3 if serum3.market_index == serum_market_index][0]
                except IndexError:
                    logging.error(f"Open orders account for {symbol} not found, creating one...")

                    serum3_create_open_orders_ix = self.make_serum3_create_open_orders_ix('SOL/USDC')

                    recent_blockhash = (await self.provider.connection.get_latest_blockhash()).value.blockhash

                    tx = Transaction()

                    tx.recent_blockhash = str(recent_blockhash)

                    tx.add(serum3_create_open_orders_ix)

                    tx.sign(self.provider.wallet.payer)

                    response = await self.provider.send(tx)

                    logging.error(f"Waiting for Open Orders account creation confirmation...")

                    await self.provider.connection.confirm_transaction(response)

                    logging.error(f"Open orders account created for {symbol}.")

                    self.mango_account = await MangoAccount.fetch(
                        self.provider.connection,
                        PublicKey(self.mango_account_pk)
                    )

                serum3_place_order_ix = self.make_serum3_place_order_ix(
                    symbol,
                    side,
                    price,
                    size
                )

                tx = Transaction()

                recent_blockhash = (await self.provider.connection.get_latest_blockhash()).value.blockhash

                tx.recent_blockhash = str(recent_blockhash)

                tx.add(serum3_place_order_ix)

                tx.sign(self.provider.wallet.payer)

                response = await self.provider.send(tx)

                return response
            case 'perpetual':
                tx = Transaction()

                recent_blockhash = (await self.provider.connection.get_latest_blockhash()).value.blockhash

                tx.recent_blockhash = str(recent_blockhash)

                perp_place_order_ix = self.make_perp_place_order_ix(symbol, side, price, size)

                tx.add(perp_place_order_ix)

                tx.sign(self.provider.wallet.payer)

                response = await self.provider.send(tx)

                return response

    def make_serum3_cancel_all_orders_ix(self, symbol: str):
        serum_market_config = [serum3_market_config for serum3_market_config in self.group_config['serum3Markets'] if serum3_market_config['name'] == symbol][0]

        serum_market_index = serum_market_config['marketIndex']

        serum_market = [
            serum_market
            for serum_market in self.serum_markets
            if serum_market.market_index == serum_market_index
        ][0]

        try:
            serum3 = [serum3 for serum3 in self.mango_account.serum3 if serum3.market_index == serum_market_index][0]
        except IndexError as error:
            print(error)

        serum_market_external = [
            serum_market_external
            for serum_market_external in self.serum_markets_external
            if serum_market_external.state.public_key() == serum_market.serum_market_external
        ][0]

        serum3_cancel_all_orders_args: Serum3CancelAllOrdersArgs = {
            'limit': 10
        }

        serum3_cancel_all_orders_accounts: Serum3CancelAllOrdersAccounts = {
            'group': self.mango_account.group,
            'account': PublicKey(self.mango_account_pk),
            'owner': self.provider.wallet.public_key,
            'open_orders': serum3.open_orders,
            'serum_market': PublicKey(serum_market_config['publicKey']),
            'serum_program': serum_market.serum_program,
            'serum_market_external': serum_market.serum_market_external,
            'market_bids': serum_market_external.state.bids(),
            'market_asks': serum_market_external.state.asks(),
            'market_event_queue': serum_market_external.state.event_queue()
        }

        serum3_cancel_all_orders_ix = serum3_cancel_all_orders(
            serum3_cancel_all_orders_args,
            serum3_cancel_all_orders_accounts
        )

        return serum3_cancel_all_orders_ix

    def make_perp_cancel_all_orders_ix(self, symbol: str):
        perp_market_config = [perp_market_config for perp_market_config in self.group_config['perpMarkets'] if perp_market_config['name'] == symbol][0]

        perp_market = [perp_market for perp_market in self.perp_markets if perp_market.perp_market_index == perp_market_config['marketIndex']][0]

        perp_cancel_all_orders_args: PerpCancelAllOrdersArgs = {
            'limit': 10
        }

        perp_cancel_all_orders_accounts: PerpCancelAllOrdersAccounts = {
            'group': perp_market.group,
            'account': PublicKey(self.mango_account_pk),
            'owner': self.provider.wallet.public_key,
            'perp_market': PublicKey(perp_market_config['publicKey']),
            'bids': perp_market.bids,
            'asks': perp_market.asks
        }

        perp_cancel_all_orders_ix = perp_cancel_all_orders(perp_cancel_all_orders_args, perp_cancel_all_orders_accounts)

        return perp_cancel_all_orders_ix

    async def cancel_all_orders(self, symbol: str):
        market_type = {'PERP': 'perpetual', 'USDC': 'spot'}[re.split(r"[-|/]", symbol)[1]]

        match market_type:
            case 'spot':
                tx = Transaction()

                recent_blockhash = (await self.provider.connection.get_latest_blockhash()).value.blockhash

                tx.recent_blockhash = str(recent_blockhash)

                serum3_cancel_all_orders_ix = self.make_serum3_cancel_all_orders_ix(symbol)

                tx.add(serum3_cancel_all_orders_ix)

                tx.sign(self.provider.wallet.payer)

                response = await self.provider.send(tx)

                return response
            case 'perpetual':
                tx = Transaction()

                recent_blockhash = (await self.provider.connection.get_latest_blockhash()).value.blockhash

                tx.recent_blockhash = str(recent_blockhash)

                perp_cancel_all_orders_ix = self.make_perp_cancel_all_orders_ix(symbol)

                tx.add(perp_cancel_all_orders_ix)

                tx.sign(self.provider.wallet.payer)

                response = await self.provider.send(tx)

                return response

    async def balances(self):
        return [
            {
                'symbol': meta['symbol'],
                'balance': float(
                    meta['token_indexed_position'] * (
                        meta['bank_deposit_index'] if meta['token_indexed_position'] > 0
                        else meta['bank_borrow_index']
                    )
                    /
                    meta['bank_mint_decimals']
                )
            }
            for meta in
            [
                {
                    'symbol': token_config['symbol'],
                    'token_indexed_position': Decimal(token.indexed_position.val) / divider,
                    'bank_mint_decimals': 10 ** bank.mint_decimals,
                    'bank_deposit_index': Decimal(bank.deposit_index.val) / divider,
                    'bank_borrow_index': Decimal(bank.borrow_index.val) / divider,
                }
                for token, bank, token_config, divider in
                [
                    [
                        token,
                        [bank for bank in self.banks if bank.token_index == token.token_index][0],
                        [token_config for token_config in self.group_config['tokens'] if token_config['tokenIndex'] == token.token_index][0],
                        Decimal(2 ** (8 * 6))
                    ]
                    for token in self.mango_account.tokens
                    if token.token_index != 65535
                ]
            ]
        ]
