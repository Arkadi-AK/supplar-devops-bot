from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from src.keyboards.default import keyboards_login


@dp.message_handler(Command("reg"))
async def bot_register_user(message: types.Message):
    await message.answer(f"Будет зарегистрирован новый пользователь - {message.from_user.full_name}!",
                         reply_markup=keyboards_login)
    await message.answer(f"Хотите использовать имя - `{message.from_user.full_name}`?", parse_mode="Markdown")


@dp.message_handler(text="SIGN UP")
async def sign_up(message: types.Message):
    await message.answer(f"Введите имя пользователя, чтобы зарегистрироваться")


@dp.message_handler(text="Info")
async def info(message: types.Message):
    await message.answer(f"Существующий пользователь нажмите 'SIGN IN'\n"
                         f"Создать нового пользователя нажмите 'SIGN UP'")
