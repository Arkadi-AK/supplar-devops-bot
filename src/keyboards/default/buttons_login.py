from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboards_login = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Info"),
            KeyboardButton(text="SIGN UP")
        ],
        [
            KeyboardButton(text="More")
        ],
    ],
    resize_keyboard=True
)
