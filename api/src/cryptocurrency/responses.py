from src.cryptocurrency.schemas import Coin
from src.models.responses import SuccessResponse


class SuccessGetCoins(SuccessResponse):
    payload: list[Coin]


class SuccessGetCurrentCoin(SuccessResponse):
    payload: Coin
