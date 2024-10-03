import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD

MONGO_DETAILS = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client['crypto-tracker']
collection = database.get_collection("coins")