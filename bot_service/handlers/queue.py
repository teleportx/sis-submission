from aiogram import Router, types
from aiogram.filters import Command

from db.User import Task

router = Router()


@router.message(Command('queue'))
async def queue(message: types.Message):
    queue_size = await Task.all().count()
    await message.reply(f'Сейчас в очереди: <b>{queue_size} посылок</b>')
