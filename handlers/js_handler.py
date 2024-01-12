from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.js_menu import js_menu, jquery_menu
js_menu_router: Router = Router()


@js_menu_router.message(F.text == "JavaScript darslari")
async def js(message: Message):
    await message.answer("JavaScript darslari", reply_markup=js_menu)

# 1-2 darslar
@js_menu_router.message(F.text == "1-2 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIElmV539PSkUXSyixASXeDL4JPch67AALhEwACQtoZSKNY_oQYch0-MwQ",caption="""
    JavaScript darslari | 1-qism | O'zgaruvchilar
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEl2V539Mj-Mpiwwj71BmP3V_UDD65AALiEwACQtoZSGQmOLlymRMLMwQ",caption="""
    JavaScript darslari | 2-qism | Primitive turlar
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 3-4 darslar
@js_menu_router.message(F.text == "3-4 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEn2V6T-O6Mi4kK7lJ4knqv2zvx2ABAALlEwACQtoZSGOX4QcdXwLAMwQ",caption="""
    JavaScript darslari | 3-qism | Object
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEoGV6T-OwlYyUXJuBVDdc-t93q6hmAALmEwACQtoZSA69UIKlSXAEMwQ",caption="""
    JavaScript darslari | 4-qism | Array
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 5-6 darslar
@js_menu_router.message(F.text == "5-6 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEo2V6UFq_-9N4NAHzfOs8UxD0-oCNAALoEwACQtoZSGCDm2ttZmf6MwQ",caption="""
    JavaScript darslari | 5-qism | Function
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEpGV6UFpl5dSoizcvoxlfB6uUd-6-AALpEwACQtoZSK7J9jIFlvaZMwQ",caption="""
    JavaScript darslari | 6-qism | Arifmetik operatorlar
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 7-8 darslar
@js_menu_router.message(F.text == "7-8 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEp2V6ULpuTsf409TiAAFDEM3VfGjHngAC6hMAAkLaGUg1M70UMMlp5jME",caption="""
    JavaScript darslari | 7-qism | Solishtiruv va tenglik operatorlari
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEqGV6ULrrx0KL2i11VNA5--WI9t3KAALrEwACQtoZSMnevRgeMuDFMwQ",caption="""
    JavaScript darslari | 8-qism | Ternary operatori
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 9-10 darslar
@js_menu_router.message(F.text == "9-10 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEq2V6UV_8tzsRtbXJMNgEJ38wCZgIAALuEwACQtoZSJziiVnS2gb-MwQ",caption="""
    JavaScript darslari | 9-qism | TBoolean algebra, mantiqiy hamda bitwise operatorlari
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIErGV6UV92OCwgE5NuaYTgY7tD2I1sAALvEwACQtoZSEPhyIm9jLchMwQ",caption="""
    JavaScript darslari | 10-qism | If else
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 11-12 darslar
@js_menu_router.message(F.text == "11-12 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEr2V6UohehmF2NpUdn_pOlHBt8Ml6AALwEwACQtoZSNaebfD-U0lYMwQ",caption="""
    JavaScript darslari | 11-qism | Switch case
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEsGV6UogmGn9VC7QKsL_0tXrNqb8OAALxEwACQtoZSGfYD7V_i3fUMwQ",caption="""
    JavaScript darslari | 12-qism | For loop
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 13-14 darslar
@js_menu_router.message(F.text == "13-14 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEs2V6UuzqIzDIlxsCl_1Q2owqdj-5AALyEwACQtoZSKJ17ppqw93XMwQ",caption="""
    JavaScript darslari | 13-qism | While, do while
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEtGV6Uuxjq-ga6A7PWLCdiIElqggoAALzEwACQtoZSBlWHGCI2r8XMwQ",caption="""
    JavaScript darslari | 14-qism | Break, continue
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 15-16 darslar
@js_menu_router.message(F.text == "15-16 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEt2V6UzFUoLY0qpinuf8V90iWDP41AAL1EwACQtoZSEM5NvjePt8HMwQ",caption="""
    JavaScript darslari | 15-qism | For in, for of
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEuGV6UzFyM2MYiSOggcs1ZQfPmAS-AAL2EwACQtoZSNxt9jrpyUw0MwQ",caption="""
    JavaScript darslari | 16-qism | Fizzbuzz
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 17-18 darslar
@js_menu_router.message(F.text == "17-18 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEu2V6U7MofLXGHHuOKz546Wa4boq8AAL3EwACQtoZSKhXEJa3igABJjME",caption="""
    JavaScript darslari | 17-qism | Factory function
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEvGV6U7MIkXyjrVm1aEYb1QhcvCymAAL4EwACQtoZSK4mIis2yPylMwQ",caption="""
    JavaScript darslari | 18-qism | Constructor function
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 19-20 darslar
@js_menu_router.message(F.text == "19-20 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEv2V6VER7aXe61sRRs5P56qKf_JtbAAL7EwACQtoZSLhMAu4VMtUMMwQ",caption="""
    JavaScript darslari | 19-qism | Constructor xossasi
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEwGV6VES9gsMQcLQ8SmGFw44dgreBAAL8EwACQtoZSErsrTYweEcEMwQ",caption="""
    JavaScript darslari | 20-qism | Function ham object
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 21-22 darslar
@js_menu_router.message(F.text == "21-22 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEw2V6VJQmG7dRhyMEptZDePn21uHKAAL9EwACQtoZSF5LIDxPBqNJMwQ",caption="""
    JavaScript darslari | 21-qism | Primitive va reference turlar
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIExGV6VJTEgl4R9eIoyb_ckJeQTaOHAAL-EwACQtoZSJGMuZGGZINdMwQ",caption="""
    JavaScript darslari | 22-qism | Object keys
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 23-24 darslar
@js_menu_router.message(F.text == "23-24 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE32V6VRFMF4FBSRJfjY37UYbDagz3AAL_EwACQtoZSBLfw97RNNJ-MwQ",caption="""
    JavaScript darslari | 23-qism | Object'dan klon olish
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE4GV6VRHcqvGdwTSoXAWEc_USX6-UAAMUAAJC2hlIhH--ny_KVVAzBA",caption="""
    JavaScript darslari | 24-qism | Math
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    
    

# 25-26 darslar
@js_menu_router.message(F.text == "25-26 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE42V6VXD937oYP_-UDlE9bsS33Nu7AAICFAACQtoZSBKRi9yOFkZ5MwQ",caption="""
    JavaScript darslari | 25-qism | String
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE5GV6VXAllDmz2BS8BCwVS3iXEhdjAAIEFAACQtoZSKj9w7fyyxwkMwQ",caption="""
    JavaScript darslari | 26-qism | Array'ga element qo'shish, uni o'chirish va izlash
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    
    

# 27-28 darslar
@js_menu_router.message(F.text == "27-28 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE42V6VXD937oYP_-UDlE9bsS33Nu7AAICFAACQtoZSBKRi9yOFkZ5MwQ",caption="""
    JavaScript darslari | 25-qism | String
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE5GV6VXAllDmz2BS8BCwVS3iXEhdjAAIEFAACQtoZSKj9w7fyyxwkMwQ",caption="""
    JavaScript darslari | 26-qism | Array'ga element qo'shish, uni o'chirish va izlash
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 29-30 darslar
@js_menu_router.message(F.text == "29-30 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE52V6VjI55NN-0c0UfsNI1LRA2XiAAAIIFAACQtoZSPN--FCzYxeCMwQ",caption="""
    JavaScript darslari | 29-qism | Array'ning map, forEach metodlari va metodlarni ketma-ket
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE6GV6VjK4apFeZowMxIOFetKEMg2JAAIKFAACQtoZSGAMhsluR8rOMwQ",caption="""
    JavaScript darslari | 30-qism | Array'ning reduce metodi
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 31-32 darslar
@js_menu_router.message(F.text == "31-32 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE62V6VpjdAzfNFbSeQk8_GxJ5aS6ZAAILFAACQtoZSDbDjaZ8U1vfMwQ",caption="""
    JavaScript darslari | 31-qism | Function e'lon qilish usullari
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE7GV6VpjZgtW2ZeBZVzPly9WsVsZMAAIMFAACQtoZSNXuqHs2I_0jMwQ",caption="""
    JavaScript darslari | 32-qism | Spread operator va rest parameter
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 33-34 darslar
@js_menu_router.message(F.text == "33-34 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE72V6Vwj8Yll532P3NKv0Eo_HXTBLAAINFAACQtoZSJcsE1wiS_DBMwQ",caption="""
    JavaScript darslari | 33-qism | Getter va setter
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE8GV6Vwj0mLB_bcq9iEVWyBDUidzdAAIOFAACQtoZSL9YdXJZ0oYHMwQ",caption="""
    JavaScript darslari | 34-qism | Try catch
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 35-36 darslar
@js_menu_router.message(F.text == "35-36 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE82V6V2ceNyJsvVE-fM0DFj4TNENoAAIPFAACQtoZSJ-HomdpPpTzMwQ",caption="""
    JavaScript darslari | 35-qism | Global scope va local scope
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE9GV6V2e8nEHsg9Ib1d8xCnhxiYSUAAIQFAACQtoZSIQ0MrPeTIriMwQ",caption="""
    JavaScript darslari | 36-qism | let bilan var'ning bir-biridan asosiy farqlari
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 37-38 darslar
@js_menu_router.message(F.text == "37-38 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE92V6V7444tmH7C1GAe7xPvkTLYI1AAIRFAACQtoZSHM3e6ZzmMioMwQ",caption="""
    JavaScript darslari | 37-qism | This
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE-GV6V7604jVXjfdtnvQcVqXvic6NAAISFAACQtoZSOv4hROuPq43MwQ",caption="""
    JavaScript darslari | 38-qism | Promise
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 39-40 darslar
@js_menu_router.message(F.text == "39-40 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE-2V6WBcHS-vq8dnppm7ZQF9Nm4zjAAIUFAACQtoZSPgyCHR8RRF-MwQ",caption="""
    JavaScript darslari | 39-qism | DOM
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIE_GV6WBfaME1wGQtu6WVU76j2keDwAAIVFAACQtoZSO3NpdravmzFMwQ",caption="""
    JavaScript darslari | 40-qism | Callback
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
# 41 darslar
@js_menu_router.message(F.text == "41 dars (JS)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIE_2V6WIr2qmV8EdQ_ZCqkf-5Pm0XbAAIWFAACQtoZSPP2soZZsTotMwQ",caption="""
    JavaScript darslari | 41-qism | Async await
\nYoutube —  www.youtube.com/c/UsmonMasudjonov  \nTelegram —  @usmon_masudjonov
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# jquery darslik uchun 
@js_menu_router.message(F.text == "jQuery darslari")
async def jqury(message: Message):
    await message.answer("jQuery darslari", reply_markup=jquery_menu)


# 39-40 darslar
@js_menu_router.message(F.text == "1-2 dars (jquery)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIFEWV6Wq5Gs4Rv4Fvw0kw3RMd3rMzeAALsEgACBeM5SAgqrsJQdKtVMwQ",caption="""
    jQuery darslari | 1-dars
\nYoutube —  https://bit.ly/3QEPtIx  \nTelegram —   ❌
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIFEmV6Wq63LsLB4Uvmk75KcaHykFTcAALuEgACBeM5SDqoeQzi99PTMwQ",caption="""
    jQuery darslari | 2-dars
\nYoutube —  https://bit.ly/3QEPtIx  \nTelegram —   ❌
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    