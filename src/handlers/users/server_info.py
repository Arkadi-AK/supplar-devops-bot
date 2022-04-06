from aiogram import types

from data.config import ADMINS_ID
from keyboards.default.buttons_info_server import keyboards_info_server
from keyboards.default.keyboards_start import keyboards_guest, keyboards_admin
from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(text="Show status of server")
async def on_server_info(message: types.Message):
    if message.from_user.id in ADMINS_ID:
        await message.answer("Выберите нужную информацию", reply_markup=keyboards_info_server)
    else:
        await message.answer("Вы не являетесь администратором", reply_markup=keyboards_guest)


@dp.message_handler(text="Show users connected to bot")
async def on_server_info(message: types.Message):
    count = await commands.count_users()
    if message.from_user.id in ADMINS_ID:
        await message.answer(f"К боту подключено {count} пользователей", reply_markup=keyboards_admin)


@dp.message_handler(text="Back")
async def on_server_info(message: types.Message):
    await message.answer(text="Выберите действие", reply_markup=keyboards_admin)


@dp.message_handler(text="Server status")
async def on_server_info(message: types.Message):
    await message.answer("Статус сервера - ", reply_markup=keyboards_info_server)


@dp.message_handler(text="Memory storage")
async def on_server_info(message: types.Message):
    await message.answer("Memory storage - ", reply_markup=keyboards_info_server)


@dp.message_handler(text="Backup last day")
async def on_server_info(message: types.Message):
    await message.answer("Backup last day - ", reply_markup=keyboards_info_server)
