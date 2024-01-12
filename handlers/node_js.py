from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.nodejs_menu import nodejs_menu
from keyboards.beckend_keyboard import start_menu

node_js_menu_router: Router = Router()

@node_js_menu_router.message(F.text == "Node JS darslari")
async def node_js(message:Message):
    await message.answer("Node JS darslari",reply_markup=nodejs_menu)


@node_js_menu_router.message(F.text=="Orqaga.")
async def orqaga(message: Message):
    await message.answer("Ozingizga ma'qul darslarni tanglang",reply_markup=start_menu)

# 1-2 darslar
@node_js_menu_router.message(F.text == "1-2 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHLmWATk2iL3_gnVO5GGPX2wbYRrt5AAJrEQACvq_xSCnRzr9Dgn9RMwQ",caption="""
    Node JS darslari | 1-dars | Kirish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHL2WATk06Krq8HcadqC1GWw-zzBS1AAJsEQACvq_xSNHmo_rZznndMwQ",caption="""
    Node JS darslari | 2-dars | Node o'zi nima
\nYoutube — www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 3-4 darslar
@node_js_menu_router.message(F.text == "3-4 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHN2WAT8ESzXsU6tLUs1F-8x9MUAbaAAJtEQACvq_xSOunizxYLQUgMwQ",caption="""
    Node JS darslari | 3-dars | Node qanday ishlaydi
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHOGWAT8FGDIMqtJcWx5rO_D3Wr2n5AAJuEQACvq_xSNKlsZkznDnzMwQ",caption="""
    Node JS darslari | 4-dars | Node arxitekturasi
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 5-6 darslar
@node_js_menu_router.message(F.text == "5-6 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHO2WAVOKnQ0pjiihepnYVwthYtkI2AAJvEQACvq_xSPopvAgv2F-ZMwQ",caption="""
    Node JS darslari | 5-dars | Node'ni o'rnatib unda ilk dasturimizni yozamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHPGWAVOLM8m14FUyTmC2otHmgJMrZAAJwEQACvq_xSIunWiWx7siCMwQ",caption="""
    Node JS darslari | 6-dars | global obyekti haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 7-8 darslar
@node_js_menu_router.message(F.text == "7-8 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHP2WAVTOE3jWl0C5I1W6rgjAtHGMHAAJxEQACvq_xSJFu8V-WR-IsMwQ",caption="""
    Node JS darslari | 7-dars | Module tushunchasi
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHQGWAVTPYHgGY2n__R1sMFgaGaD1sAAJyEQACvq_xSPFmqOwCXGCjMwQ",caption="""
    Node JS darslari | 8-dars | Yangi modul qo'shish va undagi obyektlarni eksport qilish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 9-10 darslar
@node_js_menu_router.message(F.text == "9-10 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHQ2WAVXsZ4V0oi24pOyk_jVfamePbAAJzEQACvq_xSAXj3nxlN-3DMwQ",caption="""
    Node JS darslari | 9-dars | Modulni yuklash va undan foydalanish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHRGWAVXucqSJvraW4r_HdyhZVmjMGAAJ0EQACvq_xSHdrsS7AJApKMwQ",caption="""
    Node JS darslari | 10-dars | Nodedagi path moduli
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 11-12 darslar
@node_js_menu_router.message(F.text == "11-12 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHR2WAVlCajpJPAAE56Ao_pdhKsZVc9QACdREAAr6v8UhoOezzcPaXSjME",caption="""
    Node JS darslari | 11-dars | os moduli haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHSGWAVlC2TMXX7QtfZD-FaEQU9ChRAAJ2EQACvq_xSCUUMOqm1yksMwQ",caption="""
    Node JS darslari | 12-dars | fs moduli bilan ishlaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 13-14 darslar
@node_js_menu_router.message(F.text == "13-14 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHW2WAZiGXF0bVBk878IgesLHJaVqzAAJ3EQACvq_xSGE0h6NhivVtMwQ",caption="""
    Node JS darslari | 13-dars | events moduli bilan tanishamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHXGWAZiHhFOccQyTz5IKDICf0x52sAAJ5EQACvq_xSMeM-hG-ncfuMwQ",caption="""
    Node JS darslari | 14-dars | EventEmitter'dan samarali foydalanish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 15-16 darslar
@node_js_menu_router.message(F.text == "15-16 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHX2WAZqI6UqvfOCRBw6u4jL1uP7mqAAJ6EQACvq_xSJxxxPdqF6EaMwQ",caption="""
    Node JS darslari | 15-dars | http moduli bilan ishlaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHYGWAZqIZFGvPzz7R5f-8iBexIdWGAAJ7EQACvq_xSPh701PRkvBaMwQ",caption="""
    Node JS darslari | 16-dars | npm haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 17-18 darslar
@node_js_menu_router.message(F.text == "17-18 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHY2WAZvpKld0F3qlkLJCloRSQw9w9AAJ8EQACvq_xSEYv8G3oPzxdMwQ",caption="""
    Node JS darslari | 17-dars | package.json va npm init
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHZGWAZvoWuR2njbVcr2Zw7fjSC9vPAAJ9EQACvq_xSKwgozBUWvKnMwQ",caption="""
    Node JS darslari | 18-dars | Loyihaga npm paket o'rnatish (npm install)
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 19-20 darslar
@node_js_menu_router.message(F.text == "19-20 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHZ2WAZ16t94_MOQsjzwwK5uvPDB0jAAJ-EQACvq_xSMGjl8iteWw_MwQ",caption="""
    Node JS darslari | 19-dars | npm paketlaridan foydalanish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHaGWAZ177FDyCny5F8iQlkGYY_80_AAKAEQACvq_xSEqUIo2wjC0ZMwQ",caption="""
    Node JS darslari | 20-dars | Semantic Versioning tushunchasi haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 21-22 darslar
@node_js_menu_router.message(F.text == "21-22 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHa2WAZ9qOzVt3CBCL_99czDYXvpbPAAKBEQACvq_xSCCKpuLL4MlXMwQ",caption="""
    Node JS darslari | 21-dars | npm list buyrug'i
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHbGWAZ9o4zTuonI3kLvipQEyG-BM4AAKCEQACvq_xSGI2BGnB8ctQMwQ",caption="""
    Node JS darslari | 22-dars | npm view buyrug'i
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 21-22 darslar
@node_js_menu_router.message(F.text == "21-22 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHa2WAZ9qOzVt3CBCL_99czDYXvpbPAAKBEQACvq_xSCCKpuLL4MlXMwQ",caption="""
    Node JS darslari | 21-dars | npm list buyrug'i
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHbGWAZ9o4zTuonI3kLvipQEyG-BM4AAKCEQACvq_xSGI2BGnB8ctQMwQ",caption="""
    Node JS darslari | 22-dars | npm view buyrug'i
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 23-24 darslar
@node_js_menu_router.message(F.text == "23-24 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHkWWAaMd_ML8k-Sk-jVf20B1RO_kKAAKDEQACvq_xSIpc1gcBLHt8MwQ",caption="""
    Node JS darslari | 23-dars | npm outdated va npm update buyruqlari
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHkmWAaMePCl8Y7c7WeKTT8fqfLQABkQAChBEAAr6v8UjGKzT6oQPX1zME",caption="""
    Node JS darslari | 24-dars | devDependencies haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 





# 25-26 darslar
@node_js_menu_router.message(F.text == "25-26 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHmGWA7DVFK9DyoQ6PJ_DSVwFMIZIFAAKFEQACvq_xSKlDP6vKMr4YMwQ",caption="""
    Node JS darslari | 25-dars | npm paketni o'chirib tashlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHmWWA7DX-w3hpbqrmkMVW94AqDDpCAAKGEQACvq_xSBomBO367QHuMwQ",caption="""
    Node JS darslari | 26-dars | npm paketni repozitoriyga joylash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 






# 27-28 darslar
@node_js_menu_router.message(F.text == "27-28 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHnGWA7H0D4VTsvRdQi5Vk4U7lhTZ_AAKJEQACvq_xSKeDyRLvVVZ3MwQ",caption="""
    Node JS darslari | 27-dars | RESTful API haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHnWWA7H2fUnM8CtYjYWDc1Io90T_7AAKKEQACvq_xSOTvJ5BpWZDxMwQ",caption="""
    Node JS darslari | 28-dars | Ilk express dasturimiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 29-30 darslar
@node_js_menu_router.message(F.text == "29-30 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHoGWA7M5bh94oNP0Nt6KoCoNbCtU1AAKMEQACvq_xSOp2xBhAluacMwQ",caption="""
    Node JS darslari | 29-dars | Route parameterlar haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHoWWA7M7E3nOGCYIpz5ysKsC2vst_AAKOEQACvq_xSAUpD-sswGO1MwQ",caption="""
    Node JS darslari | 30-dars | Route parameter bilan amaliy mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 





# 31-32 darslar
@node_js_menu_router.message(F.text == "31-32 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHpGWA7RSa8Kb1BrP-u9wfhwjZeOGyAAKPEQACvq_xSD_BkahiVYviMwQ",caption="""
    Node JS darslari | 31-dars | Express'da HTTP Post so'rovlari bilan ishlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHpWWA7RTdMX8u-OR12DAyc0jD5p9kAAKQEQACvq_xSBCjuXNJBR7qMwQ",caption="""
    Node JS darslari | 32-dars | Postman yordamida API hizmatni testlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 33-34 darslar
@node_js_menu_router.message(F.text == "33-34 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHqGWA7WAhwIObjIyR3aJqvZfOu7WqAAKREQACvq_xSJWwVGvTFYBPMwQ",caption="""
    Node JS darslari | 33-dars | So'rovlarni validation qilish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHqWWA7WA9nBNaLt40htjUZ5cij_A4AAKSEQACvq_xSOkOpie-WYOdMwQ",caption="""
    Node JS darslari | 34-dars | HTTP PUT so'rovlari bilan ishlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 35-36 darslar
@node_js_menu_router.message(F.text == "35-36 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHrGWA7gy3xsCsPN5dJhHu3Y5-BDq9AAKTEQACvq_xSJaHsDK9vWOtMwQ",caption="""
    Node JS darslari | 35-dars | HTTP DELETE so'rovi orqali resursni o'chirish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHrWWA7gwfnq0_K9kQVaKcr1Z9uu5bAAKVEQACvq_xSEReK1xSUun9MwQ",caption="""
    Node JS darslari | 34-dars | HTTP PUT so'rovlari bilan ishlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 37-38 darslar
@node_js_menu_router.message(F.text == "37-38 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHsGWA7lsP8PjoMojpcaJjkwKk8O-rAAKXEQACvq_xSMu3oOB8vJLbMwQ",caption="""
    Node JS darslari | 37-dars | Topshiriq natijasini tekshiramiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHsWWA7lsS_qB3nG95BSfj-2PFGqXOAAKYEQACvq_xSFY2sNZus873MwQ",caption="""
    Node JS darslari | 38-dars | Middleware funktsiyalari haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 39-40 darslar
@node_js_menu_router.message(F.text == "39-40 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHtGWA7rpWJpglgnOTjlYJP5x7Eo7ZAAKcEQACvq_xSH22OLfjChenMwQ",caption="""
    Node JS darslari | 39-dars | Custom middleware funktsiya yozamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHtWWA7rqD3EOFR4o4Dj9bVcFCGRxXAAKdEQACvq_xSLxaccOJrt_8MwQ",caption="""
    Node JS darslari | 40-dars | helmet() va morgan() middleware funktsiyalari
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 41-42 darslar
@node_js_menu_router.message(F.text == "41-42 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHxGWA75aBLGoMFJ7MO0m1mGhPNREBAAKfEQACvq_xSGAuTPRUfrLVMwQ",caption="""
    Node JS darslari | 41-dars | urlencoded() va static() middleware funktsiyalari
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHxWWA75ayWVZoTaeUhChOQmI-YtcZAAKgEQACvq_xSOx_SvquhAABzDME",caption="""
    Node JS darslari | 42-dars | Dasturning ishlash muhiti
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 43-44 darslar
@node_js_menu_router.message(F.text == "43-44 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHyGWA7-_Ur1dwPjslEmp4qFDMMUgjAAKhEQACvq_xSBjxnS-qQzMvMwQ",caption="""
    Node JS darslari | 43-dars | Dasturning sozlamalarini config-faylda saqlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHyWWA7-97B3elOG7nDRwTD-3Q8WQJAAKiEQACvq_xSMiZO3E5HPD0MwQ",caption="""
    Node JS darslari | 44-dars | 'Pug view engine'dan foydalanish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 45-46 darslar
@node_js_menu_router.message(F.text == "45-46 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIHzGWA8EvjA1ClP1ShmSTETnEOfeZXAAKkEQACvq_xSMrRjNROBysMMwQ",caption="""
    Node JS darslari | 45-dars | Loyihamiz tuzilmasini tartibga keltiramiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIHzWWA8Et-GaGKJ3uQnhJwGOD_JFwnAAKlEQACvq_xSIHBUyzuSMKQMwQ",caption="""
    Node JS darslari | 46-dars | Topshiriq
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 47-48 darslar
@node_js_menu_router.message(F.text == "47-48 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH0GWA8on2isHYwmao1hw-Q4Lnxl2_AAKmEQACvq_xSP_4B6SeAAHRojME",caption="""
    Node JS darslari | 47-dars | mongoDBni o'rnatamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH0WWA8onOmZf4iJowpiuD7PWyQY77AAKnEQACvq_xSFr4IWPMD1MCMwQ",caption="""
    Node JS darslari | 48-dars | mongoDBga ulanamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 


# 49-50 darslar
@node_js_menu_router.message(F.text == "49-50 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH1GWA8ubBdNVV4tWNCwMTxKQKPypdAAKoEQACvq_xSJG3HGjqmbnVMwQ",caption="""
    Node JS darslari | 49-dars | mongoose'dagi schema tushunchasi
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH1WWA8ub_lo1C_zlSA4lbX46hnNcUAAKpEQACvq_xSGzjCWEUC6jEMwQ",caption="""
    Node JS darslari | 50-dars | mongoose'dagi model tushunchasi
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 51-52 darslar
@node_js_menu_router.message(F.text == "51-52 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH2GWA8zMZXPUObiQfLcniCajKOTrDAAIpEQACSIvxSE0DmhueNwGNMwQ",caption="""
    Node JS darslari | 51-dars | Hujjatni mongoDBga saqlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH2WWA8zOAUdKbZvOfx5bLuIkQ6TbJAAIqEQACSIvxSON5sFgt6ktaMwQ",caption="""
    Node JS darslari | 52-dars | mongoDBdan hujjatlarni o'qish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 53-54 darslar
@node_js_menu_router.message(F.text == "53-54 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH3GWA851ouXZJwWpXoipy2WC4yMTIAAIrEQACSIvxSHGxxAkAAXuJ9DME",caption="""
    Node JS darslari | 53-dars | Hujjatlarni o'qishda filtrlardan foydalanish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH3WWA853y0v3d-7vezOUyoF89OeZ1AAItEQACSIvxSJwPDylS0dcEMwQ",caption="""
    Node JS darslari | 54-dars | Hujjatlarni izlashda RegEx'dan foydalanish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 55-56 darslar
@node_js_menu_router.message(F.text == "55-56 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH4GWA8-sW9YorWVgvJGCPVfCrVt92AAI2EQACSIvxSJqaaMwi_WWsMwQ",caption="""
    Node JS darslari | 55-dars | Ma'lumotni pagination qilish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH4WWA8-sOCOWU9xnTsMvj4ApmCGWXAAI3EQACSIvxSOvfAAGVHmCcwTME",caption="""
    Node JS darslari | 56-dars | Amaliy mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 57-58 darslar
@node_js_menu_router.message(F.text == "57-58 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH5GWA9EIsM7xSFPLMq3cEydBmTKxLAAI4EQACSIvxSN2D137l3axkMwQ",caption="""
    Node JS darslari | 57-dars | Amaliy mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH5WWA9EKb71gpa9sVnixbpZ136MNyAAI5EQACSIvxSMTq5kAB1RZLMwQ",caption="""
    Node JS darslari | 58-dars | mondoDBda hujjatlarni yangilash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 59-60 darslar
@node_js_menu_router.message(F.text == "59-60 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH6GWA9JKwzXWwG1H95OYoeV8KU7qBAAI6EQACSIvxSAX1rMJp6mJtMwQ",caption="""
    Node JS darslari | 59-dars | mondoDBdan hujjatlarni o'chirib tashlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH6WWA9JLPWsQebvD-I_BooXq9vdSRAAI7EQACSIvxSDXqhDsWi8vYMwQ",caption="""
    Node JS darslari | 60-dars | Mongoose'dagi validatorlardan foydalanish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 





# 61-62 darslar
@node_js_menu_router.message(F.text == "61-62 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH-GWA9YnX7nfCOXaEAsBuOkiVFy3-AAI9EQACSIvxSCXR2UwRlxUyMwQ",caption="""
    Node JS darslari | 61-dars | Mongoose'da custom validator yozamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH-WWA9YkovE2C0m2BcB8VTEkvalv8AAI-EQACSIvxSGq3LgwaMVacMwQ",caption="""
    Node JS darslari | 62-dars | Schema Type obyektlari
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 63-64 darslar
@node_js_menu_router.message(F.text == "63-64 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIH_GWA9iad0baWAo0104cAAXqUC6vuEAACPxEAAkiL8UhhkM-3D7Ma3zME",caption="""
    Node JS darslari | 63-dars | Topshiriq
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIH_WWA9iZ2yyC4uzQh8sFii8c7W1JRAAJAEQACSIvxSJpVlKlXmT4WMwQ",caption="""
    Node JS darslari | 64-dars | Amaliy mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 65-66 darslar
@node_js_menu_router.message(F.text == "65-66 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIA2WA9zH8uWKIjwK0U4D0xBdtG8JnAAJCEQACSIvxSF5V7RwjTtkUMwQ",caption="""
    Node JS darslari | 65-dars | Amaliy mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIBGWA9zGfdXdxEFdvG9V0rVHqjRfhAAJDEQACSIvxSLLwUI620WivMwQ",caption="""
    Node JS darslari | 66-dars | MongoDBdagi hujjaltar orasidagi aloqalarni modellashtirish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 


# 67-68 darslar
@node_js_menu_router.message(F.text == "67-68 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIB2WA9_uKGsOLAejDQRVx_Q6Y5YPxAAJEEQACSIvxSMnuZdC12l3fMwQ",caption="""
    Node JS darslari | 67-dars | MongoDBda hujjaltar orasida ko'rsatgichli bog'liqlik
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIICGWA9_urhzLVzQLYBuVlY447GMdRAAJFEQACSIvxSMQsOzvvCkOcMwQ",caption="""
    Node JS darslari | 68-dars | MongoDbda hujjatlarni bir-biriga joylash (embedding)
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 


# 69-70 darslar
@node_js_menu_router.message(F.text == "69-70 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIC2WA-E_WWon3d3ggVhVRioNpXGaYAAJGEQACSIvxSMTmX9-lUiUDMwQ",caption="""
    Node JS darslari | 69-dars | MongoDbda Tranzaktsiyalar haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIDGWA-E821LF8VGWlFlfImLASw7brAAJHEQACSIvxSIvBj7J2DRPGMwQ",caption="""
    Node JS darslari | 70-dars | ObjectId haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 71-72 darslar
@node_js_menu_router.message(F.text == "71-72 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIEmWBMhp3dQgYelG7R124T4B2bbnvAAJIEQACSIvxSIOj75e83E_jMwQ",caption="""
    Node JS darslari | 71-dars | Amalish mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIE2WBMhqooj0oYv89fgFtHO0y_iZ7AAJJEQACSIvxSM6x4hm3To2bMwQ",caption="""
    Node JS darslari | 72-dars | Amalish mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 73-74 darslar
@node_js_menu_router.message(F.text == "73-74 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIFmWBMoFnZf43cYILJrZHsDDgCC53AAJKEQACSIvxSIwGh6PP9aE9MwQ",caption="""
    Node JS darslari | 73-dars | MongoDBda fayllarni saqlash (GridFS)
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIF2WBMoHJ6_RkMVxNZIJSOyof6LQHAAJLEQACSIvxSBTmnckQyKe1MwQ",caption="""
    Node JS darslari | 74-dars | Autentifikatsiya va avtorizatsiya
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 75-76 darslar
@node_js_menu_router.message(F.text == "75-76 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIGmWBMtBO1ZeAW-NCe6tT49Yqd0yLAAJMEQACSIvxSHDuuQMWIH7uMwQ",caption="""
    Node JS darslari | 75-dars | Foydalanuvchilarni ro'yhatga olish uchun API quramiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIG2WBMtCzLhdgWv5VTf1RA_epMY95AAJOEQACSIvxSFjQv4ffQSEjMwQ",caption="""
    Node JS darslari | 76-dars | Lodash paketidan foydalanamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 77-78 darslar
@node_js_menu_router.message(F.text == "77-78 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIHmWBMxn7eAtcFtdXUBlfJzpgndNIAAJPEQACSIvxSPVJcOshL16gMwQ",caption="""
    Node JS darslari | 77-dars | Ma'lumotni hash qilish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIH2WBMxl0MBp862WYDbNdGmTbUycTAAJREQACSIvxSEykVLMRXo4VMwQ",caption="""
    Node JS darslari | 78-dars | Foydalanuvchini autentifikatsiya qilish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 79-80 darslar
@node_js_menu_router.message(F.text == "79-80 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIImWBM2NggfmgzfBXppE55GmRGv0tAAJSEQACSIvxSB2lyhTlRt9_MwQ",caption="""
    Node JS darslari | 79-dars | Json Web Token (JWT) haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIII2WBM2PepOwmLIvFdX9Zky4PxK2lAAJTEQACSIvxSEvmRo4Z-M1wMwQ",caption="""
    Node JS darslari | 80-dars | JWT bilan ishlaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 81-82 darslar
@node_js_menu_router.message(F.text == "81-82 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIJmWBM7OC6ekme4AE5EXcApsp07iQAAJWEQACSIvxSOUnjnzn6ewUMwQ",caption="""
    Node JS darslari | 81-dars | Mahfiy kalitni muhit o'zgaruvchisida saqlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIJ2WBM7O9nYhZCH7lPtCQxoRw_OdeAAJaEQACSIvxSEVfKF0WCDMhMwQ",caption="""
    Node JS darslari | 82-dars | Loyihamizda authorizationni yo'lga qo'yamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 83-84 darslar
@node_js_menu_router.message(F.text == "83-84 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIKmWBM_5A66WieYfq6JtAX2G6p0-VAAJbEQACSIvxSKH2LvTnL-4-MwQ",caption="""
    Node JS darslari | 83-dars | Foydalanuvchining profilini olish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIK2WBM_4BU1_yYWe4tF171bWmrQYDAAJcEQACSIvxSHTtgy3bc_6sMwQ",caption="""
    Node JS darslari | 84-dars | Role asosida authorization qilish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 85-86 darslar
@node_js_menu_router.message(F.text == "85-86 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIILmWBNFjU3woMOSwc_2JTzpZrNXhFAAJeEQACSIvxSNhkDJHea2GEMwQ",caption="""
    Node JS darslari | 85-dars | NodeJS dasturlarida xatolar boshqaruvi va log yozish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIL2WBNFhzL55fmJl3X9RcIsBcblrwAAJfEQACSIvxSB4zx06TSLEuMwQ",caption="""
    Node JS darslari | 86-dars | 'Undhandled promise rejection' xatolari haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 87-88 darslar
@node_js_menu_router.message(F.text == "87-88 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIMmWBNKX1uxsGj_3KdFXEib9wz8QiAAJgEQACSIvxSByMS9zh2QH6MwQ",caption="""
    Node JS darslari | 87-dars | Express'dagi error middleware
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIM2WBNKVJ0dCJgXrkZlbe7OV2fZiFAAJhEQACSIvxSICz7f0S2s8VMwQ",caption="""
    Node JS darslari | 88-dars | Xatolarni logga yozish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 89-90 darslar
@node_js_menu_router.message(F.text == "89-90 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIINmWBNPCGN750xm5oQpfH3wJGIHOaAAJiEQACSIvxSPJfiqyMRC3YMwQ",caption="""
    Node JS darslari | 89-dars | Loglarni MongoDBga yozish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIN2WBNPDNssDbE1CXDr_aCmBTRVOzAAJjEQACSIvxSDwwRiMgpwQkMwQ",caption="""
    Node JS darslari | 90-dars | Ilinmay qolgan xatolar boshqaruvi
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 91-92 darslar
@node_js_menu_router.message(F.text == "91-92 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIOmWBNVuN2U3PDBWaXoHEGAUyuxT7AAJkEQACSIvxSIvj2d_VnIWTMwQ",caption="""
    Node JS darslari | 91-dars | Kodimizni tozalaymiz (refactoring)
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIO2WBNVunVnb1n0OhaIgbM-iBo-RRAAJlEQACSIvxSLj8sv9CYBWqMwQ",caption="""
    Node JS darslari | 92-dars | Avtomatlashtirilgan testlash haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 93-94 darslar
@node_js_menu_router.message(F.text == "93-94 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIITmWBQPPoZzYM7BmXSqPwYBisoXMmAAJmEQACSIvxSA-IRLCFDCJpMwQ",caption="""
    Node JS darslari | 93-dars | Jest bilan Unit test yozamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIT2WBQPNEHh8mXANcOO62izhCy9VJAAJqEQACSIvxSMCcfnsB8lehMwQ",caption="""
    Node JS darslari | 94-dars | Funktsiyani unit testlar bilan qoplaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 



# 95-96 darslar
@node_js_menu_router.message(F.text == "95-96 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIUmWBQUalUNPiY1lQ6KBDjNkVZPC0AAJrEQACSIvxSKe3Xi2z2QMNMwQ",caption="""
    Node JS darslari | 95-dars | Matnlarni to'g'ri test qilish
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIU2WBQUaE7ZJkTCH4oioxEae9q9NAAAJsEQACSIvxSIZKtUS4KAfQMwQ",caption="""
    Node JS darslari | 96-dars | Qatorlarni testlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 




# 97-98 darslar
@node_js_menu_router.message(F.text == "97-98 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIVmWBQeZS1N9V6Vob-Pj54wH29IvwAAJtEQACSIvxSPgya_XdJPgjMwQ",caption="""
    Node JS darslari | 97-dars | Obyektlarni testlash
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIV2WBQeajdAy36mlPZcCVfZR8W6hBAAJuEQACSIvxSCxQAAGAMhUVnTME",caption="""
    Node JS darslari | 98-dars | Xatolarga test yozamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""") 





# 99-100 darslar
@node_js_menu_router.message(F.text == "99-100 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIWmWBQl2t7NN-p_25udc8aXuL5JBOAAJwEQACSIvxSFBU884KQgzpMwQ",caption="""
    Node JS darslari | 99-dars | Amaliy mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIW2WBQl2rL52DszbAuAAB26ZFvUu8RgACcREAAkiL8UgHJbSa20-LkDME",caption="""
    Node JS darslari | 100-dars | Mock funktsiyalar haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 101-102 darslar
@node_js_menu_router.message(F.text == "101-102 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIZmWCgFY8vnXUKuLJroZQdocfOEh_AAJzEQACSIvxSOAClsQBXCnJMwQ",caption="""
    Node JS darslari | 101-dars | Amaliy mashg'ulot
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIZ2WCgFarp9NxUzRwYwYbIjHEZgFkAAJ0EQACSIvxSEt6Lyp8ZbGRMwQ",caption="""
    Node JS darslari | 102-dars | Loyihaga integration test qo'shamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 103-104 darslar
@node_js_menu_router.message(F.text == "103-104 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIamWCgLj_Lft2IyGh7bluxzbVd3-HAAJ1EQACSIvxSALs9L15HLriMwQ",caption="""
    Node JS darslari | 103-dars | Integration testni takomillashtiramiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIa2WCgLheVwLSPMdMRNCAsqZIv2YYAAJ3EQACSIvxSNNW0TqWg4HZMwQ",caption="""
    Node JS darslari | 104-dars | Parametrli route'larni testlaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 105-106 darslar
@node_js_menu_router.message(F.text == "105-106 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIbmWCgSIdTCYrB7g8eLAOqDlqPnzBAAJ4EQACSIvxSGbdOVDd8Y3UMwQ",caption="""
    Node JS darslari | 105-dars | Yangi toifa qo'shilishini test qilamiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIb2WCgSJZG3ZNBQrsK4rpaSVK324UAAJ5EQACSIvxSLnXyLprKwx8MwQ",caption="""
    Node JS darslari | 106-dars | Code Coverage haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 107-108 darslar
@node_js_menu_router.message(F.text == "107-108 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIcmWCgWxvmQrUiNXI8Y6coXxRCn_aAAJ6EQACSIvxSCGFcFNmz9zzMwQ",caption="""
    Node JS darslari | 107-dars | Deployment haqida
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIc2WCgWxVcUqmC13vqOhuDAQ9VWRhAAJ7EQACSIvxSAJT_Oy3JHMNMwQ",caption="""
    Node JS darslari | 108-dars | Loyihani deploy qilishga tayyorlaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 109-110 darslar
@node_js_menu_router.message(F.text == "109-110 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIdmWCgcU0ugOFS4DGhRXPuf2Z5uYfAAJ8EQACSIvxSC__MQM2wgtmMwQ",caption="""
    Node JS darslari | 109-dars | Heroku bilan ishlashni boshlaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIId2WCgcV7GtmcWf3HMN5JLt6hW3OgAAJ9EQACSIvxSEZtdgohXdFGMwQ",caption="""
    Node JS darslari | 110-dars | Loyihani Herokuga joylaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 111-112 darslar
@node_js_menu_router.message(F.text == "111-112 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIemWCgiRWmhgn8xusZOoGm2f6MbYgAAJ-EQACSIvxSIJz7TW_C-OkMwQ",caption="""
    Node JS darslari | 111-dars | Ma'lumotlar omborini bulutga joylaymiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIe2WCgiT5iSnbmPg5phMgAznVTi1oAAJ_EQACSIvxSMn00G2wAAFLmTME",caption="""
    Node JS darslari | 112-dars | NodeJsda Telegram bot quramiz
\nYoutube —  www.youtube.com/c/FarkhodDadajanov  \nTelegram —   @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")

# 113 darslar
@node_js_menu_router.message(F.text == "113 dars (node js)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIfmWCgl868rpCtnLDke-3cdfmN0L3AAKBEQACSIvxSKQCO81588CCMwQ",caption="""
    Node JS darslari | 113-dars | Nodejsda telegram bot yozamiz (davomi)
\nYoutube —  www.youtube.com/c/FarkhodDadajanov \nTelegram —  @virtualdars
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
 

