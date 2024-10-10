from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.cryptocurrency.models import SuccessGetCoins
from src.database import coins_collection

router = APIRouter(tags=['cryptocurrency'], prefix='/crypto')


@router.get('/get', response_model=SuccessGetCoins)
async def all_coins():
    coins = await coins_collection.find().to_list()
    coins_for_response = []

    for coin in coins:
        coins_for_response.append(coin['name'])

    return JSONResponse(
        status_code=200,
        content={
            'status': 'ok',
            'payload': coins_for_response
        }
    )
