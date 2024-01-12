from aiogram import Router, F
from aiogram.types import Message,CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.majburiy import majburiy_obuna, menu
from aiogram.methods.get_chat_member import GetChatMember
from loader import bot
start_router: Router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"""Assalomu aleykum 
    \nYangicha formatdagi platformaga xush kelibsiz! Tartiblangan va yangi darslar sizni kutmoqda. Quyidagi tugmani bosing👇
        
""")
    await message.answer("Bottan foydalanish uchun kanalga qo'shiling!", reply_markup=majburiy_obuna)


@start_router.callback_query(F.data == "tasdiqlash")
async def check(query: CallbackQuery):
    user = await GetChatMember(chat_id='-1002052838409',user_id=query.from_user.id)

    
    if user.status == 'admin':
        await bot.send_message(chat_id=query.from_user.id,text="Darslarni boshlang 😊", reply_marku=menu)
    elif user.status == 'creator':
  
        await bot.send_message(chat_id=query.from_user.id,text="Darslarni boshlang 😊", reply_markup=menu)
    elif user.status == 'member':
    
        await bot.send_message(chat_id=query.from_user.id,text="Darslarni boshlang 😊", reply_markup=menu)
    else:
        await bot.send_message(chat_id=query.from_user.id,text="Kechirasiz siz kanalga azo bo'lmagansiz!", reply_markup=majburiy_obuna)

