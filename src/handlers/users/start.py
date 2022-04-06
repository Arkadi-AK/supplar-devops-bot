from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from data.config import ADMINS_ID, SUPERUSER
from keyboards.default.keyboards_start import keyboards_admin, keyboards_guest
from keyboards.inline.choice_admin_perm import choice_admin
from loader import dp, bot
from utils.db_api import quick_commands as commands

temp_message: types.Message


@dp.message_handler(CommandStart())
@dp.throttled(rate=2)
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    if message.from_user.id in ADMINS_ID:
        await message.answer(f"Привет, {name}!\n"
                             f"Вы являетесь администратором",
                             reply_markup=keyboards_admin)
    else:
        await message.answer(f"Привет, {name}!",
                             reply_markup=keyboards_guest)


@dp.message_handler(text="Request to get admin permissions")
async def request_admin_perm(message: types.Message):
    await message.answer(f"Запрос на получение админ прав отправлен", reply_markup=types.ReplyKeyboardRemove())
    user = message.from_user.username
    await dp.bot.send_message(chat_id=SUPERUSER,
                              text=f"Пользователь <b>{user}</b> (`id = {message.from_user.id}`)\n"
                                   f"запрашивает права администратора",
                              reply_markup=choice_admin
                              )
    global temp_message
    temp_message = message


@dp.callback_query_handler(lambda c: c.data == 'yes' or 'no')
async def answer_admin_perm(call: CallbackQuery):
    await bot.answer_callback_query(callback_query_id=call.id, cache_time=5)
    if call.data == "yes":
        await commands.add_user(telegram_id=temp_message.from_user.id,
                                first_name=temp_message.from_user.full_name,
                                username=temp_message.from_user.username
                                )
        await dp.bot.send_message(chat_id=call.from_user.id,
                                  text=f"Пользователь <b>{temp_message.from_user.username}</b>\n"
                                       f"(`id = {temp_message.from_user.id}`)\n"
                                       f"добавлен в список администраторов",
                                  )
        await dp.bot.send_message(chat_id=temp_message.from_user.id,
                                  text="Теперь вы администратор",
                                  reply_markup=keyboards_admin
                                  )
    if call.data == "no":
        await dp.bot.send_message(chat_id=call.from_user.id,
                                  text=f"Пользователь не добавлен в список администраторов"
                                  )
        await dp.bot.edit_message_text(
            text=call.message.text,
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        await dp.bot.send_message(chat_id=temp_message.from_user.id,
                                  text="Извините, вы не можете быть администратором"
                                  )
