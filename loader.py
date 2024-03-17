from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = '5620182480:AAF-8gAGM52fWepKVsycyGZIPkMy0tEBs1c'
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())