from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CoinPriceDetail(BaseModel):
    rub: str
    usd: str


class CoinPrice(BaseModel):
    timestamp: datetime = None
    binance: CoinPriceDetail
    okx: CoinPriceDetail
    bybit: CoinPriceDetail


class Coin(BaseModel):
    name: str
    coin_id: int
    prices: Optional[list[CoinPrice]] = None


