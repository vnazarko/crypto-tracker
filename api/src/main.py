from fastapi import FastAPI
import uvicorn
import asyncio

from src.database import collection, init_db

app = FastAPI()

