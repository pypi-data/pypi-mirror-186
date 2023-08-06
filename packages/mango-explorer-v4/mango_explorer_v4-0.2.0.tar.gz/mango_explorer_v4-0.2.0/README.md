# mango-explorer-v4

Python client library for interacting with Mango Markets v4.

## 📦 Installation

![PyPI](https://img.shields.io/pypi/v/mango-explorer-v4)

`mango-explorer-v4` is available as a [Python package on PyPI](https://pypi.org/project/mango-explorer-v4) and can be installed as:

```
pip install mango-explorer-v4
```

## Example usage

This example assumes that you have a wallet already set up: visit https://v4alpha.mango.markets to create a Mango account and fund it so that you can place orders. You can find the full sources [here](./examples).

```python
import asyncio
from mango_explorer_v4 import MangoClient

async def main():
    mango_client = await MangoClient.connect(
        secret_key='YOUR_SECRET_KEY', # Output from Phantom's "Export Private Key"
        mango_account_pk='YOUR_MANGO_ACCOUNT_PK'
    )

    print(await mango_client.symbols())
    # [
    #   {
    #       'name': 'SOL/USDC',
    #       'baseCurrency': 'SOL',
    #       'quoteCurrency': 'USDC',
    #       'makerFees': -5e-05,
    #       'takerFees': 0.0001
    #   }
    #   ...
    # ]

    print(await mango_client.place_order('SOL/USDC', 'bid', 10, 0.1, 'limit'))
    # (Refresh the UI to see the newly opened order)

    print(await mango_client.orderbook_l2('SOL/USDC', 3))
    # {
    #   'symbol': 'SOL/USDC',
    #   'bids': [
    #       [11.826, 0.899],
    #       [11.824, 39.436],
    #       [11.82, 316.421],
    #    ],
    #  'asks': [
    #       [11.839, 0.78],
    #       [11.84, 44.392],
    #       [11.841, 1.1],
    #   ]}

    print(await mango_client.balances())
    # [
    #   {'symbol': 'USDC', 'balance': 2.7435726906761744},
    #   {'symbol': 'SOL', 'balance': 0.1690007074236178},
    #   ...
    # ]

asyncio.run(main())
```