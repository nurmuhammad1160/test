from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from keyboards.bootstrap import bootstrap_menu
bootstrap_menu_router: Router = Router()


@bootstrap_menu_router.message(F.text == "Bootstrap darslari")
async def bootstrap_handler(message: Message):
    await message.answer("Bootstrap darslari", reply_markup=bootstrap_menu)

# 1-2 darslar
@bootstrap_menu_router.message(F.text == "1-2 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIENmV50bKXo6PwLBHQIus-v6RWtap6AAKbDgACwgQ5SPNyavw27R9nMwQ",caption="""
    Bootstrap darslari | 1-qism | Bootstrap kirish
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEN2V50bLo7zYHxz0q49hF4h6395yRAAKdDgACwgQ5SOJOsRQcPG-KMwQ",caption="""
    Bootstrap darslari | 2-qism | Table
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 3-4 darslar
@bootstrap_menu_router.message(F.text == "3-4 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEPWV50vhyfkTlDVjXMYXy7Aj6mwYXAAKfDgACwgQ5SJNsPV-t86TmMwQ",caption="""
    Bootstrap darslari | 3-qism | Grid
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEPmV50vg3HRhJAndX8kbHJqS3uit5AAKgDgACwgQ5SMSa6N-mU13DMwQ",caption="""
    Bootstrap darslari | 4-qism | Alert, Button groups
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 5-6 darslar
@bootstrap_menu_router.message(F.text == "5-6 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEQWV504g69Sgih4va3bKK7x63d0j_AAKhDgACwgQ5SLfzgwXj970YMwQ",caption="""
    Bootstrap darslari | 5-qism | Progress Bar, Spinners
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEQmV504hfpjGRXU8YiGsiETFnDrBgAAKiDgACwgQ5SGgB4IpZ3ZwHMwQ",caption="""
    Bootstrap darslari | 6-qism | Pagination, List Groups
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    

# 7-8 darslar
@bootstrap_menu_router.message(F.text == "7-8 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIERWV51Cc2hRyEnW3AreKCbeUCiHy8AAKjDgACwgQ5SMJ9iDqC62LqMwQ",caption="""
    Bootstrap darslari | 7-qism | Card, Dropdown Menu
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIERmV51Cc6XyJj9t3Lu-QzCD9-RGsaAAKkDgACwgQ5SJGrFvUhvUHFMwQ",caption="""
    Bootstrap darslari | 8-qism | Collapse, Nav
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 9-10 darslar
@bootstrap_menu_router.message(F.text == "9-10 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIESWV51HCR7eA3k9JNT2JEIVzqEUGZAAKlDgACwgQ5SNk2EnCU7v0iMwQ",caption="""
    Bootstrap darslari | 9-qism | Form, Input Group
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIESmV51HCN1TZ1KDKGROCRGRI8lGnjAAKmDgACwgQ5SObgfcRMMdmXMwQ",caption="""
    Bootstrap darslari | 10-qism | Input Groups
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    
    

# 11-12 darslar
@bootstrap_menu_router.message(F.text == "11-12 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIETWV51ROKZ6UwAAHo2qh439s76QzGtgACpw4AAsIEOUiyeZ0Xm0EEdTME",caption="""
    Bootstrap darslari | 11-qism | Modal, Carousel
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIETmV51ROP5YTPmek3cllrvZ-TVP6aAAKoDgACwgQ5SEbqaTeoTpmwMwQ",caption="""
    Bootstrap darslari | 12-qism | Tooltip, Popover
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 13-14 darslar
@bootstrap_menu_router.message(F.text == "13-14 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEUWV51iC-XNoYxVI4q_KsdLt69XwTAAKpDgACwgQ5SMRfbV52i9i8MwQ",caption="""
    Bootstrap darslari | 13-qism | Toast, Scroll Spy
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEUmV51iD_M18CIUTjgxqC737nJbhhAAKqDgACwgQ5SPRbHn-dq6TIMwQ",caption="""
    Bootstrap darslari | 14-qism | Croll spy
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    

# 15-16 darslar
@bootstrap_menu_router.message(F.text == "15-16 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEVWV51rsMpmYfN_O_h7JTMSe_Mn8iAAKrDgACwgQ5SDp1onlbTSRqMwQ",caption="""
    Bootstrap darslari | 15-qism | Utilities
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEVmV51rscizW6tp7fS-eLi32QPVDeAAKsDgACwgQ5SMEiw9I9du8EMwQ",caption="""
    Bootstrap darslari | 16-qism | Flex
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
    
    

# 17-18 darslar
@bootstrap_menu_router.message(F.text == "17-18 dars (bootstrap)")
async def one_two(message: Message):
    await message.answer_video("BAACAgIAAxkBAAIEWWV51xCPiQ6mcKMVIPnYDe-KM5QsAAKtDgACwgQ5SPvuT9v0-W2UMwQ",caption="""
    Bootstrap darslari | 17-qism | Custom Forms
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    await message.answer_video("BAACAgIAAxkBAAIEWmV51xAXFcUBHRuyNuTtRVuqNXDBAAKuDgACwgQ5SFj9KPqFP3uwMwQ",caption="""
    Bootstrap darslari | 18-qism | Login form yasash
\nYoutube — www.youtube.com/c/Idrok  \nTelegram — @idroktalim
\n@BepulDasturlashDarslar_bot — IT darslar platformasi!
""")
    
