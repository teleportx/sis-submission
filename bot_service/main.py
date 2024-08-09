import sys

from aiogram.client.default import DefaultBotProperties

import db

sys.path.append('..')

import asyncio

from aiogram import Bot, Dispatcher

import config
import handlers

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
