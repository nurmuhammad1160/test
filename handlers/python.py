from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.nodejs_menu import nodejs_menu
from keyboards.python_menu import python_menu

python_menu_router: Router = Router()


@python_menu_router.message(F.text == "Python darslari")
async def python(message: Message):
    await message.answer("Python darslari",reply_markup=python_menu)



# 1-2 darslar
@python_menu_router.message(F.text == "1-2 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJ-2WdYUEU2ypkwuhuF7taiBXyi1fQAAJwEgACxRTQS66mQvd_vmKuNAQ",caption="""
    Python darslari | 1-dars | Kirish so'z                             
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJ_GWdYUEpRcb_8-jawxNuRBrTnpqWAAJxEgACxRTQSzSdwel6wjnRNAQ",caption="""
    Python darslari | 2-dars | Variables                        
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 3-4 darslar
@python_menu_router.message(F.text == "3-4 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKHmWdYpeRZlKeoCo11wNJgHjQllXYAAJzEgACxRTQS73zV_lQSTNwNAQ",caption="""
    Python darslari | 3-dars | Anaconda o'rnatamiz                         
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKH2WdYpcChtOcaBtXRHLlKSVw7Fv-AAJ0EgACxRTQSyNWA63MxV6zNAQ",caption="""
    Python darslari | 4-dars | Brauzerda kod yozish (Repl.it)                  
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 5-6 darslar
@python_menu_router.message(F.text == "5-6 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKJWWdY-oVAbN-jVgumTYL5LdLRFlsAAJ4EgACxRTQS2TrDKx3PAuANAQ",caption="""
    Python darslari | 5-dars | Birinchi Dasturimiz                        
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKJmWdY-rnOwiTPErtJGTyuYKS4nIQAAJ6EgACxRTQS3i7g5j6qSt9NAQ",caption="""
    Python darslari | 6-dars | print(), Arifmetik amallar va Sinteks                 
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 7-8 darslar
@python_menu_router.message(F.text == "7-8 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKKWWdZFNtbx8dc8JQC8SbxnbhZ_KQAAJ8EgACxRTQS9hm20qtg92ONAQ",caption="""
    Python darslari | 7-dars | O'zgaruvchilar (Variables)                     
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKKmWdZFMTkz_kxCqb5BEqeby4ZLQPAAJ-EgACxRTQSz8Yv1YVI7YZNAQ",caption="""
    Python darslari | 8-dars | Matn bilan ishlash (Strings)               
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 9-10 darslar
@python_menu_router.message(F.text == "9-10 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKLWWdZJOKN5O7aX7WOmCAgrbuITqjAAJ_EgACxRTQS4jV84XyDUZyNAQ",caption="""
    Python darslari | 9-dars | Sonlar bilan ishlash                 
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKLmWdZJPaAAFBg6uDQfdRN4Ae6jNSAwACghIAAsUU0EsDfK-fgfSaWDQE",caption="""
    Python darslari | 10-dars | Lists (Ro'yxatlar)             
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 11-12 darslar
@python_menu_router.message(F.text == "11-12 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKMWWdZNrcX9NXspC-uIwSCq5W4GoAA4USAALFFNBLlwABFuuRZqXmNAQ",caption="""
    Python darslari | 11-dars | Ro'yxat bilan ishlash. O'zgarmas ro'yxatlar (Tuples)              
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKMmWdZNq0efI_3369v-DOaLClGeD3AAKIEgACxRTQSwfKUaBZU6p8NAQ",caption="""
    Python darslari | 12-dars | for sikli bilan tanishamiz          
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 13-14 darslar
@python_menu_router.message(F.text == "13-14 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKNWWdZR0zsPEEHP7rZO8ldxbYFOFcAAKNEgACxRTQSxBU3N5NffXVNAQ",caption="""
    Python darslari | 13-dars | if-else shartlari va tarmoqlanish           
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKNmWdZR2eGLCvPpgPR01p5aBCMQQ6AAKUEgACxRTQS_DP71KWCOnJNAQ",caption="""
    Python darslari | 14-dars | if-elif-else        
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 15-16 darslar
@python_menu_router.message(F.text == "15-16 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKOWWdZV9EAgHW55Y0aIjOcq1gUFdGAAKWEgACxRTQS5RoCvzES9opNAQ",caption="""
    Python darslari | 15-dars | Eng ko'p uchraydigan xatolar     
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKOmWdZV8oxY_L_LEtwkAi5TOWSgx4AAKaEgACxRTQS1O40EVTGjsxNAQ",caption="""
    Python darslari | 16-dars | GitHub bilan tanishuv   
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 17-18 darslar
@python_menu_router.message(F.text == "17-18 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKPWWdZYvCBSyL5CZXJrVWsG3DPQJiAAKfEgACxRTQS7wL2v-B4CV6NAQ",caption="""
    Python darslari | 17-dars | Lug'at (Dictionary)
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKPmWdZYt-5Zu_F0_UdpboU3MgVKfAAAKiEgACxRTQS2OIfO14D6I4NAQ",caption="""
    Python darslari | 18-dars | Lug'at bilan ishlaymiz  
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 19-20 darslar
@python_menu_router.message(F.text == "19-20 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKQWWdZgO0KlI_RvD4MJzsXGhdrPjzAAKkEgACxRTQS7x9NbthZb_RNAQ",caption="""
    Python darslari | 19-dars | Nesting
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKQmWdZgMSzpfLfffvK2uxbTLvVYBNAAKmEgACxRTQS3vfjeVkTgXQNAQ",caption="""
    Python darslari | 20-dars | While sikli 
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 21-22 darslar
@python_menu_router.message(F.text == "21-22 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKRWWdZkY8ockJ4ZW5UuFJQMe7i3Q3AAKoEgACxRTQS35bhPzDsnfgNAQ",caption="""
    Python darslari | 21-dars | While, Ro'yxatlar va Lug'atlar
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKRmWdZkYOBHtzCAFrjHO932v9oyNTAAKqEgACxRTQS6D0uz4Q1_J3NAQ",caption="""
    Python darslari | 22-dars | Funksiya
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 23-24 darslar
@python_menu_router.message(F.text == "23-24 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKSWWdZp5N1joV_GKSdpQD1zNPYR1dAAKwEgACxRTQS5THTjX0bPb1NAQ",caption="""
    Python darslari | 23-dars | Funksiyadan qiymat qaytarish
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKSmWdZp6-bsOgy0EmvFprTyTivCRJAAKzEgACxRTQS0bRJjxsdbaXNAQ",caption="""
    Python darslari | 24-dars | Funksiyaga ro'yxat uzatish
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 25-26 darslar
@python_menu_router.message(F.text == "25-26 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKTWWdZunI1YbJlynHI2Go9jQETpO3AAK1EgACxRTQS7Vq2SZfney3NAQ",caption="""
    Python darslari | 25-dars | Moslashuvchan funksiyalar
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKTmWdZulaj-10VFuvGzjap9FM5SAtAAK2EgACxRTQSziCHbNOL5NrNAQ",caption="""
    Python darslari | 26-dars | Modullar
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 27-28 darslar
@python_menu_router.message(F.text == "27-28 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKUWWdZzW3FXG-VnOKDiJglKpamx9RAAK5EgACxRTQSxmrSZ8YqZlkNAQ",caption="""
    Python darslari | 27-dars | Funksiya. So'ngso'z
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKUmWdZzUGUrds6h9q9Io87o8MJjwzAAK6EgACxRTQS7ToHEIeCXJ6NAQ",caption="""
    Python darslari | 28-dars | Son topish o'yini. 1-qism
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 29-30 darslar
@python_menu_router.message(F.text == "29-30 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKVWWdZ33OAmZP6TUHnKwm0nXiKbXCAAK7EgACxRTQS7O1uI4ZQGuQNAQ",caption="""
    Python darslari | 29-dars | Son topish o'yini. 2-qism
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKVmWdZ30fdVkWqwXBm-mZ7EhbsU-VAAK9EgACxRTQS1QTtCokm_drNAQ",caption="""
    Python darslari | 30-dars | Son topish o'yini. 3-qism
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 31-32 darslar
@python_menu_router.message(F.text == "31-32 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKWWWdZ8jSrqq3ZTsRtIrF__C0COByAAK-EgACxRTQS0CHIYTzUGwAATQE",caption="""
    Python darslari | 31-dars | So'z topish o'yini. 1-qism. Tanishuv
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKWmWdZ8hGthF-UmaiybgU6FyvFmpLAAK_EgACxRTQS4_kP9b8zshbNAQ",caption="""
    Python darslari | 32-dars | So'z topish o'yini. 2-qism. Kod
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 33-34 darslar
@python_menu_router.message(F.text == "33-34 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKXWWdaB1uyLtZogABWxn3HYuPaSPrxwACwBIAAsUU0EvMPWOuwxoR6TQE",caption="""
    Python darslari | 33-dars | Kirill-Lotin Transliterator Bot. 1-qism
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKXmWdaB1Qm5PLkfTBmidvJCvHViVFAALCEgACxRTQS6kKAY55VdRoNAQ",caption="""
    Python darslari | 34-dars | Kirill-Lotin Transliterator Bot. 2-qism
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 35-36 darslar
@python_menu_router.message(F.text == "35-36 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKYWWdaGRQBOH_vNkelVuVo_gC9AoGAALDEgACxRTQS8ZlY2Q6XwMcNAQ",caption="""
    Python darslari | 35-dars | Object Oriented Dasturlash nima?
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKYmWdaGQba9bJvvPOnwGk-J9HQcEKAALEEgACxRTQS7dSlIrHYXbcNAQ",caption="""
    Python darslari | 36-dars | Object Oriented Dasturash. Klass va Obyekt
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 37-38 darslar
@python_menu_router.message(F.text == "37-38 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKZWWdaM4B6UADg8cnM7egnabuBBxEAALFEgACxRTQSzLRZxbx1LY8NAQ",caption="""
    Python darslari | 37-dars | Object Oriented Dasturash. Obyektlar bilan ishlash
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKZmWdaM7TEgkg19tu9wKY4psUDWSUAALGEgACxRTQSwfRUv46hzXxNAQ",caption="""
    Python darslari | 38-dars | Object Oriented Dasturash. Vorislik va Polimorfizm
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 39-40 darslar
@python_menu_router.message(F.text == "39-40 dars (python)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIKaWWdaRb69KXa3IeLj1O2KxcCsypvAALHEgACxRTQS-5Ij5yOkxeKNAQ",caption="""
    Python darslari | 39-dars | Object Oriented Dasturash. Inkapsulyatsiya
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                             
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIKamWdaRbMIRtc4-TO7ocAAUpi2gXzdAACyhIAAsUU0Et99g-rIFLeYDQE",caption="""
    Python darslari | 40-dars | Object Oriented Dasturash. Dunder Metodlar
\nYoutube — www.youtube.com/c/Sariqdev \nTelegram — @sariqdev                         
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
