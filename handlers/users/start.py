from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default.Tugmalar import Bosh_menyu_tugmalari_ru
from keyboards.default.Tugmalar import Lokatsiya_bolimi_tugmalari
from states.Statelar import *
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Здрасвствуйте, {message.from_user.full_name}!", reply_markup=Bosh_menyu_tugmalari_ru)
    await state.update_data({"til":"ru"})
    await Bosh_menyu_state_ru.Bosh_ru.set()
    print(f"fullname : {message.from_user.full_name}\n"
          f"username : {message.from_user.username}\n"
          f"user_id : {message.chat.id}\n")

    

