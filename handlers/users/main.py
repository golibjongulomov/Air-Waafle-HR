from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from loader import dp, bot
from keyboards.default.Tugmalar import *
from states.Statelar import *
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="Biz haqimizda", state=Bosh_menyu_state.Bosh)
async def familya(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=AgACAgIAAxkBAAIW42XJojOEu45tJxSqpsjom8rCbY9hAAKx0DEbM09QSlCIN9sTthqNAQADAgADeQADNAQ, caption=f"Air Waffle – Gong Kong vaflilari")
    await Bosh_menyu_state.Bosh.set()

@dp.message_handler(text="🖋Vakansiyalar", state=Bosh_menyu_state.Bosh)
async def vakansiyaga_otkaz(message: types.Message):
    await message.answer(f"Air waffle jamoasiga qo\'shiling!\nFilialni tanlang:", reply_markup=Lokatsiya_bolimi_tugmalari)
    await Vakansiyalar_state.Lokatsiya_tanlash.set()

@dp.message_handler(text="🇷🇺/🇺🇿Tilni tanlash", state=Bosh_menyu_state.Bosh)
async def tilni_tanlash(message: types.Message):
    await message.answer(text=f"Tilni tanlang:", reply_markup=Til_tanlash_tugmalari)
    await Bosh_menyu_state.Tilni_tanlash.set()

@dp.message_handler(text="🇷🇺Русский", state=Bosh_menyu_state.Tilni_tanlash)
async def tilni_ozgartir(message: types.Message, state: FSMContext):
    await message.answer(text=f"Выберите раздел:", reply_markup=Bosh_menyu_tugmalari_ru)
    await state.update_data({"til":"ru"})
    await Bosh_menyu_state_ru.Bosh_ru.set()
"""________________________________________________________________________________________________________"""


@dp.message_handler(text="О нас", state=Bosh_menyu_state_ru.Bosh_ru)
async def familya(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=AgACAgIAAxkBAAIW42XJojOEu45tJxSqpsjom8rCbY9hAAKx0DEbM09QSlCIN9sTthqNAQADAgADeQADNAQ, caption=f"Air Waffle – Гонконгские вафли")
    await Bosh_menyu_state_ru.Bosh_ru.set()

@dp.message_handler(text="🖋Вакансии", state=Bosh_menyu_state_ru.Bosh_ru)
async def vakansiyaga_otkaz(message: types.Message):
    await message.answer(f"Присоединяйтесь к команде Air Waffle! \nВыберите филиал:", reply_markup=Lokatsiya_bolimi_tugmalari_ru)
    await Vakansiyalar_state_ru.Lokatsiya_tanlash_ru.set()

@dp.message_handler(text="🇷🇺/🇺🇿Выбор языка", state=Bosh_menyu_state_ru.Bosh_ru)
async def tilni_tanlash(message: types.Message):
    await message.answer(text=f"Выберите язык:", reply_markup=Til_tanlash_tugmalari_ru)
    await Bosh_menyu_state_ru.Tilni_tanlash_ru.set()


@dp.message_handler(text="🇺🇿O\'zbekcha", state=Bosh_menyu_state_ru.Tilni_tanlash_ru)
async def tilni_ozgartir(message: types.Message, state: FSMContext):
    await message.answer(text=f"Bo'limni tanlang:", reply_markup=Bosh_menyu_tugmalari)
    await state.update_data({"til":"uz"})
    await Bosh_menyu_state.Bosh.set()
