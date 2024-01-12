from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command


FronorBeck_menu_router: Router = Router()

@FronorBeck_menu_router.message(F.text=="Darslarni boshlash 💻")
async def FrontOrBeck(message: Message):

    menu_front = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Front-End"),
                KeyboardButton(text="Back-End"),
            ],
            [
                KeyboardButton(text="Kerakli dasturlar"),
            ],
            [
                KeyboardButton(text="Orqaga qaytish"),
            ],
        ],
        resize_keyboard=True
    )
    await message.answer("Ozingizga ma'qul bo'lgan yonalishni tanlang tanglang 😊", reply_markup=menu_front)


@FronorBeck_menu_router.message(F.text == "Kerakli dasturlar")
async def kerakli_dastur(message: Message):
    await message.answer_document("BQACAgIAAxkBAAIDLmV5CdV72YcKGKy050tjxJ6AJzZTAAJwNwACsKbJSyD86lvblwmMMwQ",caption="Marxamat dasturni yuklab oling 😊")


@FronorBeck_menu_router.message(F.text=="Orqaga qaytish")
async def orqaga_handler(message: Message):
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Darslarni boshlash 💻")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(f"""Assalomu aleykum 
        \nYangicha formatdagi platformaga xush kelibsiz! Tartiblangan va yangi darslar sizni kutmoqda. Quyidagi tugmani bosing👇
            
    """, reply_markup=menu)
