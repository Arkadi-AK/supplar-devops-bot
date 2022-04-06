from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_admin = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Add to Administrators",
                                                callback_data="yes"
                                            ),
                                            InlineKeyboardButton(
                                                text="Cancel",
                                                callback_data="no"
                                            ),
                                        ],
                                    ], )
