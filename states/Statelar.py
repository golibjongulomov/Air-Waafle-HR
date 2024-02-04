from aiogram.dispatcher.filters.state import State, StatesGroup

class Bosh_menyu_state(StatesGroup):
    Bosh = State()
    Tilni_tanlash = State()

class Bosh_menyu_state_ru(StatesGroup):
    Bosh_ru = State()
    Tilni_tanlash_ru = State()


class Vakansiyalar_state(StatesGroup):
    Lokatsiya_tanlash = State()     #bajarildi
    Ish_orni_olish = State()        #bajarildi
    Jinsini_olish = State()         #bajarildi
    FIO_olish = State()             #bajarildi
    Tugilgan_sana_olish = State()   #bajarildi
    Adres_olish = State()           #bajarildi
    Telefon_olish = State()         #bajarildi   
    Studentlikni_sorash = State()   #bajarildi
    Talim_shaklini_sorash = State() #bajarildi
    Malumotini_sorash = State()  #bajarildi
    Ruskiy_sorash = State() #bajarildi
    Ozbek_sorash = State() #bajarildi
    Oylik_sorash = State() #bajarildi
    Rasm_sorash = State() 
    Qayerdan_topganini_sorash = State()
    Ruxsat_sorash = State()


class Vakansiyalar_state_ru(StatesGroup):
    Lokatsiya_tanlash_ru = State()     #bajarildi
    Ish_orni_olish_ru = State()        #bajarildi
    Jinsini_olish_ru = State()         #bajarildi
    FIO_olish_ru = State()             #bajarildi
    Tugilgan_sana_olish_ru = State()   #bajarildi
    Adres_olish_ru = State()           #bajarildi
    Telefon_olish_ru = State()         #bajarildi   
    Studentlikni_sorash_ru = State()   #bajarildi
    Talim_shaklini_sorash_ru = State() #bajarildi
    Malumotini_sorash_ru = State()  #bajarildi
    Ruskiy_sorash_ru = State() #bajarildi
    Ozbek_sorash_ru = State() #bajarildi
    Oylik_sorash_ru = State() #bajarildi
    Rasm_sorash_ru = State() 
    Qayerdan_topganini_sorash_ru = State()
    Ruxsat_sorash_ru = State()

    