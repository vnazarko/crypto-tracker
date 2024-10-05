import asyncio
from datetime import datetime, timezone

import httpx
from bs4 import BeautifulSoup
from icecream import ic

from utils import get_price_binance, get_price_okx, get_price_bybit
from db_utils import update_coin
from database import collection
from models.enums import Coin


async def update_prices_in_db():
    while True:
        btc_binance = await get_price_binance('https://www.binance.com/ru/trade/BTC_USDT?type=spot')
        eth_binance = await get_price_binance('https://www.binance.com/ru/trade/ETH_USDT?type=spot')
        ton_binance = await get_price_binance('https://www.binance.com/ru/trade/TON_USDT?type=spot')

        btc_okx = await get_price_okx('https://www.okx.com/ru/trade-spot/btc-usdc')
        eth_okx = await get_price_okx('https://www.okx.com/ru/trade-spot/eth-usdt')
        ton_okx = await get_price_okx('https://www.okx.com/ru/trade-spot/ton-usdc')

        btc_bybit = await get_price_bybit('https://www.bybit.com/trade/usdt/BTCUSDT')
        eth_bybit = await get_price_bybit('https://www.bybit.com/trade/usdt/ETHUSDT')
        ton_bybit = await get_price_bybit('https://www.bybit.com/trade/usdt/TONUSDT')

        update_btc = await update_coin(coin_type=Coin.BTC.value, collection=collection, binance_price=btc_binance,
                                       okx_price=btc_okx, bybit_price=btc_bybit)
        update_eth = await update_coin(coin_type=Coin.ETH.value, collection=collection, binance_price=eth_binance,
                                       okx_price=eth_okx, bybit_price=eth_bybit)
        update_ton = await update_coin(coin_type=Coin.TON.value, collection=collection, binance_price=ton_binance,
                                       okx_price=ton_okx, bybit_price=ton_bybit)

        ic(f'{datetime.now(timezone.utc)} Цены обновлены')

        await asyncio.sleep(60)


async def main():
    await update_prices_in_db()


if __name__ == '__main__':
    asyncio.run(main())
