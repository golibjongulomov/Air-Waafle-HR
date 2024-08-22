from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from loader import dp, bot
from keyboards.default.Tugmalar import *
from states.Statelar import *
from aiogram.dispatcher import FSMContext
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData

@dp.message_handler(text="❌Отмена", state="*")
async def lokatsiya_oluvchi(message: types.Message, state: FSMContext):
    await message.answer(f"Выберите раздел:", reply_markup=Bosh_menyu_tugmalari_ru)
    await Bosh_menyu_state_ru.Bosh_ru.set()

@dp.message_handler(state=Vakansiyalar_state_ru.Lokatsiya_tanlash_ru)
async def lokatsiya_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Выберите раздел:", reply_markup=Bosh_menyu_tugmalari_ru)
        await Bosh_menyu_state_ru.Bosh_ru.set() 
    else:  
        chat_id = message.chat.id
        from handlers.funksiyalar import send_user_location
        user_id = message.from_user.id
        if message.text == f"📍Magic City":
            latitude = 41.303148198871305  
            longitude = 69.2454436138731 
            await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Выберите интересующую Вас вакансию:", reply_markup=Lavozim_tanlash_tugmalari_m1_s1_ru)
            await Vakansiyalar_state_ru.Ish_orni_olish_ru.set()
        elif message.text == f"📍Seoul Mun":
            latitude = 41.29910224041661
            longitude = 69.24690418546267
            await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Выберите интересующую Вас вакансию:", reply_markup=Lavozim_tanlash_tugmalari_m1_s1_ru)
            await Vakansiyalar_state_ru.Ish_orni_olish_ru.set()
        elif message.text == f"📍Национальный парк":
            latitude = 41.30293396835559 
            longitude = 69.24080897938212
            await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Выберите интересующую Вас вакансию:", reply_markup=Lavozim_tanlash_tugmalari_ru)
            await Vakansiyalar_state_ru.Ish_orni_olish_ru.set()
        elif message.text == f"📍Broadway":
            latitude = 41.311993303350874 
            longitude = 69.27420855094067
            await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Выберите интересующую Вас вакансию:", reply_markup=Lavozim_tanlash_tugmalari_ru)
            await Vakansiyalar_state_ru.Ish_orni_olish_ru.set()
        elif message.text == f"📍Центральный парк":
            latitude = 41.31270419098545
            longitude = 69.29877042978262
            await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Выберите интересующую Вас вакансию:", reply_markup=Lavozim_tanlash_tugmalari_ru)
            await Vakansiyalar_state_ru.Ish_orni_olish_ru.set()
        await state.update_data({"Filial":message.text})
    
@dp.message_handler(state=Vakansiyalar_state_ru.Ish_orni_olish_ru)
async def lavozim_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Выберите филиал:", reply_markup=Lokatsiya_bolimi_tugmalari_ru)
        await Vakansiyalar_state_ru.Lokatsiya_tanlash_ru.set()
    else:
        if message.text == f"Кассир":
            await message.answer(f"""Основные требования к соискателю:
∙ умею свободно общаться на русском и узбекском языках, умею общаться на английском языке на среднем уровне;
∙ Быть активным и вежливым;
∙ Доброжелательность и позитивный настрой в работе;
∙ Ответственность и честность;
∙ Навыки работы в команде;
∙ Стрессоустойчивость;
∙ Навыки работы с контрольно-кассовой техникой;
∙ Опыт работы кассиром не менее 3-х месяцев.""")
            await message.answer(f"Выберите пол:", reply_markup=Jinsni_tanlash_tugmalari_ru)
            await Vakansiyalar_state_ru.Jinsini_olish_ru.set()
        elif message.text == f"Рабочий кухни":
            await message.answer(f"""Основные требования к соискателю:
∙ Быть активным и вежливым;
∙ Доброжелательность и позитивный настрой в работе;
∙ Ответственность и честность;
∙ Высокая скорость обучения;
∙ Навыки работы в команде;
∙ Стрессоустойчивость;
∙ Опыт работы не требуется – всему обучаем сами!

Основные обязанности:
∙ Приготовление еды в соответствии с технологиями и стандартами компании;
∙ Обслуживание гостей по стандартам компании:
∙ работа на кассе для приема заказов;
∙ раздача заказов гостям;
∙ Поддержание чистоты на рабочем месте, в кухонной зоне;
∙ Соблюдение стандартов внешнего вида, принятых в компании;
∙ Соблюдение технических правил охраны труда и техники безопасности на рабочем месте;""")
            await message.answer(f"Выберите пол:", reply_markup=Jinsni_tanlash_tugmalari_ru)
            await Vakansiyalar_state_ru.Jinsini_olish_ru.set()  
        elif message.text == f"Бариста":
            await message.answer(f"""Основные требования к соискателю:
∙ Быть активным и вежливым;
∙ Доброжелательность и позитивный настрой в работе;
∙ Ответственность и честность;
∙ Высокая скорость обучения;
∙ Навыки работы в команде;
∙ Стрессоустойчивость;
∙ Опыт работы не требуется – всему обучаем сами!

Основные обязанности:
∙ Приготовление еды в соответствии с технологиями и стандартами компании;
∙ Обслуживание гостей по стандартам компании:
∙ работа на кассе для приема заказов;
∙ раздача заказов гостям;
∙ Поддержание чистоты на рабочем месте, в кухонной зоне;
∙ Соблюдение стандартов внешнего вида, принятых в компании;
∙ Соблюдение технических правил охраны труда и техники безопасности на рабочем месте;""")
            await message.answer(f"Выберите пол:", reply_markup=Jinsni_tanlash_tugmalari_ru)
            await Vakansiyalar_state_ru.Jinsini_olish_ru.set()    
        elif message.text == f"Ранер":
            await message.answer(f"""Основные требования к соискателю:
∙ Быть активным и вежливым;
∙ Доброжелательность и позитивный настрой в работе;
∙ Ответственность и честность;
∙ Стрессоустойчивость;
                                 
Основные обязанности:
∙ Обслуживание гостей по стандартам компании:
∙ работа в зале обслуживания гостей;
∙ Поддержание чистоты на рабочем месте, в зоне ресторана;
∙ Соблюдение стандартов внешнего вида, принятых в компании;
∙ Соблюдение технических правил охраны труда и техники безопасности на рабочем месте;""")
            await message.answer(f"Выберите пол:", reply_markup=Jinsni_tanlash_tugmalari_ru)
            await Vakansiyalar_state_ru.Jinsini_olish_ru.set()
        elif message.text == f"Техничка":
            await message.answer(f"""Основные требования к соискателю:
∙ Доброжелательность и позитивный настрой в работе;
∙ Ответственность и честность;
∙ Стрессоустойчивость;

Основные обязанности:
∙ Поддержание чистоты на рабочем месте, в зоне ресторана;
∙ Поддержание посуды в чистоте и подготовка ее к быстрому использованию;
∙ Соблюдение технических правил охраны труда и техники безопасности на рабочем месте;""")
            await message.answer(f"Выберите пол:", reply_markup=Jinsni_tanlash_tugmalari_ru)
            await Vakansiyalar_state_ru.Jinsini_olish_ru.set()
        await state.update_data({"Lavozim":message.text})
    
@dp.message_handler(state=Vakansiyalar_state_ru.Jinsini_olish_ru)
async def jins_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Присоединяйтесь к команде Air Waffle! \nВыберите филиал:", reply_markup=Lokatsiya_bolimi_tugmalari_ru)
        await Vakansiyalar_state_ru.Lokatsiya_tanlash_ru.set()
    else:
        if message.text == f"Мужчина":
            await message.answer(text=f"Введите ФИО (Иванов Иван Иванович)", reply_markup=bekor_ortga_tugmalari_ru)
            await Vakansiyalar_state_ru.FIO_olish_ru.set()
        elif message.text == "Женщина":
            await message.answer(text=f"Введите ФИО (Иванов Иван Иванович)", reply_markup=bekor_ortga_tugmalari_ru) 
            await Vakansiyalar_state_ru.FIO_olish_ru.set()
        await state.update_data({"Jinsi":message.text}) 
    
@dp.message_handler(state=Vakansiyalar_state_ru.FIO_olish_ru)
async def ism_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Выберите пол:", reply_markup=Jinsni_tanlash_tugmalari_ru)
        await Vakansiyalar_state_ru.Jinsini_olish_ru.set()
    else:
        from handlers.funksiyalar import filter_name
        input_name = message.text
        filtered_name = filter_name(input_name)

        if filtered_name:
            await state.update_data({"Ism":message.text})
            await message.answer(f"Укажите дату своего рождения (пример, 30.10.2003):", reply_markup=bekor_ortga_tugmalari_ru)
            await Vakansiyalar_state_ru.Tugilgan_sana_olish_ru.set()
        else:
            await message.answer(f"Неправильный формат имени, введите еще раз:")

@dp.message_handler(state=Vakansiyalar_state_ru.Tugilgan_sana_olish_ru)
async def sana_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(text=f"Введите ФИО (Иванов Иван Иванович)", reply_markup=bekor_ortga_tugmalari_ru)
        await Vakansiyalar_state_ru.FIO_olish_ru.set()
    else:
        from handlers.funksiyalar import filter_birthdate
        input_date = message.text
        filtered_birthdate = filter_birthdate(input_date)
        if filtered_birthdate:
            await state.update_data({"Tugilgan_sana":message.text})
            await message.answer("Укажите свой адрес проживания", reply_markup=lokatsiya_jonatish_tugmalari_ru)
            await Vakansiyalar_state_ru.Adres_olish_ru.set()
        else:
            await message.answer(f"Неверная дата, пожалуйста, введите еще раз:")

@dp.message_handler(content_types=types.ContentType.LOCATION, state=Vakansiyalar_state_ru.Adres_olish_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await message.answer(f"Отправьте свой номер телефона:", reply_markup=raqam_jonatish_tugmalari_ru)
    await state.update_data({"latitude":latitude, "longitude":longitude},)
    await Vakansiyalar_state_ru.Telefon_olish_ru.set()
    
@dp.message_handler(state=Vakansiyalar_state_ru.Adres_olish_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Укажите дату своего рождения (пример, 30.10.2003):", reply_markup=bekor_ortga_tugmalari_ru)
        await Vakansiyalar_state_ru.Tugilgan_sana_olish_ru.set()
    else:
        await message.answer(f"Пожалуйста отправить правильное местоположение")

@dp.message_handler(content_types=types.ContentType.CONTACT, state=Vakansiyalar_state_ru.Telefon_olish_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    contact = message.contact
    phone_number = contact.phone_number
    await state.update_data({"raqam":phone_number})
    await message.answer(f"Вы студент?", reply_markup=Ha_yoq_tugmalari_ru)
    await Vakansiyalar_state_ru.Studentlikni_sorash_ru.set()
    
@dp.message_handler(state=Vakansiyalar_state_ru.Telefon_olish_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer("Укажите свой адрес проживания", reply_markup=lokatsiya_jonatish_tugmalari_ru)
        await Vakansiyalar_state_ru.Adres_olish_ru.set()
    else:
        from handlers.funksiyalar import filter_phone_number
        phone_number = message.text
        filtered_phone_number = filter_phone_number(phone_number)
        if filtered_phone_number:
            await state.update_data({"raqam":phone_number})
            await message.answer(f"Вы студент?", reply_markup=Ha_yoq_tugmalari_ru)
            await Vakansiyalar_state_ru.Studentlikni_sorash_ru.set()
        else:
            print(f"Пожалуйста, отправьте номер в правильном формате:")

@dp.message_handler(state=Vakansiyalar_state_ru.Studentlikni_sorash_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Отправьте свой номер телефона:", reply_markup=raqam_jonatish_tugmalari_ru)
        await Vakansiyalar_state_ru.Telefon_olish_ru.set()
    elif message.text == f"✅Да":
        await state.update_data({"Talabalik":"✅Ha"})
        await message.answer(f"На какой форме обучения вы учитесь?", reply_markup=Talim_shakli_tugmalari_ru)
        await Vakansiyalar_state_ru.Talim_shaklini_sorash_ru.set()
    elif message.text == f"❌Нет":
        await state.update_data({"Talabalik":message.text})
        await state.update_data({"Talim_shakli":"–"})
        await message.answer(f"Каково ваше образование?", reply_markup=Malumot_tugmalari_ru)
        await Vakansiyalar_state_ru.Malumotini_sorash_ru.set()
    else: 
        await message.answer(f"Пожалуйста, отправьте один из ответов:")
    
@dp.message_handler(state=Vakansiyalar_state_ru.Malumotini_sorash_ru)
async def malumot_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Вы студент?", reply_markup=Ha_yoq_tugmalari_ru)
        await Vakansiyalar_state_ru.Studentlikni_sorash_ru.set()
    elif message.text == f"Среднее":
        await state.update_data({"Malumoti":message.text})
        await message.answer(f"Какой у вас уровень знания русского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ruskiy_sorash_ru.set()
    elif message.text == f"Средне-специальное":
        await state.update_data({"Malumoti":message.text})
        await message.answer(f"Какой у вас уровень знания русского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ruskiy_sorash_ru.set()
    elif message.text == f"Высшее":
        await state.update_data({"Malumoti":message.text})
        await message.answer(f"Какой у вас уровень знания русского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ruskiy_sorash_ru.set()
    else:
        message.answer(f"Пожалуйста, отправьте один из ответов:")


@dp.message_handler(state=Vakansiyalar_state_ru.Talim_shaklini_sorash_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Вы студент?", reply_markup=Ha_yoq_tugmalari_ru)
        await Vakansiyalar_state_ru.Studentlikni_sorash_ru.set()
    elif message.text == f"Очное":
        await state.update_data({"Talim_shakli":message.text})
        await message.answer(f"Какой у вас уровень знания русского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ruskiy_sorash_ru.set()
    elif message.text == f"Вечернее":
        await state.update_data({"Talim_shakli":message.text})
        await message.answer(f"Какой у вас уровень знания русского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ruskiy_sorash_ru.set()
    elif message.text == f"Заочное":
        await state.update_data({"Talim_shakli":message.text})
        await message.answer(f"Какой у вас уровень знания русского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ruskiy_sorash_ru.set()
    else:
        await message.answer(f"Пожалуйста, отправьте один из ответов:")

@dp.message_handler(state=Vakansiyalar_state_ru.Ruskiy_sorash_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"На какой форме обучения вы учитесь?", reply_markup=Talim_shakli_tugmalari_ru)
        await Vakansiyalar_state_ru.Talim_shaklini_sorash_ru.set()
    elif message.text == f"Начальный":
        await state.update_data({"Rus_tili_darajasi":message.text})
        await message.answer(f"Какой у вас уровень знания узбекского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ozbek_sorash_ru.set()
    elif message.text == f"Средний":
        await state.update_data({"Rus_tili_darajasi":message.text})
        await message.answer(f"Какой у вас уровень знания узбекского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ozbek_sorash_ru.set()
    elif message.text == f"Свободный":
        await state.update_data({"Rus_tili_darajasi":message.text})
        await message.answer(f"Какой у вас уровень знания узбекского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ozbek_sorash_ru.set()
    else:
        await message.answer(f"Пожалуйста, отправьте один из ответов:")

@dp.message_handler(state=Vakansiyalar_state_ru.Ozbek_sorash_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Какой у вас уровень знания русского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ruskiy_sorash_ru.set()
    elif message.text == f"Начальный":
        await state.update_data({"Ozbek_tili_darajasi":message.text})
        await message.answer(f"Какая зарплата вас устраивает?", reply_markup=Ish_haqi_tugmalari_ru)
        await Vakansiyalar_state_ru.Oylik_sorash_ru.set()
    elif message.text == f"Средний":
        await state.update_data({"Ozbek_tili_darajasi":message.text})
        await message.answer(f"Какая зарплата вас устраивает?", reply_markup=Ish_haqi_tugmalari_ru)
        await Vakansiyalar_state_ru.Oylik_sorash_ru.set()
    elif message.text == f"Свободный":
        await state.update_data({"Ozbek_tili_darajasi":message.text})
        await message.answer(f"Какая зарплата вас устраивает?", reply_markup=Ish_haqi_tugmalari_ru)
        await Vakansiyalar_state_ru.Oylik_sorash_ru.set()
    else:
        await message.answer(f"Пожалуйста, отправьте один из ответов:")

@dp.message_handler(state=Vakansiyalar_state_ru.Oylik_sorash_ru)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Какой у вас уровень знания узбекского языка?", reply_markup=Til_bilish_tugmalari_ru)
        await Vakansiyalar_state_ru.Ozbek_sorash_ru.set()
    elif message.text == f"1,5-2 млн":
        await state.update_data({"Maosh":message.text})
        await message.answer(f"Пожалуйста, пришлите свое фото (возможно селфи)", reply_markup=bekor_ortga_tugmalari_ru)
        await Vakansiyalar_state_ru.Rasm_sorash_ru.set()
    elif message.text == f"2-3 млн":
        await state.update_data({"Maosh":message.text})
        await message.answer(f"Пожалуйста, пришлите свое фото (возможно селфи)", reply_markup=bekor_ortga_tugmalari_ru)
        await Vakansiyalar_state_ru.Rasm_sorash_ru.set()
    elif message.text == f"3-4 млн":
        await state.update_data({"Maosh":message.text})
        await message.answer(f"Пожалуйста, пришлите свое фото (возможно селфи)", reply_markup=bekor_ortga_tugmalari_ru)
        await Vakansiyalar_state_ru.Rasm_sorash_ru.set()
    elif message.text == f"5 млн +":
        await state.update_data({"Maosh":message.text})
        await message.answer(f"Пожалуйста, пришлите свое фото (возможно селфи)", reply_markup=bekor_ortga_tugmalari_ru)
        await Vakansiyalar_state_ru.Rasm_sorash_ru.set()
    else:
        message.answer(f"Пожалуйста, отправьте один из ответов:")
    
@dp.message_handler(content_types=types.ContentType.PHOTO, state=Vakansiyalar_state_ru.Rasm_sorash_ru)
async def rasm_oluvchi(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data({"photo_id":photo_file_id})
    user_id = message.from_user.id
    data = await state.get_data()
    filial = data.get("Filial")
    lavozim = data.get("Lavozim")
    jins = data.get("Jinsi")
    ism = data.get("Ism")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    tugilgan_sana = data.get("Tugilgan_sana")
    telefon = data.get("raqam")
    talaba = data.get("Talaba")
    talim_shakli = data.get("Talim_shakli")
    malumoti = data.get("Malumoti")
    rus_tili = data.get("Rus_tili_darajasi")
    ozbek_tili = data.get("Ozbek_tili_darajasi")
    maosh = data.get("Maosh")
    caption = f"Филиал: {filial}\nДолжность: {lavozim}\nПол: {jins}\nФИО: {ism}\nДата рождения: {tugilgan_sana}\nТелефон: {telefon}\nСтудент: {talaba}\nФорма образования: {talim_shakli}\nОбразования: {malumoti}\nРусский язык: {rus_tili}\nУзбекский язык: {ozbek_tili}\nЗарплата: {maosh}"
    await bot.send_photo(user_id, photo=photo_file_id, caption=caption)
    await message.answer(f"Вы даете согласие на обработку ваших данных?", reply_markup=Rozilik_tugmalari_ru)
    await Vakansiyalar_state_ru.Ruxsat_sorash_ru.set()

@dp.message_handler(state=Vakansiyalar_state_ru.Rasm_sorash_ru)
async def rasm_oluvchi_rasm_emas(message: types.Message, state: FSMContext):
    if message.text == f"↩️Назад":
        await message.answer(f"Какая зарплата вас устраивает?", reply_markup=Ish_haqi_tugmalari_ru)
        await Vakansiyalar_state_ru.Oylik_sorash_ru.set()
    else:
        await message.answer(f"Пожалуйста, пришлите свое фото!")

@dp.message_handler(state=Vakansiyalar_state_ru.Ruxsat_sorash_ru)
async def ruxsat_oluvchi_funksiya(message: types.Message, state: FSMContext):
    if message.text == f"✅Подтверждать отправки":
        data = await state.get_data()
        filial = data.get("Filial")
        lavozim = data.get("Lavozim")
        jins = data.get("Jinsi")
        ism = data.get("Ism")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        tugilgan_sana = data.get("Tugilgan_sana")
        telefon = data.get("raqam")
        talaba = data.get("Talabalik")
        talim_shakli = data.get("Talim_shakli")
        malumoti = data.get("Malumoti")
        rus_tili = data.get("Rus_tili_darajasi")
        ozbek_tili = data.get("Ozbek_tili_darajasi")
        maosh = data.get("Maosh")
        photo_id = data.get("photo_id")
        caption = f"Филиал: {filial}\nДолжность: {lavozim}\nПол: {jins}\nФИО: {ism}\nДата рождения: {tugilgan_sana}\nТелефон: {telefon}\nСтудент: {talaba}\nФорма образования: {talim_shakli}\nОбразования: {malumoti}\nРусский язык: {rus_tili}\nУзбекский язык: {ozbek_tili}\nЗарплата: {maosh}"
        
        inline_tugmalar_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton(text=f"Vakansiya yo\'q", callback_data=message.from_user.id)
        inline_tugmalar_markup.add(button)
        
        await bot.send_location(-1002189488233, latitude=latitude, longitude=longitude)
        await bot.send_photo(-1002189488233, photo=photo_id, caption=caption, reply_markup=inline_tugmalar_markup)
        await message.answer(f"Резюме отправлено, мы свяжемся с вами в ближайшее время!", reply_markup=Bosh_menyu_tugmalari_ru)
        await Bosh_menyu_state_ru.Bosh_ru.set()
        

# @dp.callback_query_handler(state="*")
# async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
#     await bot.answer_callback_query(callback_query.id, text=f"Xabar yuborildi")
#     await bot.send_message(callback_query.data, f"Благодарим вас за интерес к тому, чтобы стать членом команды Air Waffle. К сожалению, на данный момент вакансий по данной вакансии нет. Мы сообщим вам, как только откроется место!")
#     await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
#                                         message_id=callback_query.message.message_id,
#                                         reply_markup=None)
