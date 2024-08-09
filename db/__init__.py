from tortoise import Tortoise

import config


async def init():
    await Tortoise.init(
        db_url=config.db_url,
        modules={"models": ['db.User']}
    )
