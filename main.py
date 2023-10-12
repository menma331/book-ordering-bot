import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from Connection import Connection
from handlers import router

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)


async def start():
    bot = Bot(token=os.getenv('TOKEN'))
    disp = Dispatcher()
    disp.include_router(router=router)
    await disp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print('Exit.')
