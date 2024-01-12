
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


start_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Node JS darslari"),
                KeyboardButton(text="Java darslari"),
            ],
            [
                KeyboardButton(text="Python darslari"),
                KeyboardButton(text="PHP darslari"),
            ],
            [
                KeyboardButton(text="C++ darslari"),
                KeyboardButton(text="C# darslari"),
            ],
            [
                KeyboardButton(text="Go darslari"),
                KeyboardButton(text="PHP (Yii2 framework)"),
            ],
            [
                KeyboardButton(text="Python (Django framework)"),
            ],
            [
                KeyboardButton(text="Orqaga"),
                KeyboardButton(text="🔝 Asosiy Menyu"),
            ],
        ],
        resize_keyboard=True
    )