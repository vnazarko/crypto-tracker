from fastapi import FastAPI
import uvicorn
import asyncio

from starlette.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.cryptocurrency.router import router as cryptocurrency_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(cryptocurrency_router)

origins = [
    "https://crypto-track.none1qq.ru",
    "https://api.crypto-track.none1qq.ru"
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)