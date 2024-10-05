import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
if __name__ == '__main__':
    from config import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD
    from models.models import Coin
else:
    from src.config import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD
    from src.models.models import Coin

MONGO_DETAILS = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client['crypto-tracker']
coins_collection = database.get_collection("coins")
users_collection = database.get_collection("users")


async def init_db():
    btc = Coin(name='BTC')
    eth = Coin(name='ETH')
    ton = Coin(name='TON')

    result = coins_collection.insert_many([btc.__str__(), eth.__str__(), ton.__str__()])

    print('База данных Mongo инициализирована')

if __name__ == '__main__':
    asyncio.run(init_db())
