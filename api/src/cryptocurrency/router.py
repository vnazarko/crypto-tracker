import asyncio
import json
from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException, WebSocket
from icecream import ic

from src.cryptocurrency.schemas import Coin
from src.cryptocurrency.responses import SuccessGetCoins, SuccessGetCurrentCoin
from src.database import coins_collection

router = APIRouter(tags=['cryptocurrency'], prefix='/crypto')


@router.get('/get', response_model=SuccessGetCoins, response_model_exclude_none=True)
async def get_all_coins():
    coins = await coins_collection.find().to_list()
    coins_for_response = []

    for coin in coins:
        coins_for_response.append(Coin(
            name=coin['name'],
            coin_id=coin['coin_id'],
        ))

    return SuccessGetCoins(
        payload=coins_for_response
    )


@router.get('/get/{coin_id}', response_model=SuccessGetCurrentCoin)
async def get_current_coin(coin_id: int):
    coin = await coins_collection.find_one({'coin_id': coin_id})

    if not coin:
        raise HTTPException(
            status_code=404,
            detail='Coin not found'
        )

    coin_for_response = Coin(
        name=coin['name'],
        coin_id=coin['coin_id'],
        prices=coin['prices']
    )

    return SuccessGetCurrentCoin(
        payload=coin_for_response
    )


@router.websocket('/ws/{coin_id}')
async def get_price_of_current_coin(websocket: WebSocket, coin_id: int):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()

        if data == 'Get All Prices':
            while True:
                previous_prices = ''

                all_prices = await coins_collection.find_one({'coin_id': coin_id})

                two_hours_ago = datetime.utcnow() - timedelta(hours=2)
                prices = [dt for dt in all_prices['prices'] if dt['timestamp'] > two_hours_ago]

                if json.dumps(prices) != json.dumps(previous_prices):
                    await websocket.send_text(f"{prices}")
                await asyncio.sleep(15)

