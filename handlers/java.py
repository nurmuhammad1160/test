from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.nodejs_menu import nodejs_menu
from keyboards.java_menu import java_menu

java_menu_router: Router = Router()

@java_menu_router.message(F.text== "Java darslari")
async def java(message: Message):
    await message.answer("Java darslari",reply_markup=java_menu)



# 1-2 darslar
@java_menu_router.message(F.text == "1-2 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIn2WCiFjB1IXJ9MyBfIL3BDYwqR28AAJjEwACPCgQSWRfFWWhwd40MwQ",caption="""
    Java (Beginner) darslari | 1-dars | Istalling the JDK,Downloading Eclipse, Hello Java
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIoGWCiFj4kg6loEV5jl3hU1xNXAtnAAJkEwACPCgQSVjSVZZWVumWMwQ",caption="""
    Java (Beginner) darslari | 2-dars | Variables
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 3-4 darslar
@java_menu_router.message(F.text == "3-4 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIqGWCkmNuWKekD5fxqP3lL4k2Is6VAAJlEwACPCgQSaPFSy41CSrcMwQ",caption="""
    Java (Beginner) darslari | 3-dars | Promotion and Casting
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIqWWCkmOHgYuOaInVdRsbv4B1I0shAAJmEwACPCgQSfUbf83t2SguMwQ",caption="""
    Java (Beginner) darslari | 4-dars | Wrapper Class and Initialization
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 5-6 darslar
@java_menu_router.message(F.text == "5-6 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIrGWCkq5yP0JafuPa05cXv7bboQ2iAAJnEwACPCgQSUmqScvSv-8NMwQ",caption="""
    Java (Beginner) darslari | 5-dars | Class and Console Print
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIrWWCkq5tPsWteWlHRRGeIQk3djV0AAJoEwACPCgQSS09UfmF4yoYMwQ",caption="""
    Java (Beginner) darslari | 6-dars | Keyboard Input
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 7-8 darslar
@java_menu_router.message(F.text == "7-8 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIsGWCkwOJqbT8ldHa7Z7GPHr0QKzAAAJpEwACPCgQSVqucRSdW3XjMwQ",caption="""
    Java (Beginner) darslari | 7-dars | If Statement
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIsWWCkwPP_kdS170LL6e12wgFmXVAAAJqEwACPCgQSZaie_YL9tqsMwQ",caption="""
    Java (Beginner) darslari | 9-dars | for break,continue,label
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 9-10 darslar
@java_menu_router.message(F.text == "9-10 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIItGWCk5HRDi-cJdGS9COCpaTUz3jMAAJrEwACPCgQSSGeqf6xqsfmMwQ",caption="""
    Java (Beginner) darslari | 9-dars | while, do_while
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIItWWCk5GTHkWsLUDQOAjsNHUvGRQKAAJsEwACPCgQSb7ur9RofZKrMwQ",caption="""
    Java (Beginner) darslari | 10-dars | method
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 11-12 darslar
@java_menu_router.message(F.text == "11-12 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIvGWClDdhIIlxOGeJaA2Y0cPp4WToAAJtEwACPCgQSTuSEFBUChMZMwQ",caption="""
    Java (Beginner) darslari | 11-dars | return Method
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIvWWClDfxFNBvlo9RCnKPpCxK_MK3AAJuEwACPCgQSf6Sm6tjGJYAATME",caption="""
    Java (Beginner) darslari | 12-dars | Array
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 13-14 darslar
@java_menu_router.message(F.text == "13-14 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIwGWClLR57-I5vvQ17Y3C3D8q-rzJAAJwEwACPCgQSRK_Jt084_R5MwQ",caption="""
    Java (Beginner) darslari | 13-dars | Enhanced for Loop
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIwWWClLQnuUdyuNKCPmp2tEXR-KwYAAJxEwACPCgQSYWGrlFgu1OaMwQ",caption="""
    Java (Beginner) darslari | 14-dars | Arrays in Methods
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 15-16 darslar
@java_menu_router.message(F.text == "15-16 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIxGWClRcNl9wb8Nwrfmo69VKJVfVmAAJyEwACPCgQScO8ajB9_zTpMwQ",caption="""
    Java (Beginner) darslari | 15-dars | Multidimensional Arrays
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIxWWClRew30shvNxEUUR-kzRDeAhuAAJzEwACPCgQSd1NjfVQgthBMwQ",caption="""
    Java (Beginner) darslari | 16-dars | Variable Length Arguments
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 17-18 darslar
@java_menu_router.message(F.text == "17-18 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIyGWClYfp7RgedgO0nYznHz4EjAM-AAJ0EwACPCgQSagY9U1Ik2COMwQ",caption="""
    Java (Beginner) darslari | 17-dars | Class Introduction
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIyWWClYdnxPTRFjiO72WIdbtgXav_AAJ1EwACPCgQSY67SRzBWOYOMwQ",caption="""
    Java (Beginner) darslari | 18-dars | Constructor and Overloading
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 19-20 darslar
@java_menu_router.message(F.text == "19-20 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIIzGWCle9vE3RhPExbEuLlM__WYtx3AAJ2EwACPCgQSctyqo2Bxq6oMwQ",caption="""
    Java (Beginner) darslari | 19-dars | Constructor and Overloading
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIIzWWCle9_HAsrUke1impKRfVNQy_fAAJ3EwACPCgQSXkUjt8vF-HWMwQ",caption="""
    Java (Beginner) darslari | 20-dars | this and this()
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 21-22 darslar
@java_menu_router.message(F.text == "21-22 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJaGWOkwE3_u_KsZl2qqi3JMOHPFlCAAJ4EwACPCgQSa-JLtDtAbxnNAQ",caption="""
    Java (Beginner) darslari | 21-dars | Garbage Collector
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJaWWOkwEpn1D1I_f_yH4V8LFo58QZAAJ5EwACPCgQSeOlk_bwbnYVNAQ",caption="""
    Java (Beginner) darslari | 22-dars | private, public, protected, package
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 23-24 darslar
@java_menu_router.message(F.text == "23-24 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJbGWOk52R3I1m3OerMiUMbHmvkPXEAAJ6EwACPCgQSSXByFlqEmRcNAQ",caption="""
    Java (Beginner) darslari | 23-dars | Getter, Setter(Encapsulation)
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJbWWOk52AJC098_A1GB3gVvX1IYAHAAJ7EwACPCgQSQJGYliQ2i4pNAQ",caption="""
    Java (Beginner) darslari | 24-dars | Static
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 25-26 darslar
@java_menu_router.message(F.text == "25-26 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJcGWOlAY95EvWi4fAAhNKuL8Mdq6mAAJ8EwACPCgQSfgx_r2r_HoINAQ",caption="""
    Java (Beginner) darslari | 25-dars | Inner Class
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJcWWOlAbACKEyJ9EsKeH0RTvAIyyzAAJ9EwACPCgQSTm7mXfYEsARNAQ",caption="""
    Java (Beginner) darslari | 26-dars | static Inner Class
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")


# 27-28 darslar
@java_menu_router.message(F.text == "27-28 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJemWP4Fwooq-DhsolEer7dQODtqKRAAJ-EwACPCgQSVyhMO1rpPlaNAQ",caption="""
    Java (Beginner) darslari | 27-dars | Local Inner Class
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJe2WP4FxLmT9AtbgZLsTT_sp-Ial4AAJ_EwACPCgQSVkwLwoOPXF8NAQ",caption="""
    Java (Beginner) darslari | 28-dars | anonymous Inner Class
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")

# 29-30 darslar
@java_menu_router.message(F.text == "29-30 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJfmWP4LVhhkg4dGzuGVZYN3i_n7lxAAKAEwACPCgQSSeOj5EU1F7hNAQ",caption="""
    Java (Beginner) darslari | 29-dars | Inheritance (extends Object and Classes)
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJf2WP4LW-eF0lH3O96ct5_ddjvJLNAAKBEwACPCgQSay-KRL8kzxtNAQ",caption="""
    Java (Beginner) darslari | 30-dars | this and super Methods
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")

# 31-32 darslar
@java_menu_router.message(F.text == "31-32 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJgmWP4a00Q8QJErQ_0fM9Ml5pn9MdAAKDEwACPCgQSTpt8984dGe0NAQ",caption="""
    Java (Beginner) darslari | 31-dars | this and super with Variables
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJg2WP4a0DcKP_CdLTXuC42SFFeeh-AAKEEwACPCgQSSWq818JUCDZNAQ",caption="""
    Java (Beginner) darslari | 32-dars | Overriding
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 33-34 darslar
@java_menu_router.message(F.text == "33-34 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJhmWP4iL-gNec1L1BOXkb4sCmlwwXAAKFEwACPCgQSWf9Vab-vgk2NAQ",caption="""
    Java (Beginner) darslari | 33-dars | Abstraction
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJh2WP4iLvwqXBe0_T3e6tIH-F4ZUZAAKGEwACPCgQSeClTc0j-uFkNAQ",caption="""
    Java (Beginner) darslari | 34-dars | Interfaces
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")





# 35-36 darslar
@java_menu_router.message(F.text == "35-36 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJimWP4orNlHhfwkeKftDroyort38BAAKHEwACPCgQSaHc6hkLzCQWNAQ",caption="""
    Java (Beginner) darslari | 35-dars | Thread
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJi2WP4oo3nBzLj-69RaXFIghPYKk9AAKJEwACPCgQSeE_u7L8Q32yNAQ",caption="""
    Java (Beginner) darslari | 36-dars | Thread APIs
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")






# 37-38 darslar
@java_menu_router.message(F.text == "37-38 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJjmWP4vJYljiThukj9VJBbbYY2APcAAKKEwACPCgQSW8oioZesr-DNAQ",caption="""
    Java (Beginner) darslari | 37-dars | Thread Synchronization
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJj2WP4vKAkNw-jBklNnoMF0WSmRQ9AAKLEwACPCgQSVqSt_XSbm5DNAQ",caption="""
    Java (Beginner) darslari | 38-dars | Exception, try_catch_final, throw
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")




# 39-40 darslar
@java_menu_router.message(F.text == "39-40 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJkmWP456KZOkIBajSxIrZuDyF1wHiAAKMEwACPCgQSTJ8c2m0rnIeNAQ",caption="""
    Java (Beginner) darslari | 39-dars | Set, Map HashSet, Hashtable, HashMap
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJk2WP454YckSnD2A5Zj9WWjlcW14aAAKOEwACPCgQSeWzdXeeBS6hNAQ",caption="""
    Java (Beginner) darslari | 40-dars | List, ArrayList, instanceof
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")





# 41-42 darslar
@java_menu_router.message(F.text == "41-42 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJlmWP4_wUTu4f5jBtG-BJy2uD8IRQAAKQEwACPCgQSWLGcE3oaiVPNAQ",caption="""
    Java (Beginner) darslari | 41-dars | Creating File
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIJl2WP4_xT39XCxhyZmeDXSAABeOocxwACkRMAAjwoEEnQ94ntSputNDQE",caption="""
    Java (Beginner) darslari | 42-dars | Write and Read Text in File
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists  \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")



# 43 darslar
@java_menu_router.message(F.text == "43 dars (java)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIJm2WP5EnXQpvoEOa35atZSV-oRb9sAAKTEwACPCgQSaMUL8N6SVT8NAQ",caption="""
    Java (Beginner) darslari | 43-dars | Write and Read Object in File
\nYoutube — www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists \nFacebook — www.facebook.com/kurbanovxurshid
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")

