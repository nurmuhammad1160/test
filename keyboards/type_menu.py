from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


type_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-2 dars (type script)"),
            KeyboardButton(text="3-4 dars (type script)")
        ],
        [
            KeyboardButton(text="5-6 dars (type script)"),
            KeyboardButton(text="7-8 dars (type script)")
        ],
        [
            KeyboardButton(text="9-10 dars (type script)"),
            KeyboardButton(text="11-12 dars (type script)")
        ],
        [
            KeyboardButton(text="13-14 dars (type script)"),
            KeyboardButton(text="15-16 dars (type script)")
        ],
        [
            KeyboardButton(text="17-18 dars (type script)"),
            KeyboardButton(text="19-20 dars (type script)")
        ],
        [
            KeyboardButton(text="21-22 dars (type script)"),
            
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu"),
        ],
    ],
    resize_keyboard=True
)