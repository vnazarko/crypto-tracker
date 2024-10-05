from fastapi import FastAPI
import uvicorn
import asyncio

from src.auth.router import router as auth_router

app = FastAPI()

app.include_router(auth_router)