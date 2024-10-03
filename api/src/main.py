from fastapi import FastAPI
import uvicorn
import asyncio

from database import collection, init_db

app = FastAPI()

