import logging
import sys

sys.path.append('..')

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher

import db
import asyncio


import config
import handlers

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)


dp = Dispatcher()

bot = Bot(
    token=config.token,
    default=DefaultBotProperties(parse_mode='html'),
)


async def main():
    await db.init()

    dp.include_router(handlers.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
