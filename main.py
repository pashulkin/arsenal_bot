import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()    
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')