import logging

from aiogram import Dispatcher
from aiogram.utils.exceptions import ChatNotFound

from data.config import ADMINS_ID


async def on_startup_notify(dp: Dispatcher):
    logging.info("Оповещение администрации...")
    for admin in ADMINS_ID:
        try:
            await dp.bot.send_message(
                admin, f"<b>Это сообщение только для администраторов</b>\n"
                       "Бот был успешно запущен!",
                disable_notification=True
            )
        except ChatNotFound:
            logging.debug("Чат с админом не найден")
