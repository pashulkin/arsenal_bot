from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Players')],
        [KeyboardButton(text='Goalkeepers'), KeyboardButton(text='Defenders')],
        [KeyboardButton(text='Midfielders'), KeyboardButton(text='Forwards')]
], 
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...')

