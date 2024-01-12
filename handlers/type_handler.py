from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.type_menu import type_menu
type_menu_router: Router = Router()


@type_menu_router.message(F.text == "TypeScript darslari")
async def handler(message: Message):
    await message.answer("TypeScript darslari",reply_markup=type_menu)




# 1-2 darslar
@type_menu_router.message(F.text == "1-2 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGR2V7tOVcSkxXGTxZIpdLP3093BbUAAKiFwACeuDQS6-lOTA-tlEhMwQ",caption="""
    TypeScript darslari | 1-dars | Kirish
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGSGV7tOXrY3JLcl3WInrc-DppWApQAALVFwACeuDQSyYSBKxnVNrRMwQ",caption="""
    TypeScript darslari | 2-dars | TypeScript darslari ma'lumot
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 3-4 darslar
@type_menu_router.message(F.text == "3-4 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGS2V7tYs15TxTM_GGlkspWgGeLKsbAALWFwACeuDQS63x0d7o1ltdMwQ",caption="""
    TypeScript darslari | 3-dars | TypeScript darslari yo'l xarita
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGTGV7tYvZDOD4au32Jur-qSguWNS-AALXFwACeuDQSx-DkETnUwUmMwQ",caption="""
    TypeScript darslari | 4-dars | TypeScript darslari dastur holat
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    


# 5-6 darslar
@type_menu_router.message(F.text == "5-6 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGT2V7teSu1JX8LqiNAtm1MKvdt8VaAALYFwACeuDQS2EAAcz-wO2xCTME",caption="""
    TypeScript darslari | 5-dars | TypeScript darslari Interface
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGUGV7teQ05vNMDYtl6Wu6o-WKL2x7AALaFwACeuDQS4jE-IiA7A0DMwQ",caption="""
    TypeScript darslari | 6-dars | TypeScript darslari xatolarni ko'rsatish
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 7-8 darslar
@type_menu_router.message(F.text == "7-8 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGV2V7tlnH5c0_Hx-EmQG9ffTjRex9AALcFwACeuDQS7oYEfX2fmsSMwQ",caption="""
    TypeScript darslari | 7-dars | TypeScript darslari type nima
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGWGV7tlnSkgJ_S1t2gMP5SuFeOv9kAALeFwACeuDQS0f_f6_MnIwaMwQ",caption="""
    TypeScript darslari | 8-dars | TypeScript darslari annotation & interface
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 9-10 darslar
@type_menu_router.message(F.text == "9-10 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGW2V7tqsAAQ1ZmHslAw6ld7CJMR-aOwAC4BcAAnrg0EtcI24pN_KHNjME",caption="""
    TypeScript darslari | 9-dars | TypeScript darslari type annotations, Array, Object, Function
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGXGV7tqtowytWOmPkfw5MLPs3bpymAALkFwACeuDQSyQ6KVSwJILrMwQ",caption="""
    TypeScript darslari | 10-dars | TypeScript darslari ANY nima
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 11-12 darslar
@type_menu_router.message(F.text == "11-12 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGX2V7tvkyMfl1I5XhCNK06sVHE9xpAALmFwACeuDQS4q4JEjH6BiiMwQ",caption="""
    TypeScript darslari | 11-dars | TypeScript darslari keraklik joyda ishlatish ANY
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGYGV7tvkuWclvscKDrlqMiexwjV7gAALnFwACeuDQSwx84z87tElHMwQ",caption="""
    TypeScript darslari | 12-dars | TypeScript darslari annotations of function
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 13-14 darslar
@type_menu_router.message(F.text == "13-14 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGY2V7t0177xt-ar3B1XjxOpMFsm1dAALoFwACeuDQS6U040rWccKFMwQ",caption="""
    TypeScript darslari | 13-dars | TypeScript darslari Distruksiya
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGZGV7t01YbHP-AvAaZKUeEvWmD9puAALqFwACeuDQS5A_iI0SJoqIMwQ",caption="""
    TypeScript darslari | 14-dars | TypeScript darslari annotations of array
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 15-16 darslar
@type_menu_router.message(F.text == "15-16 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGZ2V7t50X5s4fSwVojAL-fbqjMnZpAALrFwACeuDQSz-wdViFAvGsMwQ",caption="""
    TypeScript darslari | 15-dars | TypeScript darslari Tuples
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGaGV7t50f6QxBGI0GM-KMKA4KXg3OAALtFwACeuDQS1MlNLSB1gABDTME",caption="""
    TypeScript darslari | 16-dars | TypeScript darslari Interface nima
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    
    

# 17-18 darslar
@type_menu_router.message(F.text == "17-18 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGa2V7t-7cS7PHbsE_Rq-fvpt5Q6kPAALuFwACeuDQS4NVpo9cSHqQMwQ",caption="""
    TypeScript darslari | 17-dars | TypeScript darslari Interface class
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGbGV7t-7_XKUT1Qh25cDFxkHoR3XcAALxFwACeuDQS-C09qeS_p7ZMwQ",caption="""
    TypeScript darslari | 18-dars | TypeScript darslari Parcell & Faker
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    
    

# 19-20 darslar
@type_menu_router.message(F.text == "19-20 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGb2V7uFm4JzHC25PEMPbOaN55uOgMAALzFwACeuDQS8GBg1L8t2sTMwQ",caption="""
    TypeScript darslari | 19-dars | TypeScript darslari Google Map API
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGcGV7uFnrpFUPxb_4DLUujA3QR-TjAAL0FwACeuDQS3nsp1Ek_xvQMwQ",caption="""
    TypeScript darslari | 20-dars | TypeScript darslari Config Type Map
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    
    

# 21-22 darslar
@type_menu_router.message(F.text == "21-22 dars (type script)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIGc2V7uLveM5sGb14G61KQOqFYtdQRAAL1FwACeuDQS_N1P_vDF1TFMwQ",caption="""
    TypeScript darslari | 21-dars | TypeScript darslari Funktsional Qo'shish
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIGdGV7uLv5sSTrAAG8WmEQdo1c844nawAC9hcAAnrg0Etw-WuVqwwcyTME",caption="""
    TypeScript darslari | 22-dars | TypeScript darslari InfoWindow
\nYoutube —  www.youtube.com/c/SamarBadriddinov  \nTelegram —   @samarbadriddinov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
