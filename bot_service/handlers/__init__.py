from aiogram import Router

from . import start
from . import subscribe
from . import queue

router = Router()

router.include_router(start.router)
router.include_router(subscribe.router)
router.include_router(queue.router)
