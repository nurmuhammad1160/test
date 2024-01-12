from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


bootstrap_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-2 dars (bootstrap)"),
            KeyboardButton(text="3-4 dars (bootstrap)"),
        ],
        [
            KeyboardButton(text="5-6 dars (bootstrap)"),
            KeyboardButton(text="7-8 dars (bootstrap)"),
        ],
        [
            KeyboardButton(text="9-10 dars (bootstrap)"),
            KeyboardButton(text="11-12 dars (bootstrap)"),
        ],
        [
            KeyboardButton(text="13-14 dars (bootstrap)"),
            KeyboardButton(text="15-16 dars (bootstrap)"),
        ],
        [
            KeyboardButton(text="17-18 dars (bootstrap)"),
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu"),
        ],
    ],
    resize_keyboard=True
)