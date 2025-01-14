from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from loader import dp


@dp.message_handler(state=None, content_types=ContentType.TEXT)
async def bot_echo(message: types.Message):
    """
    Echo handler, which gets text messages without the specified state.
    """
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")


@dp.message_handler(state="*", content_types=types.ContentTypes.TEXT)
async def bot_echo_all(message: types.Message, state: FSMContext):
    """
    Echo handler, which gets all messages with the specified state.
    """
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
