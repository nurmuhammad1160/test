from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


react_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-2 dars (react)"),
            KeyboardButton(text="3-4 dars (react)"),
        ],
        [
            KeyboardButton(text="5-6 dars (react)"),
            KeyboardButton(text="7-8 dars (react)"),
        ],
        [
            KeyboardButton(text="9-10 dars (react)"),
            KeyboardButton(text="11-12 dars (react)"),
        ],
        [
            KeyboardButton(text="13 dars (react)"),
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu"),
        ],
    ]
)