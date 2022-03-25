import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

# Using dotenv for load environ-variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    code = "`from aiogram import Bot`"
    print(message)
    await message.reply(code, parse_mode="Markdown")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
