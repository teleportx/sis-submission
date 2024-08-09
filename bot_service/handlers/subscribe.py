from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from db.User import User

router = Router()


@router.message(Command('subscribe'))
async def subscribe(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.reply('Не указано ФИ.\n'
                            'Пример использования команды:\n'
                            '<code>/subscribe &#60;ФИ (как в таблице)&#62;</code>')
        return

    if len(command.args) > 64:
        await message.reply('ФИ по длине не должно превышать 64 символа.')
        return

    if not command.args.replace(' ', '').isalpha():
        await message.reply('Кажется ФИ не должно содержать специальных символов...')
        return

    await User.filter(uid=message.chat.id).update(subscription=command.args)

    await message.reply(f'Теперь вы подписаны на посылки <code>{command.args}</code>\n'
                        f'Если захотите сменить подписку, то повторите процедуру.')
