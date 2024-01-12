from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.beckend_keyboard import start_menu

beckend_menu_router: Router = Router()


@beckend_menu_router.message(F.text=="Back-End")
async def start_menu_handler(message: Message):
    await message.answer("Ozingizga ma'qul darslarni tanglang",reply_markup=start_menu)


@beckend_menu_router.message(F.text == "Orqaga")
async def beckend(message: Message):
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
    await message.answer("Ozingizga ma'qul bo'lgan yonalishni tanlang tanglang 😊",reply_markup=menu_front)