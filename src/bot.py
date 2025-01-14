from aiogram import executor

from loader import dp
from src import middlewares, filters, handlers
from utils.db_api import db_gino
from utils.set_bot_commands import set_default_commands

__all__ = ["middlewares", "filters", "handlers"]


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    # Connecting to the database
    await db_gino.on_startup(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
