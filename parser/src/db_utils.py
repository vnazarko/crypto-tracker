from datetime import datetime, timezone

from icecream import ic
from motor.motor_asyncio import AsyncIOMotorCollection

from models.enums import Coin


async def update_coin(coin_type: Coin, collection: AsyncIOMotorCollection, binance_price: dict, okx_price: dict, bybit_price: dict):
    try:
        prices = await get_coin_price(coin_type=coin_type, collection=collection)

        if prices is not None:
            prices.append({
                'timestamp': datetime.now(timezone.utc),
                'binance': binance_price,
                'okx': okx_price,
                'bybit': bybit_price
            })

            update_btc = await collection.update_one(
                {'name': coin_type},
                {
                    '$set': {
                        'prices': prices
                    }
                }
            )
        else:
            ic(f'Произошла ошибка при обновлении цен {coin_type}')
    except Exception as e:
        ic(f'Произошла ошибка при обновлении цен {coin_type}')


async def get_coin_price(coin_type: Coin, collection: AsyncIOMotorCollection):
    try:
        coin_data = await collection.find_one({'name': coin_type})
        if coin_data:
            return coin_data['prices']
        else:
            ic(f'Данные о ценах для {coin_type} не найдены')
            return None
    except:
        ic(f'Произошла ошибка при получении цен {coin_type}')
        return None