from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

vue_js = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-2 dars (vue js)"),
            KeyboardButton(text="3-4 dars (vue js)")
        ],
        [
            KeyboardButton(text="5-6 dars (vue js)"),
            KeyboardButton(text="7-8 dars (vue js)")
        ],
        [
            KeyboardButton(text="9-10 dars (vue js)"),
            KeyboardButton(text="11-12 dars (vue js)")
        ],
        [
            KeyboardButton(text="13-14 dars (vue js)"),
            KeyboardButton(text="15-16 dars (vue js)")
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu"),
        ],
    ],
    resize_keyboard=True
)