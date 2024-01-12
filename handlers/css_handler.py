from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.css import css_menu, scss

css_menu_router: Router = Router()

@css_menu_router.message(F.text == "CSS darslari")
async def css_handler(message: Message):
    await message.answer("CSS darslari",reply_markup=css_menu)



# 1-2 dars
@css_menu_router.message(F.text == "1-2 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDg2V5D8tDUzMZ0jPq-fCDoxk9AAGdVwAC-RMAAgXjOUhSonCJoafZSDME",caption="""
    CSS darslari | 1-dars | CSS Asoslari
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDhGV5D8uKeu_roUy0L24Pfg1G7P__AAL6EwACBeM5SCVSZblvkn4XMwQ",caption="""
    CSS darslari | 2-dars | CSS Fonlar
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)




# 3-4 dars
@css_menu_router.message(F.text == "3-4 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDimV5Ec_BCwVsxNNF5byrODvkbSnmAAL7EwACBeM5SKWLkkLBaLGcMwQ",caption="""
    CSS darslari | 3-dars | CSS Border
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDi2V5Ec9ujo8Ox9cWyHuJOiW1xD_zAAL8EwACBeM5SJ7o7xRMyjdSMwQ",caption="""
    CSS darslari | 4-dars | CSS Margin , Padding, Width, Height
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)


# 5-6 dars
@css_menu_router.message(F.text == "5-6 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDkWV5Ekif03Y3v6qIfwbWtL4wzalsAAL9EwACBeM5SC4Oevih_KT5MwQ",caption="""
    CSS darslari | 5-dars | CSS Font
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDkmV5EkglmSJQ-dZPKVMn0sYLqk4AA_4TAAIF4zlIjDIbvgKHSsAzBA",caption="""
    CSS darslari | 6-dars | Display
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)



# 7-8 dars
@css_menu_router.message(F.text == "7-8 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDn2V5NARR_GI3ycov1Y1iEX0t3wdJAAMUAAIF4zlI3r1KbJsuyO0zBA",caption="""
    CSS darslari | 7-dars | Position haqida
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDoGV5NATRqXSmMs6UM5n71fH-Q7IqAAIBFAACBeM5SPT9PX0eN-jBMwQ",caption="""
    CSS darslari | 8-dars | Table
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

 


# 9-10 dars
@css_menu_router.message(F.text == "9-10 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDo2V5NMmy4pf__nFpKagXy3wVhKIOAAICFAACBeM5SP9kWv01CUNxMwQ",caption="""
    CSS darslari | 9-dars | Float & Layout
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDpGV5NMkMzyX6V3_tadIKgzngvCcqAAIDFAACBeM5SCiOzmBEKiV9MwQ",caption="""
    CSS darslari | 10-dars | Float workshop
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

 


# 11-12 dars
@css_menu_router.message(F.text == "11-12 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDp2V5NWHnN80K7zajnB5X7baYrktPAAIEFAACBeM5SGuhQdvQ-M64MwQ",caption="""
    CSS darslari | 11-dars | Outline
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDqGV5NWHN2GzVfKsjeicTlgwSey-7AAIFFAACBeM5SOK_ZSVgxnZAMwQ",caption="""
    CSS darslari | 12-dars | Text
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)


# 13-14 dars
@css_menu_router.message(F.text == "13-14 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDq2V5NdNMhrl_VWY3Kr65df-EqtHSAAIGFAACBeM5SCcLfMmF7ZyZMwQ",caption="""
    CSS darslari | 13-dars | Icons
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDrGV5NdMoRlPPyjQ0HeBSSzGi_je7AAIHFAACBeM5SL2o1hFN8aOeMwQ",caption="""
    CSS darslari | 14-dars | Selectors
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

 

# 15-16 dars
@css_menu_router.message(F.text == "15-16 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDxGV5NpE2w_zHoTorZkvsuSlpX-mmAAIJFAACBeM5SM51CFgadwXQMwQ",caption="""
    CSS darslari | 15-dars | Selector 2 - Pseudo class
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDxWV5NpHV_38Hr3nEOOXcZnCJizA8AAILFAACBeM5SJ_ueYILODvVMwQ",caption="""
    CSS darslari | 16-dars | Selector 3 - Pseudo class
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

 
 

# 17-18 dars
@css_menu_router.message(F.text == "17-18 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIDy2V5N7VdXZePoW2J6lnCQVHiM_nxAAIMFAACBeM5SGbnEm5mWyRjMwQ",caption="""
    CSS darslari | 15-dars | Selector 2 - Pseudo class
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAIDyWV5N2-XZh3vEnNAD-Hv04JT_z6rAAINFAACBeM5SI4Q3xMvXvkmMwQ",caption="""
    CSS darslari | 18-dars | Gradientlar
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

 
 

# 19-20 dars
@css_menu_router.message(F.text == "19-20 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAID0GV5OVsoNDJ4MvX6OEOkjcQ9bV74AAIPFAACBeM5SNU9stTyLsNNMwQ",caption="""
    CSS darslari | 19-dars | Maxsus Font yuklash
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAID0WV5OVu-Erl-vcz9NHS59xeh3IiHAAIQFAACBeM5SPXoj8th1i9aMwQ",caption="""
    CSS darslari | 20-dars | Animation
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

 
 

# 21-22 dars
@css_menu_router.message(F.text == "21-22 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAID1GV5Odf5Qn_frhtdVGJOEktabi8mAAIRFAACBeM5SI3oJagKkfqoMwQ",caption="""
    CSS darslari | 21-dars | Column
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAID1WV5OdfIOSSRTDyLozD2oCcxoPFCAAISFAACBeM5SEQBdAKjikMCMwQ",caption="""
    CSS darslari | 22-dars | Flexbox
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

 
 

# 23-24 dars
@css_menu_router.message(F.text == "23-24 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAID2GV5OkK57hrl8UrPPWRWIupSe6CyAAITFAACBeM5SOJ_7NsKsmLrMwQ",caption="""
    CSS darslari | 23-dars | Flexbox 2
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

    await messege.answer_video("BAACAgIAAxkBAAID2WV5OkJUZrCbzfUbv5VK7d1to6-hAAIUFAACBeM5SF5V9lAVuj-CMwQ",caption="""
    CSS darslari | 24-dars | Navbar - Workshop
\nYoutube — www.youtube.com/c/Alitechacademy \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

 
 

# 25 dars
@css_menu_router.message(F.text == "25 dars (CSS)")
async def bir_ikki(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAID3GV5OwQDAQywuhtSe40xJ7oyS72WAAIVFAACBeM5SHtBGCvPiexBMwQ",caption="""
    CSS darslari | 25-dars | Responsive - Moslashuvchan dizayn
\nYoutube — www.youtube.com/c/Alitechacademy  \nTelegram — @alitechuz

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

# SCSS UCHUN DARSLIK

@css_menu_router.message(F.text == "Sass darslari")
async def SCSS_darslik(message: Message):
    await message.answer("Sass darslari", reply_markup=scss)


@css_menu_router.message(F.text == "1-1 dars")
async def one_one(messege: Message):
    await messege.answer_video("BAACAgIAAxkBAAIEImV5mEh8QgWfJ2VBo5cAAZhZTs9vYAAChRMAAsIEMUhvcEzZDPS3LzME",caption="""
    Sass darslari | To'liq | Barcha ma'lumotlar
\nYoutube — www.youtube.com/channel/UCinSYLW9PnY1cW3nHCRwcBw/videos  \nTelegram — ❌

\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
    """)

# orqaga

@css_menu_router.message(F.text=="🔙 Orqaga")
async def FrontOrBeck(message: Message):

    menu_frontd = ReplyKeyboardMarkup(
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
    await message.answer("Ozingizga ma'qul bo'lgan yonalishni tanlang tanglang 😊", reply_markup=menu_frontd)



# assosiy menu 

@css_menu_router.message(F.text=="🔝 Asosiy Menyu")
async def orqaga_handler(message: Message):
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Darslarni boshlash 💻")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(f"""Assalomu aleykum 
        \nYangicha formatdagi platformaga xush kelibsiz! Tartiblangan va yangi darslar sizni kutmoqda. Quyidagi tugmani bosing👇
            
    """, reply_markup=menu)

 