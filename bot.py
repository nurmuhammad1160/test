import asyncio
import logging

from aiogram import  Dispatcher
from loader import bot

from handlers.start import start_router
from handlers.frontend import fronend_menu_router
from handlers.frontentorbeckend import FronorBeck_menu_router
from handlers.get_video_id import get_id_router
from handlers.html import html_menu_router
from handlers.css_handler import css_menu_router
from handlers.bootstrap_h import bootstrap_menu_router
from handlers.js_handler import js_menu_router
from handlers.react_handler import react_menu_router
from handlers.vue_js_handler import vue_js_menu_router
from handlers.type_handler import type_menu_router
from handlers.beckend import beckend_menu_router
from handlers.node_js import node_js_menu_router
from handlers.java import java_menu_router
from handlers.python import python_menu_router
from handlers.PHP import php_menu_router

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
       
    )

    logger.info("Starting bot")

 
    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        FronorBeck_menu_router,
        fronend_menu_router,
        html_menu_router,
        css_menu_router,
        bootstrap_menu_router,
        js_menu_router,
        react_menu_router,
        vue_js_menu_router,
        type_menu_router,
        beckend_menu_router,
        node_js_menu_router,
        java_menu_router,
        python_menu_router,
        php_menu_router,
        start_router,
        get_id_router,
       
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
