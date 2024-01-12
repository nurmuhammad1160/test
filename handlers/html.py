from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command


html_menu_router: Router = Router()

@html_menu_router.message(F.text=="HTML darslari")
async def html_handler(message: Message):
    html = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="1-2 dars (HTML)"),
                KeyboardButton(text="3-4 dars (HTML)"),
            ],
            [
                KeyboardButton(text="5-6 dars (HTML)"),
                KeyboardButton(text="7-8 dars (HTML)"),
            ],
            [
                KeyboardButton(text="9-10 dars (HTML)"),
                KeyboardButton(text="11 dars (HTML)"),
            ],
         
            [
                KeyboardButton(text="Orqaga 🔙"),
                KeyboardButton(text="🔝 Asosiy Menyu"),
            ],
        ],
        resize_keyboard=True
    )

    await message.answer("HTML darslari", reply_markup=html)



# 1-2 dars
@html_menu_router.message(F.text=="1-2 dars (HTML)")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBrmVpN3UQXYRtlQnWx-BwlKvFiCHBAALHEAAC2v8JSAs4ovaUgrDlMwQ', caption="""
    HTML darslari | 1-dars | Asosiy tushunchalar

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)
    await message.answer_video("BAACAgIAAxkBAAIBr2VpN3VJCQYuK2Gvo3v9zTZ1lJalAALIEAAC2v8JSC3nYPyDlq-mMwQ", caption="""
    HTML darslari | 2-dars | Tuzulmasi 

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)


# 3-4 dars
@html_menu_router.message(F.text=="3-4 dars (HTML)")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIB2WVpYeY7rxJpeuA2wJZPiL6P1hgMAALJEAAC2v8JSJg8MBio5mM1MwQ', caption="""
    HTML darslari | 3-dars | Head, body haqida

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)
    await message.answer_video("BAACAgIAAxkBAAIB2mVpYeZSplZxP_LvMkX7C1_UsT5uAALKEAAC2v8JSPM_x-7ThSZuMwQ", caption="""
    HTML darslari | 4-dars | Dasturlashni boshladik

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)


# 5-6 dars
@html_menu_router.message(F.text=="5-6 dars (HTML)")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIB3WVpYlFxeu-QUYtdHfR_4MzNLhwgAALLEAAC2v8JSH4dUewLgSDpMwQ', caption="""
    HTML darslari | 5-dars | Taglar haqida

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)
    await message.answer_video("BAACAgIAAxkBAAIB3mVpYlGyfZI-vv4djqPvHCEAAfHGCgACzRAAAtr_CUhmcCqzsIS3QzME", caption="""
    HTML darslari | 6-dars | li teglari haqida

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

# 7-8 dars
@html_menu_router.message(F.text=="7-8 dars (HTML)")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIB4WVpYss5Ajsh7mw5M2smRtOGGw2QAALSEAAC2v8JSA99xjKUbs51MwQ', caption="""
    HTML darslari | 7-dars | Formlar haqida

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)
    await message.answer_video("BAACAgIAAxkBAAIB4mVpYst9AAEXzbOr4BG3BHuQXMf-wwAC0xAAAtr_CUibVsm0eLDLITME", caption="""
    HTML darslari | 8-dars | Foydali ma'lumotlar

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)



# 9-10 dars
@html_menu_router.message(F.text=="9-10 dars (HTML)")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIB5WVpY03cTYII_W5ur1mO2qBHdWP_AALYEAAC2v8JSA6qsDM6NTqMMwQ', caption="""
    HTML darslari | 9-dars | Form workshop

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)
    await message.answer_video("BAACAgIAAxkBAAIB5mVpY00WnDRXwcRZGgnO267AfCasAALaEAAC2v8JSHD0vd_8LA8TMwQ", caption="""
    HTML darslari | 10-dars | Media elementlari

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

# 11 dars
@html_menu_router.message(F.text=="11 dars (HTML)")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIB6WVpZGoULf_G5VXunS1UOhUNMgyaAALcEAAC2v8JSDjeX-jQE3KJMwQ', caption="""
    HTML darslari | 11-dars | HTML da rasm xarita tuzish

    \nYoutube — www.youtube.com/c/Alitechacademy
    \nTelegram — @alitechuz

    \n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

@html_menu_router.message(F.text=="Orqaga 🔙")
async def one_two(message: Message):
    start_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Frontend (intensiv)"),
                KeyboardButton(text="HTML darslari"),
            ],
            [
                KeyboardButton(text="CSS darslari"),
                KeyboardButton(text="Sass darslari"),
            ],
            [
                KeyboardButton(text="Bootstrap darslari"),
                KeyboardButton(text="JavaScript darslari"),
            ],
            [
                KeyboardButton(text="jQuery darslari"),
                KeyboardButton(text="React JS darslar"),
            ],
            [
                KeyboardButton(text="Vue JS darslari"),
                KeyboardButton(text="TypeScript darslari"),
            ],
            [
                KeyboardButton(text="🔙 Orqaga"),
                KeyboardButton(text="🔝 Asosiy Menyu"),
            ],
        ],
        resize_keyboard=True
    )

    await message.answer("Ozingizga ma'qul darslarni tanglang",reply_markup=start_menu)

