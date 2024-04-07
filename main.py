import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers import router

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))
disp = Dispatcher()


async def start():
    print('Bot has been started')
    disp.include_router(router=router)
    await disp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print('Bot has been stopped')
