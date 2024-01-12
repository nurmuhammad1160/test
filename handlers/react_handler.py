from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.react_menu import react_menu
react_menu_router: Router = Router()

@react_menu_router.message(F.text == "React JS darslar")
async def react_handler(message: Message):
    await message.answer("React JS darslar",reply_markup=react_menu)



# 1-2 darslar
@react_menu_router.message(F.text == "1-2 dars (react)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIFyWV7pRN8vt86tsO1dlfg2T76rvLQAAIFEwACBeM5SERcJID2JoUoMwQ",caption="""
    React Js darslari | 1-dars | React nima
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIFymV7pRPC0aA0RYPG9sil0Nao0ERhAAIGEwACBeM5SNDhLc9snnhoMwQ",caption="""
    React Js darslari | 2-dars | renderDom haqida
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 3-4 darslar
@react_menu_router.message(F.text == "3-4 dars (react)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIF0mV7qQvRENWiLe8VaPIJPBIgs5sOAAIIEwACBeM5SO0Mv7P1gSSlMwQ",caption="""
    React Js darslari | 3-dars | react JSX nima
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIF02V7qQsVN8VRUPxD_a_DOgABULa_FQACChMAAgXjOUgU-GTuD1QluzME",caption="""
    React Js darslari | 4-dars | react components
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 5-6 darslar
@react_menu_router.message(F.text == "5-6 dars (react)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIF1mV7qVmQJeVHR0qlQ-9PsDhc8la9AAILEwACBeM5SPDxJGaKuKf9MwQ",caption="""
    React Js darslari | 5-dars | State
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIF12V7qVnjGCfk33JvLfBNnbe2xI-LAAINEwACBeM5SCU2u46aSuSNMwQ",caption="""
    React Js darslari | 6-dars | Lifecycle
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 7-8 darslar
@react_menu_router.message(F.text == "7-8 dars (react)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIF2mV7qZ9EyqcZwWmNwFNQV5GqHwHrAAIPEwACBeM5SA_m8iPKTKDRMwQ",caption="""
    React Js darslari | 7-dars | Form va event boshqaruvi
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIF22V7qZ86Yb7kDceMbRVhUMKrowjPAAIREwACBeM5SIfzcsRZqCm5MwQ",caption="""
    React Js darslari | 8-dars | Conditional Rendering
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 9-10 darslar
@react_menu_router.message(F.text == "9-10 dars (react)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIF3mV7qe20Kx10QQQ99z3pkkbD1shQAAISEwACBeM5SKrA-UjqptLJMwQ",caption="""
    React Js darslari | 9-dars | Router haqida
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIF32V7qe1e5lbA5tV0QGXU1XqPHuZmAAITEwACBeM5SLH2BU_2xYUDMwQ",caption="""
    React Js darslari | 10-dars | Fetch get
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 11-12 darslar
@react_menu_router.message(F.text == "11-12 dars (react)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIF4mV7qjjXUgHVT9QnY7QgQym4wTiqAAIVEwACBeM5SBeHu-0n1yiwMwQ",caption="""
    React Js darslari | 11-dars | Fetch post
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIF42V7qjh2XJsEMl2CIIv5hq9ly-JJAAIWEwACBeM5SB1zeWEiX4CzMwQ",caption="""
    React Js darslari | 12-dars | Axios Get Post
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 13 darslar
@react_menu_router.message(F.text == "13 dars (react)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIF-GV7qr6mxh3E-HSl5AO_qtxgvHm3AAIdEwACBeM5SAFc8Gq4jzj0MwQ",caption="""
    React Js darslari | 13-dars | Style
\nYoutube —  www.youtube.com/c/Alitechacademy  \nTelegram —   @alitechuz
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")