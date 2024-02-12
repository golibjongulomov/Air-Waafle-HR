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

@dp.message_handler(text="❌Bekor qilish", state="*")
async def lokatsiya_oluvchi(message: types.Message, state: FSMContext):
    await message.answer(f"Bo\'limni tanlang:", reply_markup=Bosh_menyu_tugmalari)
    await Bosh_menyu_state.Bosh.set()

@dp.message_handler(state=Vakansiyalar_state.Lokatsiya_tanlash)
async def lokatsiya_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Bo\'limni tanlang:", reply_markup=Bosh_menyu_tugmalari)
        await Bosh_menyu_state.Bosh.set() 
    else:  
        from handlers.funksiyalar import send_user_location
        user_id = message.from_user.id
        chat_id = message.chat.id
        if message.text == f"📍Magic City":
            latitude = 41.303148198871305  
            longitude = 69.2454436138731 
            await send_user_location(user_id, latitude, longitude)
            # await bot.send_photo(chat_id=message.chat.id, photo=photo_file_id, caption='Filial haqida')
            await message.answer(f"Qaysi lavozimda ishlamoqchisiz?", reply_markup=Lavozim_tanlash_tugmalari_m1_s1)
            await Vakansiyalar_state.Ish_orni_olish.set()
        elif message.text == f"📍Seoul Mun":
            latitude = 41.29910224041661
            longitude = 69.24690418546267
            await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Qaysi lavozimda ishlamoqchisiz?", reply_markup=Lavozim_tanlash_tugmalari_m1_s1)
            await Vakansiyalar_state.Ish_orni_olish.set()
        elif message.text == f"📍Milliy Bog\'": 
            latitude = 41.30293396835559 
            longitude = 69.24080897938212
            await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Qaysi lavozimda ishlamoqchisiz?", reply_markup=Lavozim_tanlash_tugmalari)
            await Vakansiyalar_state.Ish_orni_olish.set()
        elif message.text == f"📍Broadway":
            latitude = 41.31136501782332 
            longitude = 69.2739697119936 
            await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Qaysi lavozimda ishlamoqchisiz?", reply_markup=Lavozim_tanlash_tugmalari)
            await Vakansiyalar_state.Ish_orni_olish.set()
        elif message.text == f"📍Central Park":
            # latitude = 41.303148198871305  
            # longitude = 69.2454436138731 
            # await send_user_location(user_id, latitude, longitude)
            await message.answer(f"Qaysi lavozimda ishlamoqchisiz?", reply_markup=Lavozim_tanlash_tugmalari)
            await Vakansiyalar_state.Ish_orni_olish.set()
        await state.update_data({"Filial":message.text})
    
@dp.message_handler(state=Vakansiyalar_state.Ish_orni_olish)
async def lavozim_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Filialni tanlang:", reply_markup=Lokatsiya_bolimi_tugmalari)
        await Vakansiyalar_state.Lokatsiya_tanlash.set()
    else:
        if message.text == f"Kassir":
            await message.answer(f"""Ariza beruvchiga qo'yiladigan asosiy talablar:
∙ Rus va O\'zbek tillarida erkin muloqot qila olish, Ingliz tilida o\'rta darajada muloqot qila olish;
∙ Aktiv bo'lish va xushmuomalalik;
∙ Ishda xayrixohlik va ijobiy munosabat;
∙ Mas'uliyat va halollik;
∙ Jamoada ishlash ko'nikmalari;
∙ Stressga chidamlilik;
∙ Kassa qurilmalari bilan ishlash ko'nikmalari;
∙ Kassir lavozimida kamida 3 oylik tajribaga ega bo\'lish.""")
            await message.answer(f"Jinsingizni tanlang:", reply_markup=Jinsni_tanlash_tugmalari)
            await Vakansiyalar_state.Jinsini_olish.set()
        elif message.text == f"Oshxona hodimi":
            await message.answer(f"""Ariza beruvchiga qo'yiladigan asosiy talablar:
∙ Aktiv bo'lish va xushmuomalalik;
∙ Ishda xayrixohlik va ijobiy munosabat;
∙ Mas'uliyat va halollik;
∙ Yuqori o'rganish tezligi;
∙ Jamoada ishlash ko'nikmalari;
∙ Stressga chidamlilik;
∙ Ish tajribasi shart emas – biz hamma narsani o'zimiz o'rgatamiz!

Asosiy vazifalar:
∙ Kompaniya texnologiyasi va standartlariga muvofiq ovqat tayyorlash;
∙ Kompaniya standartlariga muvofiq mehmonlarga xizmat ko'rsatish:
∙ buyurtmalarni qabul qilish uchun kassada ishlash;
∙ mehmonlarga buyurtmalar tarqatish;
∙ Ish joyida, oshxona hududida tozalikni saqlash;
∙ Kompaniyada qabul qilingan tashqi ko'rinish standartlariga rioya qilish;
∙ Ish joyida Mehnat muhofazasi va Xavfsizlik texnika qoidalariga rioya qilish;""")
            await message.answer(f"Jinsingizni tanlang:", reply_markup=Jinsni_tanlash_tugmalari)
            await Vakansiyalar_state.Jinsini_olish.set()    
        elif message.text == f"Raner":
            await message.answer(f"""Ariza beruvchiga qo'yiladigan asosiy talablar:
∙ Aktiv bo'lish va xushmuomalalik;
∙ Ishda xayrixohlik va ijobiy munosabat;
∙ Mas'uliyat va halollik;
∙ Stressga chidamlilik;

Asosiy vazifalar:
∙ Kompaniya standartlariga muvofiq mehmonlarga xizmat ko'rsatish:
∙ mehmonlarga xizmat ko'rsatish zalida ishlash;
∙ Ish joyida, restoran hududida tozalikni saqlash;
∙ Kompaniyada qabul qilingan tashqi ko'rinish standartlariga rioya qilish;
∙ Ish joyida Mehnat muhofazasi va Xavfsizlik texnika qoidalariga rioya qilish;""")
            await message.answer(f"Jinsingizni tanlang:", reply_markup=Jinsni_tanlash_tugmalari)
            await Vakansiyalar_state.Jinsini_olish.set()
        elif message.text == f"Texnik hodim":
            await message.answer(f"""Ariza beruvchiga qo'yiladigan asosiy talablar:
∙ Ishda xayrixohlik va ijobiy munosabat;
∙ Mas'uliyat va halollik;
∙ Stressga chidamlilik;

Asosiy vazifalar:
∙ Ish joyida, restoran hududida tozalikni saqlash;
∙ Idishlar tozaligini saqlash va tezlik bilan ishlatishga tayyorlash;
∙ Ish joyida Mehnat muhofazasi va Xavfsizlik texnika qoidalariga rioya qilish;""")
            await message.answer(f"Jinsingizni tanlang:", reply_markup=Jinsni_tanlash_tugmalari)
            await Vakansiyalar_state.Jinsini_olish.set()
        await state.update_data({"Lavozim":message.text})
    
@dp.message_handler(state=Vakansiyalar_state.Jinsini_olish)
async def jins_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Air waffle jamoasiga qo\'shiling!\nFilialni tanlang:", reply_markup=Lokatsiya_bolimi_tugmalari)
        await Vakansiyalar_state.Lokatsiya_tanlash.set()
    else:
        if message.text == f"Erkak":
            await message.answer(text=f"FIO kiriting: (Malasan: Ivan Ivanovich Ivanov)", reply_markup=bekor_ortga_tugmalari)
            await Vakansiyalar_state.FIO_olish.set()
        elif message.text == "Ayol":
            await message.answer(text=f"FIO kiriting: (Malasan: Ivan Ivanovich Ivanov)", reply_markup=bekor_ortga_tugmalari) 
            await Vakansiyalar_state.FIO_olish.set()
        await state.update_data({"Jinsi":message.text}) 
    
@dp.message_handler(state=Vakansiyalar_state.FIO_olish)
async def ism_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Jinsingizni tanlang:", reply_markup=Jinsni_tanlash_tugmalari)
        await Vakansiyalar_state.Jinsini_olish.set()
    else:
        from handlers.funksiyalar import filter_name
        input_name = message.text
        filtered_name = filter_name(input_name)

        if filtered_name:
            await state.update_data({"Ism":message.text})
            await message.answer(f"Tu\'ilgan sanangizni kiriting: (Masalan: 01.01.2000)", reply_markup=bekor_ortga_tugmalari)
            await Vakansiyalar_state.Tugilgan_sana_olish.set()
        else:
            await message.answer(f"Ism formati noto\'g\'ri, iltimos qaytadan kiriting:")

@dp.message_handler(state=Vakansiyalar_state.Tugilgan_sana_olish)
async def sana_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(text=f"FIO kiriting: (Malasan: Ivan Ivanovich Ivanov)", reply_markup=bekor_ortga_tugmalari)
        await Vakansiyalar_state.FIO_olish.set()
    else:
        from handlers.funksiyalar import filter_birthdate
        input_date = message.text
        filtered_birthdate = filter_birthdate(input_date)
        if filtered_birthdate:
            await state.update_data({"Tugilgan_sana":message.text})
            await message.answer("Yashash manzilingiz lokatsiyasini yuboring", reply_markup=lokatsiya_jonatish_tugmalari)
            await Vakansiyalar_state.Adres_olish.set()
        else:
            await message.answer(f"No'to\'g\'ri sana, Iltimos qaytadan kiriting:")

@dp.message_handler(content_types=types.ContentType.LOCATION, state=Vakansiyalar_state.Adres_olish)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await message.answer(f"Telefon raqamingizni yuboring:", reply_markup=raqam_jonatish_tugmalari)
    await state.update_data({"latitude":latitude, "longitude":longitude},)
    await Vakansiyalar_state.Telefon_olish.set()
    
@dp.message_handler(state=Vakansiyalar_state.Adres_olish)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Tu\'ilgan sanangizni kiriting: (Masalan: 01.01.2000)", reply_markup=bekor_ortga_tugmalari)
        await Vakansiyalar_state.Tugilgan_sana_olish.set()
    else:
        await message.answer(f"Iltimos. to\'g\'ri lokatsiya yuboring")

@dp.message_handler(content_types=types.ContentType.CONTACT, state=Vakansiyalar_state.Telefon_olish)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    contact = message.contact
    phone_number = contact.phone_number
    await state.update_data({"raqam":phone_number})
    await message.answer(f"Siz talabamisiz?", reply_markup=Ha_yoq_tugmalari)
    await Vakansiyalar_state.Studentlikni_sorash.set()
    
@dp.message_handler(state=Vakansiyalar_state.Telefon_olish)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer("Yashash manzilingiz lokatsiyasini yuboring", reply_markup=lokatsiya_jonatish_tugmalari)
        await Vakansiyalar_state.Adres_olish.set()
    else:
        from handlers.funksiyalar import filter_phone_number
        phone_number = message.text
        filtered_phone_number = filter_phone_number(phone_number)
        if filtered_phone_number:
            await state.update_data({"raqam":phone_number})
            await message.answer(f"Siz talabamisiz?", reply_markup=Ha_yoq_tugmalari)
            await Vakansiyalar_state.Studentlikni_sorash.set()
        else:
            print(f"Iltimos, to\'g\'ri formatda raqam yuboring:")

@dp.message_handler(state=Vakansiyalar_state.Studentlikni_sorash)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Telefon raqamingizni yuboring:", reply_markup=raqam_jonatish_tugmalari)
        await Vakansiyalar_state.Telefon_olish.set()
    elif message.text == f"✅Ha":
        await state.update_data({"Talabalik":"✅Ha"})
        await message.answer(f"Qaysi ta'lim shaklida o\'qiysiz?", reply_markup=Talim_shakli_tugmalari)
        await Vakansiyalar_state.Talim_shaklini_sorash.set()
    elif message.text == f"❌Yo\'q":
        await state.update_data({"Talabalik":message.text})
        await state.update_data({"Talim_shakli":message.text})
        await message.answer(f"Ma\'lumotingiz qanday?", reply_markup=Malumot_tugmalari)
        await Vakansiyalar_state.Malumotini_sorash.set()
    else: 
        await message.answer(f"Iltimos javoblardan birini yuboring:")
    
@dp.message_handler(state=Vakansiyalar_state.Malumotini_sorash)
async def malumot_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Siz talabamisiz?", reply_markup=Ha_yoq_tugmalari)
        await Vakansiyalar_state.Studentlikni_sorash.set()
    elif message.text == f"O\'rta":
        await state.update_data({"Malumoti":message.text})
        await message.answer(f"Rus tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ruskiy_sorash.set()
    elif message.text == f"O\'rta-maxsus":
        await state.update_data({"Malumoti":message.text})
        await message.answer(f"Rus tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ruskiy_sorash.set()
    elif message.text == f"Oliy":
        await state.update_data({"Malumoti":message.text})
        await message.answer(f"Rus tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ruskiy_sorash.set()
    else:
        message.answer(f"Iltimos, javoblardan birini yuboring:")


@dp.message_handler(state=Vakansiyalar_state.Talim_shaklini_sorash)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Siz talabamisiz?", reply_markup=Ha_yoq_tugmalari)
        await Vakansiyalar_state.Studentlikni_sorash.set()
    elif message.text == f"Kunduzgi":
        await state.update_data({"Talim_shakli":message.text})
        await message.answer(f"Rus tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ruskiy_sorash.set()
    elif message.text == f"Kechki":
        await state.update_data({"Talim_shakli":message.text})
        await message.answer(f"Rus tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ruskiy_sorash.set()
    elif message.text == f"Sirtqi":
        await state.update_data({"Talim_shakli":message.text})
        await message.answer(f"Rus tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ruskiy_sorash.set()
    else:
        await message.answer(f"Iltimos, javoblardan birini yuboring:")

@dp.message_handler(state=Vakansiyalar_state.Ruskiy_sorash)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Qaysi ta'lim shaklida o\'qiysiz?", reply_markup=Talim_shakli_tugmalari)
        await Vakansiyalar_state.Talim_shaklini_sorash.set()
    elif message.text == f"Boshlang\'ich":
        await state.update_data({"Rus_tili_darajasi":message.text})
        await message.answer(f"O'zbek tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ozbek_sorash.set()
    elif message.text == f"O\'rta":
        await state.update_data({"Rus_tili_darajasi":message.text})
        await message.answer(f"O'zbek tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ozbek_sorash.set()
    elif message.text == f"Erkin":
        await state.update_data({"Rus_tili_darajasi":message.text})
        await message.answer(f"O'zbek tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ozbek_sorash.set()
    else:
        await message.answer(f"Iltimos, javoblardan birini yuboring:")

@dp.message_handler(state=Vakansiyalar_state.Ozbek_sorash)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Rus tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ruskiy_sorash.set()
    elif message.text == f"Boshlang\'ich":
        await state.update_data({"Ozbek_tili_darajasi":message.text})
        await message.answer(f"Qancha maosh sizni qoniqtiradi?", reply_markup=Ish_haqi_tugmalari)
        await Vakansiyalar_state.Oylik_sorash.set()
    elif message.text == f"O\'rta":
        await state.update_data({"Ozbek_tili_darajasi":message.text})
        await message.answer(f"Qancha maosh sizni qoniqtiradi?", reply_markup=Ish_haqi_tugmalari)
        await Vakansiyalar_state.Oylik_sorash.set()
    elif message.text == f"Erkin":
        await state.update_data({"Ozbek_tili_darajasi":message.text})
        await message.answer(f"Qancha maosh sizni qoniqtiradi?", reply_markup=Ish_haqi_tugmalari)
        await Vakansiyalar_state.Oylik_sorash.set()
    else:
        await message.answer(f"Iltimos, javoblardan birini yuboring:")

@dp.message_handler(state=Vakansiyalar_state.Oylik_sorash)
async def adres_oluvchi(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"O'zbek tilini bilish darajangiz qanday?", reply_markup=Til_bilish_tugmalari)
        await Vakansiyalar_state.Ozbek_sorash.set()
    elif message.text == f"1,5-2 mln":
        await state.update_data({"Maosh":message.text})
        await message.answer(f"Iltimos, rasmingizni jo'nating (Selfi ham mumkin)", reply_markup=bekor_ortga_tugmalari)
        await Vakansiyalar_state.Rasm_sorash.set()
    elif message.text == f"2-3 mln":
        await state.update_data({"Maosh":message.text})
        await message.answer(f"Iltimos, rasmingizni jo'nating (Selfi ham mumkin)", reply_markup=bekor_ortga_tugmalari)
        await Vakansiyalar_state.Rasm_sorash.set()
    elif message.text == f"3-4 mln":
        await state.update_data({"Maosh":message.text})
        await message.answer(f"Iltimos, rasmingizni jo'nating (Selfi ham mumkin)", reply_markup=bekor_ortga_tugmalari)
        await Vakansiyalar_state.Rasm_sorash.set()
    elif message.text == f"5 mln +":
        await state.update_data({"Maosh":message.text})
        await message.answer(f"Iltimos, rasmingizni yuboring (Selfi ham mumkin)", reply_markup=bekor_ortga_tugmalari)
        await Vakansiyalar_state.Rasm_sorash.set()
    else:
        message.answer(f"Iltimos, javoblarda birini yuboring")
    
@dp.message_handler(content_types=types.ContentType.PHOTO, state=Vakansiyalar_state.Rasm_sorash)
async def rasm_oluvchi(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    print(photo_file_id)
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
    caption = f"""Filial: {filial}\nLavozim: {lavozim}\nJinsi: {jins}\nFIO: {ism}\nTug\'ilgan sana: {tugilgan_sana}\nTelefon: {telefon}\nTalabami: {talaba}\nTalim shakli: {talim_shakli}\nMa\'lumoti: {malumoti}\nRus tili: {rus_tili}\nO'zbek tili: {ozbek_tili}\nMaosh: {maosh}"""
    await bot.send_photo(user_id, photo=photo_file_id, caption=caption)
    await message.answer(f"Ma\'lumotlaringiz qayta ishlanishiga rozimisiz?", reply_markup=Rozilik_tugmalari)
    await Vakansiyalar_state.Ruxsat_sorash.set()

@dp.message_handler(state=Vakansiyalar_state.Rasm_sorash)
async def rasm_oluvchi_rasm_emas(message: types.Message, state: FSMContext):
    if message.text == f"↩️Ortga":
        await message.answer(f"Qancha maosh sizni qoniqtiradi?", reply_markup=Ish_haqi_tugmalari)
        await Vakansiyalar_state.Oylik_sorash.set()
    else:
        await message.answer(f"Iltimos, rasmingizni yuboring!")

@dp.message_handler(state=Vakansiyalar_state.Ruxsat_sorash)
async def ruxsat_oluvchi_funksiya(message: types.Message, state: FSMContext):
    if message.text == f"✅Rezumeni yuborish":
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
        caption = f"Filial: {filial}\nLavozim: {lavozim}\nJinsi: {jins}\nFIO: {ism}\nTug\'ilgan sana: {tugilgan_sana}\nTelefon: {telefon}\nTalaba: {talaba}\nTalim shakli: {talim_shakli}\nMa\'lumoti: {malumoti}\nRus tili: {rus_tili}\nO'zbek tili: {ozbek_tili}\nMaosh: {maosh}"
        
        inline_tugmalar_markup = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton(text=f"Vakansiya yo\'q", callback_data=message.from_user.id)
        inline_tugmalar_markup.add(button)
        
        await bot.send_location(5030191796, latitude=latitude, longitude=longitude)
        await bot.send_photo(5030191796, photo=photo_id, caption=caption, reply_markup=inline_tugmalar_markup)
        await bot.send_location(6589557772, latitude=latitude, longitude=longitude)
        await bot.send_photo(6589557772, photo=photo_id, caption=caption, reply_markup=None)
        await message.answer(f"Rezume yuborildi, tez orada siz bilan bog\'lanamiz.", reply_markup=Bosh_menyu_tugmalari)
        await Bosh_menyu_state.Bosh.set()
        

@dp.callback_query_handler(state="*")
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print("callback ishladi")
    til = data.get("til")
    await bot.answer_callback_query(callback_query.id, text=f"Xabar yuborildi")
    await bot.send_message(callback_query.data, f"\tAir Waffle jamoasi a\'zosiga aylanish istagini bildirganingiz uchun tashakkur.\nKechirasiz, hozirda ushbu vakansiyada bo\'sh joylar mavjud emas. Joylar ochilishi bilan sizga xabar beramiz! \n \tБлагодарим вас за интерес к тому, чтобы стать членом команды Air Waffle. К сожалению, на данный момент вакансий по данной вакансии нет. Мы сообщим вам, как только откроется место!")
    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=None)
