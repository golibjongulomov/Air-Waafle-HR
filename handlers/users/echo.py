from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(text=f"Iltimos, botdan foydalanish uchun /start tugmasini bosing!\nПожалуйста, нажмите /start, чтобы использовать бота!")
