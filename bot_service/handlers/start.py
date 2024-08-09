from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import LinkPreviewOptions
from aiogram.utils.formatting import Text, Bold, TextLink, Code

from db.User import User

router = Router()

text = Text(
    Bold('Посылки ЛКШ'), '\n',
    'Автор - ', TextLink('Степан Хожемпо', url='https://github.com/teleportx'), '\n',
    TextLink('Source code', url='https://github.com/teleportx/sis-submission'), '\n',
    '\n',
    Bold('Что делает этот бот?'), '\n',
    'Он отправляет вам уведомление об изменении статуса отосланной посылки от определенного человека.\n',
    'Для этого пропишите:\n', Code('/subscribe <ФИ (также как в таблице)>'), '\n',
    'После этого вы будете получать уведомления о изменение статуса посылки с PR на RJ или OK.', '\n',
    '\n',
    Bold('Как это работает?'), '\n',
    'Вкраце: парсинг таблицы с ejudge\'a.\n'
    'Более подробно, как это хостится и какие были трудности можете прочитать в readme на гитхабе.'
)


@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(**text.as_kwargs(), link_preview_options=LinkPreviewOptions(is_disabled=True))
    await User.get_or_create(uid=message.chat.id)
