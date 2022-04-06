from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboards_guest = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Request to get admin permissions"),
            KeyboardButton(text="Quit"),
        ],
    ],
    resize_keyboard=True
)

keyboards_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Show users connected to bot"),
            KeyboardButton(text="Show status of server"),
        ],
    ],
    resize_keyboard=True
)
