
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message




logging.basicConfig(level=logging.INFO)

bot = Bot(token='7319987062:AAENQ0cQHTLwVpYlQRSTZxZmVQzapMoBmY4')
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer('Привет!')


async def main():    
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')