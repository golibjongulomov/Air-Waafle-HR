from datetime import datetime
def filter_birthdate(input_str):
    try:
        # Attempt to parse the input string as a date
        birthdate = datetime.strptime(input_str, "%d.%m.%Y").date()
    
        # Check if the parsed date is reasonable for a birthdate
        current_year = datetime.now().year
        if 1970 <= birthdate.year <= current_year and 1 <= birthdate.month <= 12 and 1 <= birthdate.day <= 31:
            return birthdate
        else:
                return None
    except ValueError:
                # If parsing fails, return None
            return None
    
import re
def filter_name(names):
    filtered_names = []

    for name in names:
        # Check if the name contains only English or Russian characters and the symbol '
        if re.match(r'^[A-Za-zА-Яа-я\']+$', name):
            filtered_names.append(name)

    return filtered_names


import re

def filter_phone_number(phone_number):
    # Regular expression for a basic phone number with country code
    pattern = re.compile(r'^\+?[0-9]+$')

    # Remove non-digit characters
    cleaned_number = re.sub(r'\D', '', phone_number)

    if pattern.match(cleaned_number):
        return cleaned_number
    else:
        return None
        

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from loader import dp, bot
async def send_user_location(chat_id, latitude, longitude):
    await bot.send_location(chat_id, latitude, longitude)
    
    


