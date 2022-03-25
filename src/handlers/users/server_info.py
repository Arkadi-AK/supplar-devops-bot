from aiogram import types

from data.config import ADMINS_ID
from keyboards.default import keyboards_login
from keyboards.default.buttons_info_server import keyboards_info_server
from loader import dp


@dp.message_handler(text="More")
async def on_server_info(message: types.Message):
    if str(message.from_user.id) in ADMINS_ID:
        await message.answer("Информация", reply_markup=keyboards_info_server)
    else:
        await message.answer("Вы не являетесь администратором", reply_markup=keyboards_login)
