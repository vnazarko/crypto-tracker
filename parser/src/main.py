import asyncio
import httpx
from bs4 import BeautifulSoup
from icecream import ic

from utils import get_price_binance, get_price_okx, get_price_bybit

link = 'https://browser-info.ru/'


async def main():
    btc_binance = await get_price_binance('https://www.binance.com/ru/trade/BTC_USDT?type=spot')
    eth_binance = await get_price_binance('https://www.binance.com/ru/trade/ETH_USDT?type=spot')
    ton_binance = await get_price_binance('https://www.binance.com/ru/trade/TON_USDT?type=spot')
    ic(btc_binance)
    ic(eth_binance)
    ic(ton_binance)

    btc_okx = await get_price_okx('https://www.okx.com/ru/trade-spot/btc-usdc')
    eth_okx = await get_price_okx('https://www.okx.com/ru/trade-spot/eth-usdt')
    ton_okx = await get_price_okx('https://www.okx.com/ru/trade-spot/ton-usdc')
    ic(btc_okx)
    ic(eth_okx)
    ic(ton_okx)

    btc_bybit = await get_price_bybit('https://www.bybit.com/trade/usdt/BTCUSDT')
    eth_bybit = await get_price_bybit('https://www.bybit.com/trade/usdt/ETHUSDT')
    ton_bybit = await get_price_bybit('https://www.bybit.com/trade/usdt/TONUSDT')
    ic(btc_bybit)
    ic(eth_bybit)
    ic(ton_bybit)


if __name__ == '__main__':
    asyncio.run(main())
