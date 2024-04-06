from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Bosh_menyu_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Biz haqimizda"),
        ],
        [
            KeyboardButton(text="🖋Vakansiyalar"),
        ],
        [
            KeyboardButton(text="🇷🇺/🇺🇿Tilni tanlash")
        ],
    ],
        
    resize_keyboard=True
)

Til_tanlash_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🇷🇺Русский"),
        ],
    ],
        
    resize_keyboard=True
)

Lokatsiya_bolimi_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text=f"📍Magic City"),
        KeyboardButton(text=f"📍Milliy Bog\'"),
        ],
        [
            KeyboardButton(text=f"📍Seoul Mun"),
            KeyboardButton(text=f"📍Broadway")
        ],
        [
            KeyboardButton(text=f"📍Central Park"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish")
        ],
    ],
        
    resize_keyboard=True
)

Lavozim_tanlash_tugmalari_m1_s1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Kassir"),
        ],
        [
            KeyboardButton(text=f"Oshxona hodimi"),
        ],
        [
            KeyboardButton(text=f"Barista"),
        ],
        [
            KeyboardButton(text=f"Raner"),
        ],
        [
            KeyboardButton(text=f"Texnik hodim"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
        
    resize_keyboard=True
)

Lavozim_tanlash_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Oshxona hodimi"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
        
    resize_keyboard=True
)

Jinsni_tanlash_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Erkak"),
            KeyboardButton(text=f"Ayol"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
        
    resize_keyboard=True
)

bekor_ortga_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
        
    resize_keyboard=True
)

lokatsiya_jonatish_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"📍Lokatsiya yuborish", request_location=True)
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
        
    resize_keyboard=True
)

raqam_jonatish_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Raqam yuborish", request_contact=True)
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
        
    resize_keyboard=True
)

Ha_yoq_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"✅Ha"),
            KeyboardButton(text=f"❌Yo\'q"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
        
    resize_keyboard=True
)

Talim_shakli_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Kunduzgi"),
        ],
        [
            KeyboardButton(text=f"Kechki"),
        ],
        [
            KeyboardButton(text=f"Sirtqi"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
        
    resize_keyboard=True
)

Til_bilish_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Boshlang\'ich"),
        ],
        [
            KeyboardButton(text=f"O\'rta"),
        ],
        [
            KeyboardButton(text=f"Erkin")
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
    resize_keyboard=True
)

Malumot_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"O\'rta"),
        ],
        [
            KeyboardButton(text=f"O\'rta-maxsus"),
        ],
        [
            KeyboardButton(text=f"Oliy")
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
    resize_keyboard=True
)


Ish_haqi_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"1,5-2 mln"),
            KeyboardButton(text=f"2-3 mln"),
        ],
        [
            KeyboardButton(text=f"3-4 mln"),
            KeyboardButton(text=f"5 mln +"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
    resize_keyboard=True
)
Rozilik_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"✅Rezumeni yuborish"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
    resize_keyboard=True
)

Jonatish_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text=f"Jo\'natish"),
        ],
        [
            KeyboardButton(text=f"❌Bekor qilish"),
            KeyboardButton(text=f"↩️Ortga"),
        ],
    ],
    resize_keyboard=True
)



"""--------------------------------------------------------------------------------------------------------------------"""





Bosh_menyu_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="О нас"),
        ],
        [
            KeyboardButton(text="🖋Вакансии"),
        ],
        [
            KeyboardButton(text="🇷🇺/🇺🇿Выбор языка"),
        ],
    ],
        
    resize_keyboard=True
)

Til_tanlash_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🇺🇿O\'zbekcha"),
        ],
    ],
        
    resize_keyboard=True
)

Lokatsiya_bolimi_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text=f"📍Magic City"),
        KeyboardButton(text=f"📍Национальный парк"),
        ],
        [
            KeyboardButton(text=f"📍Seoul Mun"),
            KeyboardButton(text=f"📍Broadway")
        ],
        [
            KeyboardButton(text=f"📍Центральный парк"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

Lavozim_tanlash_tugmalari_m1_s1_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Кассир"),
        ],
        [
            KeyboardButton(text=f"Рабочий кухни"),
        ],
        [
            KeyboardButton(text=f"Ранер"),
        ],
        [
            KeyboardButton(text=f"Техничка"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

Lavozim_tanlash_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Рабочий кухни"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

Jinsni_tanlash_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Мужчина"),
            KeyboardButton(text=f"Женщина"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

bekor_ortga_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

lokatsiya_jonatish_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"📍Отправить местоположение", request_location=True)
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

raqam_jonatish_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Отправить номер", request_contact=True)
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

Ha_yoq_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"✅Да"),
            KeyboardButton(text=f"❌Нет"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

Talim_shakli_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Очное"),
        ],
        [
            KeyboardButton(text=f"Вечернее"),
        ],
        [
            KeyboardButton(text=f"Заочное"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
        
    resize_keyboard=True
)

Til_bilish_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Начальный"),
        ],
        [
            KeyboardButton(text=f"Средний"),
        ],
        [
            KeyboardButton(text=f"Свободный")
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
    resize_keyboard=True
)

Malumot_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Среднее"),
        ],
        [
            KeyboardButton(text=f"Средне-специальное"),
        ],
        [
            KeyboardButton(text=f"Высшее")
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
    resize_keyboard=True
)


Ish_haqi_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"1,5-2 млн"),
            KeyboardButton(text=f"2-3 млн"),
        ],
        [
            KeyboardButton(text=f"3-4 млн"),
            KeyboardButton(text=f"5 млн +"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
    resize_keyboard=True
)
Rozilik_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"✅Подтверждать отправки"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
    resize_keyboard=True
)

Jonatish_tugmalari_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text=f"Jo\'natish"),
        ],
        [
            KeyboardButton(text=f"❌Отмена"),
            KeyboardButton(text=f"↩️Назад"),
        ],
    ],
    resize_keyboard=True
)




