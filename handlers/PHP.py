from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.nodejs_menu import nodejs_menu
from keyboards.PHP_menu import php_menu_keyboard

php_menu_router: Router = Router()


@php_menu_router.message(F.text == "PHP darslari")
async def python(message: Message):
    await message.answer("PHP darslari",reply_markup=php_menu_keyboard)




# 1-2 darslar
@php_menu_router.message(F.text == "1-2 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKqWWdbbF36cZ1JurP5qtVfX_KO-RjAAJIFAAC0UZ4SHeDU5uz_lILNAQ",caption="""
    PHP darslari | 1-dars | OpenServer yuklab olish                         
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKqmWdbbHcRHPUizPDGAeIZxMgsPfJAAJJFAAC0UZ4SHA3KjvNqr00NAQ",caption="""
    PHP darslari | 2-dars | PHP Sintaksisi va echo, print buyruqlari bilan ishlash                        
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 3-4 darslar
@php_menu_router.message(F.text == "3-4 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKsmWdblfCIMdfO_WcGaGpGMrtAAF4fwACShQAAtFGeEgWsYqyT1ScxDQE",caption="""
    PHP darslari | 3-dars | PHPda O'zgaruvchilar                         
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKs2Wdblfn5JL8VD6cAiet8-eFH3WMAAJLFAAC0UZ4SOVxyPNr4oShNAQ",caption="""
    PHP darslari | 4-dars | PHPda Arifmetik amallar                       
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 5-6 darslar
@php_menu_router.message(F.text == "5-6 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKtmWdbpWD60qVsNM23Nni_8rqdd6bAAJMFAAC0UZ4SGvajW4Ck2hzNAQ",caption="""
    PHP darslari | 5-dars | solishtirish operatorlari               
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKt2WdbpVPA4y7ew30-REDhWuxe06RAAJNFAAC0UZ4SGKaLqZCyKKaNAQ",caption="""
    PHP darslari | 6-dars | Shart operatorlari                      
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 7-8 darslar
@php_menu_router.message(F.text == "7-8 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKumWdbtl8y1Asv6HUuFM5jwHCUANKAAJOFAAC0UZ4SJofNhRzihZuNAQ",caption="""
    PHP darslari | 7-dars | Shart operatorlari 2-qism             
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKu2WdbtlAcuUO26TZuXHfxfij2IKeAAJPFAAC0UZ4SJUZ1sZBIma1NAQ",caption="""
    PHP darslari | 8-dars | Switch Operatori                     
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 9-10 darslar
@php_menu_router.message(F.text == "9-10 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKvmWdbxwaszjlTfCbo_66YtwLVW4-AAJQFAAC0UZ4SP1e8heVsq4GNAQ",caption="""
    PHP darslari | 9-dars | switch operatorida mashq           
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKv2Wdbxw-Zj5kfGAeOqo_ngye6ESEAAJRFAAC0UZ4SK1X7PmGR4CWNAQ",caption="""
    PHP darslari | 10-dars | takrorlanish operatori (For)                    
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 11-12 darslar
@php_menu_router.message(F.text == "11-12 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKwmWdb1f3SVLKRWsp2Mqk20FHwJs6AAJSFAAC0UZ4SJsN6Ih1gqMqNAQ",caption="""
    PHP darslari | 11-dars | While (takrorlanish operatori)           
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKw2Wdb1f-p3hcan83L4VyCDE6nmDxAAJTFAAC0UZ4SPHuZacLSnEgNAQ",caption="""
    PHP darslari | 12-dars | massiv(array)                   
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 13-14 darslar
@php_menu_router.message(F.text == "13-14 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKxmWdb5yn0mdMWdgseQHooFaM06TaAAJUFAAC0UZ4SM2I9FX6_R9FNAQ",caption="""
    PHP darslari | 13-dars | Assotsative && Ko'p o'lchamli arrays           
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKx2Wdb5xQ36dn4H3lrnP1Y-TCC0M6AAJVFAAC0UZ4SOMdZCD0mo9INAQ",caption="""
    PHP darslari | 14-dars | Foreach              
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 15-16 darslar
@php_menu_router.message(F.text == "15-16 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKymWdb9WKso31CrzceqL073EiY_2GAAJWFAAC0UZ4SJfxooShB9M7NAQ",caption="""
    PHP darslari | 15-dars | Massiv va Foreach ga doir mashq       
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKy2Wdb9VGcioZboXgqF6LFsJ28dkrAAJXFAAC0UZ4SEiMVlLj7WYpNAQ",caption="""
    PHP darslari | 16-dars | funktsiya(function)            
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 17-18 darslar
@php_menu_router.message(F.text == "17-18 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKzmWdcBAyEQ4VBPnN0-dXLWNWx5dsAAJYFAAC0UZ4SItuQGnzUyHaNAQ",caption="""
    PHP darslari | 17-dars | include     
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKz2WdcBDpPSpBuLIc0AF5GeRJHvEYAAJZFAAC0UZ4SMDeV8xo3H8oNAQ",caption="""
    PHP darslari | 18-dars | Super Globalniy o'zgaruvchilar            
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 19-20 darslar
@php_menu_router.message(F.text == "19-20 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIK0mWdcFJFmPHeeX82qeNjJVtzswzsAAJaFAAC0UZ4SAl0tIxeXtN0NAQ",caption="""
    PHP darslari | 19-dars | POST va GET 
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIK02WdcFLohjDCHhdQtzPm78oGaI40AAJbFAAC0UZ4SIYYitEUUGnyNAQ",caption="""
    PHP darslari | 20-dars | SESSION va COOKIE            
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 21-22 darslar
@php_menu_router.message(F.text == "21-22 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIK1mWdcI4Z2cp0XTiaztQpWph8LN51AAJcFAAC0UZ4SKoHftIkZKN-NAQ",caption="""
    PHP darslari | 21-dars | const, define
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIK12WdcI7dNIy3U9XvYmplcfhEju-kAAJdFAAC0UZ4SMr4LCTigKIoNAQ",caption="""
    PHP darslari | 22-dars | mashq(fibanachi sonlar ketma-ketligi)           
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 23-24 darslar
@php_menu_router.message(F.text == "23-24 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIK2mWdcMzjijN4-IGKozfGjgtpza5JAAJeFAAC0UZ4SAiYbrJs3IKqNAQ",caption="""
    PHP darslari | 23-dars | mashq tub sonlarni aniqlash
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIK22WdcMwSUEM_czDyOcoh5-A5Wc_yAAKrEQACHryoSNVb8C4epnMgNAQ",caption="""
    PHP darslari | 24-dars | PHP va SQL ni bog’lanishi           
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 25-26 darslar
@php_menu_router.message(F.text == "25-26 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIK3mWdcQq076kYYdC8nMoltvihqiiAAAJfFAAC0UZ4SJxqiP-wQp2iNAQ",caption="""
    PHP darslari | 25-dars | SQlga insert, update, delete amallari
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIK32WdcQqp5IMezrUAAQcxkC4F3dDl8gACYBQAAtFGeEg7et_N7GogejQE",caption="""
    PHP darslari | 26-dars | forma yordamida insert, update, delete amallari        
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 27-28 darslar
@php_menu_router.message(F.text == "27-28 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIK4mWdcUhdqM68MuMIYwABtg7fGWXv-wACYRQAAtFGeEhJ4QRkkOpShTQE",caption="""
    PHP darslari | 27-dars | forma yordamida insert, update, delete validate
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIK42WdcUj71UY5X7zAKM2KakA8rqMlAAJiFAAC0UZ4SC0tBOMWdDjfNAQ",caption="""
    PHP darslari | 28-dars | form orqali update buyrug’i        
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 29-30 darslar
@php_menu_router.message(F.text == "29-30 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIK5mWdcYNkELQ4EJidq9UNr7bpJ5tEAAJjFAAC0UZ4SG9Tiqz5BJOLNAQ",caption="""
    PHP darslari | 29-dars | delete & view pages
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIK52WdcYP_FH2SAsx-t3B0lGfCsBV7AAJkFAAC0UZ4SM87wZoUF7XfNAQ",caption="""
    PHP darslari | 30-dars | image upload, Rasm yuklash  
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                      
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")

# 31 dars
@php_menu_router.message(F.text == "31 dars (php)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIK6mWdcc-v7x1SXz9ADG8tB6f2HUBsAAJlFAAC0UZ4SEEb-DHpOK69NAQ",caption="""
    PHP darslari | 31-dars | image upload, Rasm yuklash 2-qism
\nYoutube — www.youtube.com/c/CodeLeader \nTelegram — @codeleaderuz                           
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")