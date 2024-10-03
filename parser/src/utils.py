import asyncio
import time

import httpx
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium_stealth import stealth
from icecream import ic


def init_webdriver() -> WebDriver:
    driver = webdriver.Chrome()
    stealth(driver, platform='Win32')
    return driver


def get_rub_price():
    url = 'https://www.rbc.ru/quote/ticker/72413'
    page = httpx.get(url).text

    soup = BeautifulSoup(page, 'lxml')

    price = soup.find('span', {'class': 'chart__info__sum'}).text[1:]

    return price.replace(',', '.')


async def get_price_binance(url: str) -> dict:
    if url.startswith('https://www.binance.com/ru/trade/'):
        driver = init_webdriver()
        driver.get(url)

        await asyncio.sleep(1)

        try:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            price = soup.find('div', {'class': 'showPrice'}).text.replace(',', ' ')

            return {
                'usd': price,
                'rub': str(round(float(price.replace(' ', '')) * float(get_rub_price()), 2))
            }
        except Exception as e:
            return {
                'usd': '0',
                'rub': '0'
            }
    else:
        ic('Invalid URL for Binance')


async def get_price_okx(url: str) -> dict:
    if url.startswith('https://www.okx.com/ru/trade-spot/'):
        driver = init_webdriver()
        driver.get(url)

        await asyncio.sleep(2)
        try:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            price = soup.find('title').text.split(' ')[0].replace('\xa0', ' ').replace(',', '.')
            return {
                'usd': price,
                'rub': str(round(float(price.replace(' ', '')) * float(get_rub_price()), 2))
            }
        except Exception as e:
            return {
                'usd': '0',
                'rub': '0'
            }
    else:
        ic('Invalid URL for OKX')


async def get_price_bybit(url: str) -> dict:
    if url.startswith('https://www.bybit.com/trade/'):
        driver = init_webdriver()
        driver.get(url)

        await asyncio.sleep(2)
        try:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            price = soup.find('span', {'class': 'chart__head-left--price'}).text.replace(',', ' ')
            return {
                'usd': price,
                'rub': str(round(float(price.replace(' ', '')) * float(get_rub_price()), 2))
            }
        except Exception as e:
            return {
                'usd': '0',
                'rub': '0'
            }
    else:
        ic('Invalid URL for Bybit')
