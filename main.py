"""
ដំណើរការ Bot (Admin + Store, Helper ប្រសិនបើកំណត់ Token) + Mini App Web Server ក្នុងពេលតែមួយ។
ដំណើរការ: python main.py
ឈប់: Ctrl + C
"""
import asyncio
import logging
import os
from threading import Thread

import database as db
import admin_bot
import store_bot
from keep_alive import keep_alive

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def start_webapp_server():
    import webapp_server
    port = int(os.getenv("WEBAPP_PORT", os.getenv("PORT", "8080")))
    logger.info(f"Starting Mini App web server on port {port}")
    Thread(target=webapp_server.run, kwargs={"port": port}, daemon=True).start()


async def main():
    db.init_db()

    # Mini App web server (serves the store UI + product API). Runs whenever WEBAPP_URL
    # is configured, since that means the person wants the Mini App available.
    if os.getenv("WEBAPP_URL"):
        start_webapp_server()
    elif os.getenv("ENABLE_KEEPALIVE") == "1":
        keep_alive()

    apps = [admin_bot.build_app(), store_bot.build_app()]

    # Helper Bot (Blox Fruits tips bot) is optional - only starts if a real token is set
    helper_token = os.getenv("HELPER_BOT_TOKEN", "")
    if helper_token and "PUT_YOUR" not in helper_token:
        import helper_bot
        apps.append(helper_bot.build_app())

    for app in apps:
        await app.initialize()
        await app.start()
        await app.updater.start_polling()

    logger.info(f"{len(apps)} Uchiro Store bot(s) running. Press Ctrl+C to stop.")

    stop_event = asyncio.Event()
    try:
        await stop_event.wait()
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        for app in apps:
            await app.updater.stop()
            await app.stop()
            await app.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
