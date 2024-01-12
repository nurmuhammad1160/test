from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

get_id_router: Router = Router()

@get_id_router.message()
async def get_id(message: Message):
    try:
        file_id = message.video.file_id
        await message.reply(file_id)
    except:
        await message.answer("Kechirasiz hozircha bunday malumot yo'q!")