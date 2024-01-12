from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


php_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-2 dars (php)"),
            KeyboardButton(text="3-4 dars (php)"),
        ],
        [
            KeyboardButton(text="5-6 dars (php)"),
            KeyboardButton(text="7-8 dars (php)"),
        ],
        [
            KeyboardButton(text="9-10 dars (php)"),
            KeyboardButton(text="11-12 dars (php)"),
        ],
        [
            KeyboardButton(text="13-14 dars (php)"),
            KeyboardButton(text="15-16 dars (php)"),
        ],
        [
            KeyboardButton(text="17-18 dars (php)"),
            KeyboardButton(text="19-20 dars (php)"),
        ],
        [
            KeyboardButton(text="21-22 dars (php)"),
            KeyboardButton(text="23-24 dars (php)"),
        ],
        [
            KeyboardButton(text="25-26 dars (php)"),
            KeyboardButton(text="27-28 dars (php)"),
        ],
        [
            KeyboardButton(text="29-30 dars (php)"),
            KeyboardButton(text="31 dars (php)"),
        ],
        [
            KeyboardButton(text="Orqaga."),
            KeyboardButton(text="🔝 Asosiy Menyu"),
        ],
    ],
    resize_keyboard=True
)