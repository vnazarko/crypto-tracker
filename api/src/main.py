from fastapi import FastAPI
import uvicorn
import asyncio

from database import collection, init_db

app = FastAPI()


async def main():
    uvicorn.run('main:app', reload=True)


if __name__ == '__main__':
    asyncio.run(main())
