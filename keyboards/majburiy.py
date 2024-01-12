from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


majburiy_obuna = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanaga qo'shilish",url='https://t.me/obunachi_yegish')
        ],
        [
            InlineKeyboardButton(text="Tasdiqlash ✅",callback_data="tasdiqlash")
        ]
    ]
)




menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Darslarni boshlash 💻")
        ]
    ],
    resize_keyboard=True
)
