from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command


fronend_menu_router: Router = Router()


@fronend_menu_router.message(F.text=="Front-End")
async def start_menu_handler(message: Message):
    
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



# Frontend (intensiv)
@fronend_menu_router.message(F.text=="Frontend (intensiv)")
async def Frontend_intensiv(message: Message):
    intensiv = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="1-2 dars"),
                KeyboardButton(text="3-4 dars"),
            ],
            [
                KeyboardButton(text="5-6 dars"),
                KeyboardButton(text="7-8 dars"),
            ],
            [
                KeyboardButton(text="9-10 dars"),
                KeyboardButton(text="11-12 dars"),
            ],
            [
                KeyboardButton(text="13-14 dars"),
                KeyboardButton(text="15-16 dars"),
            ],
            [
                KeyboardButton(text="17-18 dars"),
                KeyboardButton(text="19-20 dars"),
            ],
            [
                KeyboardButton(text="21-22 dars"),
                KeyboardButton(text="23-24 dars"),
            ],
            [
                KeyboardButton(text="25-26 dars"),
                KeyboardButton(text="27-28 dars"),
            ],
            [
                KeyboardButton(text="29-30 dars"),
                KeyboardButton(text="31-32 dars"),
            ],
            [
                KeyboardButton(text="33-34 dars"),
                KeyboardButton(text="35-36 dars"),
            ],
            [
                KeyboardButton(text="37-37 dars"),
                KeyboardButton(text="39-40 dars"),
            ],
            [
                KeyboardButton(text="🔙 Orqaga"),
                KeyboardButton(text="🔝 Asosiy Menyu"),
            ],
        ],
        resize_keyboard=True
    )

    await message.answer("Frontend (intensiv)", reply_markup=intensiv)

# 1-2 dars
@fronend_menu_router.message(F.text=="1-2 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIDPmV5Cu6IOD_1RORyvtSwd7Vrr2R1AAJTGgACzEo5S8zl4NfcF33jMwQ', caption="""
    📹 Frontend. 1-dars. Kirish 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)
    await message.answer_video("BAACAgIAAxkBAAIDP2V5Cu6GjpN1nFe3g13TjkjUsuBzAAJUGgACzEo5S79tBkKESFrAMwQ", caption="""
    📹 Frontend. 2-dars. Fayllar, html, htmldagi kodni brauzerda ochish, teglar, H1 tegi 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

#  3-4 dars
@fronend_menu_router.message(F.text=="3-4 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAOLZWfpJcGH_pMiXXZxckpTrXt06TwAAlUaAALMSjlLqzFwKHKPOr8zBA', caption="""
    📹 Frontend. 3-dars. Rasm, link, list, sarlavha, paragraf va kichik tegla 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)
    await message.answer_video("BAACAgIAAxkBAAONZWfpLex4Xwo63g0gRuvSDrNwvPQAAuojAAIrwlhKCeLHXwy_gO8zBA", caption="""
    📹 Frontend. 4-dars. Table, form, video, audio, block elementlari

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)


#  5-6 dars
@fronend_menu_router.message(F.text=="5-6 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAOeZWfqW8WRgZOGz9Cw5pfV93a9OiAAAusjAAIrwlhKUhooPLkyGC0zBA', caption="""
    📹 Frontend. 5-dars. Cssga kirish, displeylar va ranglar  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAOgZWfqaDY9n_vsjhqEUQJIv5bUhCcAAu8jAAIrwlhKc2qfHuWAMdkzBA", caption="""
    📹 Frontend. 6-dars. Padding, margin, background image, box sizing, border

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)






#  7-8 dars
@fronend_menu_router.message(F.text=="7-8 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAOlZWfrCTi4a1W_paVCl7jgj_e3MHYAAvAjAAIrwlhKEuPH_7LSq68zBA', caption="""
    📹 Frontend. 7-dars. Fontning stillari va boxlarni joylashtirish bo'yicha qisqa ko'rgazma  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAOnZWfrEDepEUHSPPj8uTcxhLZdBq4AAvEjAAIrwlhKdQ7W6JNwECQzBA", caption="""
    📹 Frontend. 8-dars. Boxlar bilan ishlash, boxlarni joylashtirish, flex 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)



#  9-10 dars
@fronend_menu_router.message(F.text=="9-10 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAOsZWfsL6jGT_LoU7F6bt_Eo44ptiQAAvIjAAIrwlhKuyZduuMHHXszBA', caption="""
    📹 Frontend. 9-dars. Figma bilan tanishish, dizaynlar topish va ularni ko'chirib olish   

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAOuZWfsNnNixlWYP_7_eSytovUkw0AAAvUjAAIrwlhKnxMNFGJSjWMzBA", caption="""
    📹 Frontend. 10-dars. Sodda saytning templateni yasab ko'rish 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)


#  11-12 dars
@fronend_menu_router.message(F.text=="11-12 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAO0ZWfs2xOiaOAbssr2m6t-PwrYMvUAAgIkAAIrwlhK4I0g4MfEAbozBA', caption="""
    📹 Frontend. 11-dars. Psevdo klass va psevdo elementlar    

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAOuZWfsNnNixlWYP_7_eSytovUkw0AAAvUjAAIrwlhKnxMNFGJSjWMzBA", caption="""
    BAACAgIAAxkBAAOzZWfs2-ZGhzxIlSr-IdBD4cTPk74AAvsjAAIrwlhKCilpOLl2z70zBA 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)



#  13-14 dars
@fronend_menu_router.message(F.text=="13-14 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAPuZWghabuPdx_qq-C5QNSbolZXiwgAAgUkAAIrwlhKoyEKdTluvhkzBA', caption="""
    📹 Frontend. 13-dars. Animation va transform    

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAPvZWghaR1713KcL5Aj86r2ED3jXScAAgYkAAIrwlhKH96-Ur08qfQzBA", caption="""
    📹 Frontend.14-dars. Responsive dizayn    

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)




#  15-16 dars
@fronend_menu_router.message(F.text=="15-16 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAP3ZWgjFRqNTmQSG_yDo9ck4Q6oPQcAAjwkAAIrwlhK7iOcafG-WFkzBA', caption="""
    📹 Frontend. 15-dars. Praktika 1-dars  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAP2ZWgjFVWMUBxZ8lJubvX91GaogP4AAtcgAALI8khKi8siXHHM6hQzBA", caption="""
    📹 Frontend. 16-dars. Praktika 2-dars     

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)


#  17-18 dars
@fronend_menu_router.message(F.text=="17-18 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBBmVoJI8IbUp1epfakol3wcXBJvDBAAKqHQAC6d5oSufXQu58ib38MwQ', caption="""
    📹 Frontend. 17-dars. Bootstrap  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBB2VoJI9-foqhRFvTLKj4afPEVgABUAAC8RkAAu3VAAFIreI3bevr6QgzBA", caption="""
    📹 Frontend. 18-dars. Bootstrap grid 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)


#  19-20 dars
@fronend_menu_router.message(F.text=="19-20 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBDWVoJS0MRISBySjnGhSH7Ej9JfzwAALyGQAC7dUAAUjw5ZrU4WCNDjME', caption="""
    📹 Frontend. 19-dars. Javascript kirish  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBDmVoJS0c4n1GBkXZuOPqmlOgG8zdAAIDGgAC7dUAAUhHDAGTPXfiKzME", caption="""
    📹 Frontend. 20-dars. Javascript variable, let, const, var, and arifmetik amallar  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)



#  21-22 dars
@fronend_menu_router.message(F.text=="21-22 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBFGVoJev5d8igP2JNK-Gk56VFI6IzAAIEGgAC7dUAAUhmHz1ZFeT8JTME', caption="""
    📹 Frontend. 21-dars. Ma'lumot turlari 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBFWVoJeucuV3i2RQir4MKTgABs1HX2QACcyMAAnepEEglzzV24sxaKTME", caption="""
    📹 Frontend. 22-dars. Non primiteve tiplar  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)


#  23-24 dars
@fronend_menu_router.message(F.text=="23-24 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBP2VpLmB-sFVIj7XgWIuvN4MiRLPqAAKtHQAC6d5oSgrid0WmvOjmMwQ', caption="""
    📹 Frontend. 23-dars. Shartlar 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBQGVpLmBdbwmmpHSEdRTOcqeFJGWXAAKwHQAC6d5oSmXxgvkNpJbxMwQ", caption="""
    📹 Frontend. 24-dars. Funksiyalar   

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)




#  25-26 dars
@fronend_menu_router.message(F.text=="25-26 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBRmVpLv3ZGkt4pTW_6Dj4Poii0UGQAAIaJAACd6kQSBZFe84MMEq5MwQ', caption="""
    📹 Frontend. 25-dars. Array, iterator va object metodlari

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBR2VpLv1rXRL0feN2mRpxH80YWeKSAAIcJAACd6kQSMFdzl5YGwwdMwQ", caption="""
    📹 Frontend. 26-dars. Dom, elementlarni tanlash    

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)


#  27-28 dars
@fronend_menu_router.message(F.text=="27-28 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBSmVpL2ypKzn_jGE-SR9Om9-tYe3EAAIgJAACd6kQSLnTBjjUHpN_MwQ', caption="""
    📹 Frontend. 27-dars. Classlar bilan ishlash, appendchild, prepend 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBS2VpL2znp6vvBtaaFQj8uwxaMcQ0AAKyHQAC6d5oSgijlICB6dEmMwQ", caption="""
    📹 Frontend. 28-dars. Eventlar bilan ishlash   

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)




#  29-30 dars
@fronend_menu_router.message(F.text=="29-30 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBTmVpL6yp4BI85NyQYORK-XcVU-rLAAK1HQAC6d5oSvljnvXUqCmDMwQ', caption="""
    📹 Frontend. 29-dars. Js Fetch  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBT2VpL6y5EG52GzGzQ9kyS98qHEcNAAK3HQAC6d5oSjDGOzRro0E6MwQ", caption="""
    📹 Frontend. 30-dars. Localstorage    

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

#  31-32 dars
@fronend_menu_router.message(F.text=="31-32 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBUmVpMFRM-XqqkJZz5K5YB5t9DqyoAAK5HQAC6d5oSsub3eI0zmTQMwQ', caption="""
    📹 Frontend. 31-dars. Reactga kirish   

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBU2VpMFRzTkpiItoHZnDlyRpGsFTRAAK6HQAC6d5oSnry4t8Vt3jXMwQ", caption="""
    📹 Frontend. 32-dars. React component, fragment  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

#  33-34 dars
@fronend_menu_router.message(F.text=="33-34 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBYGVpMW2wY3H3PTvaUX_vma1fcRWbAAK7HQAC6d5oSghSfXd3GajaMwQ', caption="""
    📹 Frontend. 33-dars. React, usestate, lifecycle  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBYWVpMW0zMcEE13Ak3tzE1aKpn_8QAAK8HQAC6d5oStKtVfFVzFMIMwQ", caption="""
    📹 Frontend. 34-dars. React useeffect 

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

#  35-36 dars
@fronend_menu_router.message(F.text=="35-36 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBZGVpMcaAOmQVMllQY1LIGLncml_6AAK9HQAC6d5oSgv8kCiItispMwQ', caption="""
    📹 Frontend. 35-dars. React context 
    
    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBZWVpMcYYzqEd9gWCx0Y4FeaVxbFwAAK-HQAC6d5oSj4AAezdG2bN4DME", caption="""
    📹 Frontend. 36-dars. Create react app  

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

#  37-38 dars
@fronend_menu_router.message(F.text=="37-38 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBaGVpMiyXQd6g6hocMsA8puq_J0IOAAIhHgACx3EYSJmVOQ8oUGZgMwQ', caption="""
    📹 Frontend. 37-dars. Create-react-app windowsda o'rnatish 
    
    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBaWVpMixlu3o3L39MNnikDmniqTwwAAIqHgACx3EYSLKiB3fHH5eiMwQ", caption="""
    📹 Frontend. 38-dars. React router DOM   

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)



#  39-40 dars
@fronend_menu_router.message(F.text=="39-40 dars")
async def one_two(message: Message):
    await message.answer_video('BAACAgIAAxkBAAIBbGVpMqMjxyqY-F902LG1gdoTsZ1UAAIsHgACx3EYSPEHOkfxQr5LMwQ', caption="""
    📹 Frontend. 39-dars. Github  
    
    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)

    await message.answer_video("BAACAgIAAxkBAAIBbWVpMqMxyfC5Z89s9gfjybQPGDoeAAI_HgACx3EYSOoWmBHOShcbMwQ", caption="""
    📹 Frontend. 40-dars. Deploying

    \nMilliy ta'lim resurslari youtube kanali:
👉 bit.ly/3EJqH7e

    \n@MilliyTalimResursBot — yaqinlarga ulashing!
    """)



# orqaga

@fronend_menu_router.message(F.text=="🔙 Orqaga")
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

@fronend_menu_router.message(F.text=="🔝 Asosiy Menyu")
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
