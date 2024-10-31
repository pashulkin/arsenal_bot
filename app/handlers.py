from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb
import database.user_data as user_data
from squad import players, goalkeepers, defenders, midfielders, forwards

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_data.add_user(user_id, first_name, last_name)
    await message.answer(f'Hello, {message.from_user.first_name}!',
                         reply_markup=kb.main)
    

@router.message(F.text == 'Players')
async def cmd_players(message: Message):
    await message.answer('\n'.join(players), reply_markup=kb.main)


@router.message(F.text == 'Goalkeepers')
async def cmd_goalkeepers(message: Message):
    await message.answer('\n'.join(goalkeepers), reply_markup=kb.main)


@router.message(F.text == 'Defenders')
async def cmd_defenders(message: Message):
    await message.answer('\n'.join(defenders), reply_markup=kb.main)


@router.message(F.text == 'Midfielders')
async def cmd_midfielders(message: Message):
    await message.answer('\n'.join(midfielders), reply_markup=kb.main)


@router.message(F.text == 'Forwards')
async def cmd_forwards(message: Message):
    await message.answer('\n'.join(forwards), reply_markup=kb.main)