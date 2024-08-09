from aiogram import Router

from . import start
from . import subscribe

router = Router()

router.include_router(start.router)
router.include_router(subscribe.router)
