from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboards_info_server = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Server status"),
            KeyboardButton(text="Memory storage"),
            KeyboardButton(text="Backup last day"),
        ],
        [
            KeyboardButton(text="More")
        ],
    ],
    resize_keyboard=True
)
