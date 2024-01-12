from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.vue_js import vue_js
vue_js_menu_router: Router = Router()

@vue_js_menu_router.message(F.text == "Vue JS darslari")
async def vue(message: Message):
    await message.answer("Vue JS darslari",reply_markup=vue_js)



# 1-2 darslar
@vue_js_menu_router.message(F.text == "1-2 dars (vue js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGDGV7rmBp1qdLqJMbYEUrXjDtPWx3AAIREwACg9BQS33Pf1QXrjHJMwQ",caption="""
    Vue JS darslari | 1-dars | Kirish
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGDWV7rmDkUFNZZIWPLW_O8uZLBlJGAAISEwACg9BQS2qHlirtr-YTMwQ",caption="""
    Vue JS darslari | 2-dars | Vue JS nima, Terminalda ishlash, CLI 
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    


# 3-4 darslar
@vue_js_menu_router.message(F.text == "3-4 dars (vue js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGEGV7rtaAuZbHmyM2KldLjyuob8VOAAITEwACg9BQS2WwJE99Jt6WMwQ",caption="""
    Vue JS darslari | 3-dars | Vue JS metod bilan ishlash, Interpolatsiya
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGEWV7rtaIzaD8q2Fg8bNNhzEuYhB1AAIUEwACg9BQSyX0wumsJ5tkMwQ",caption="""
    Vue JS darslari | 4-dars | Vue JS formalar bilan ishlash, xodisalar
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    


# 5-6 darslar
@vue_js_menu_router.message(F.text == "5-6 dars (vue js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGGmV7r0GSEHDIXi26oGgJsE6ewcagAAIWEwACg9BQS-E-s4cMlARtMwQ",caption="""
    Vue JS darslari | 5-dars | Vue JS Props va $emit nima, ular bilan ishlash
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGG2V7r0Gk2pZP31zlnKxSI_o95jrvAAIbEwACg9BQS-hYxmUEM7O5MwQ",caption="""
    Vue JS darslari | 6-dars | Vue JS UI Kutubxona yasaymiz
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    


# 7-8 darslar
@vue_js_menu_router.message(F.text == "7-8 dars (vue js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGHmV7r5Tkm7S8gRQyJ9E3BC5q6XdUAAIhEwACg9BQS3A7T5VJMLDhMwQ",caption="""
    Vue JS darslari | 7-dars | Vue JS Modal oynasi
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGH2V7r5T0oAa6W8vOmYdodHw4GOFrAAIiEwACg9BQSxmrMKAPXfFxMwQ",caption="""
    Vue JS darslari | 8-dars | Vue JS Server bilan ishlash, lifescyle method
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 9-10 darslar
@vue_js_menu_router.message(F.text == "9-10 dars (vue js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGImV7r90kd6n-gSI6qSwJvINp5jwAAyMTAAKD0FBL2E1uL1L5m_wzBA",caption="""
    Vue JS darslari | 9-dars | Vue JS filterlash category bo'yicha 
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGI2V7r91y4jUkfmbqbDsG2PaJkUP0AAIlEwACg9BQS2_Bia5AXmVnMwQ",caption="""
    Vue JS darslari | 10-dars | Vue JS kontent category bo'yicha o'zgartirish
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 11-12 darslar
@vue_js_menu_router.message(F.text == "11-12 dars (vue js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGJmV7sDKpXqaLmWhy0UPLCDkFRbx9AAImEwACg9BQS0Hr0XmP9yUHMwQ",caption="""
    Vue JS darslari | 11-dars | Vue JS Pagination va Animatsiya
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGJ2V7sDKIopJ-FGxwWbblTISRWk9lAAInEwACg9BQS-TC0vG7vqpvMwQ",caption="""
    Vue JS darslari | 12-dars | Vue JS Navigatsiya bilan ishlash
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 13-14 darslar
@vue_js_menu_router.message(F.text == "13-14 dars (vue js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGKmV7sJHSwuda6MCMKzpRPaawXooBAAIoEwACg9BQS2m3W9DlMv3zMwQ",caption="""
    Vue JS darslari | 13-dars | Vue JS praktika 
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGK2V7sJEcdIKZSXB3a2k28yHqLR1uAAIqEwACg9BQS8qaJIkdGuHQMwQ",caption="""
    Vue JS darslari | 14-dars | Vue JS project
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    
    

# 15-16 darslar
@vue_js_menu_router.message(F.text == "15-16 dars (vue js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGLmV7sOOwXyhBz_JKw9cG50YhdT4pAAIuEwACg9BQS3m7kGWxkMWmMwQ",caption="""
    Vue JS darslari | 15-dars | Vue JS Amaliyot Weather App
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGL2V7sONmiHl1KiCCRjas1J5hqU9yAAIvEwACg9BQS637lGgPEUrwMwQ",caption="""
    Vue JS darslari | 16-dars | Vue JS amaliyot progress bar
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
   