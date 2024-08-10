import sys

sys.path.append('..')

import asyncio
import logging

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

import config
import db
import parser
from db.User import Task, User

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)

bot = Bot(
    token=config.token,
    default=DefaultBotProperties(parse_mode='html'),
)


async def update_table():
    table = await parser.parse()

    prs_saved = await Task.filter()

    for name in table:
        for task in table[name]:
            virtual_task = Task(name=task[0])
            is_saved = virtual_task in prs_saved

            if task[1] == 'PR':
                if not is_saved:
                    logging.info(f'Added PR {task[0]}')
                    await virtual_task.save()
                continue

            if not is_saved:
                continue

            logging.info(f'Change {task[0]} PR -> {task[1]}')

            await Task.filter(name=task[0]).delete()

            users = await User.filter(subscription=name)
            text = ('❗️ <b>Статус посылки изменен</b>\n'
                    f'Задача: <code>{task[0][task[0].find(",") + 2:]}</code>\n'
                    f'<i>PR -> {task[1]}</i>')
            for send_to in users:
                try:
                    await bot.send_message(send_to.uid, text)

                except:
                    ...


async def main():
    await db.init()

    while True:
        logging.info('Updating table...')
        try:
            await update_table()

        except asyncio.exceptions.TimeoutError:
            logging.error('Failed access to the table. Skipping updating.')
            await asyncio.sleep(10)
            continue

        logging.info('Table updating completed.')
        await asyncio.sleep(120)


if __name__ == '__main__':
    asyncio.run(main())
