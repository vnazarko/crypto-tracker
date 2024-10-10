from pydantic import BaseModel

from src.models.responses import SuccessResponse


class Coin(BaseModel):
    name: str


class SuccessGetCoins(SuccessResponse):
    payload: list[Coin]