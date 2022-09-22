from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import  executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import os
import asyncio
from contextlib import suppress
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted, MessageToDeleteNotFound)
from config import *
print('Фреймворк загружен\nТокен загружен')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
print('Токен установлен\nБот запущен')
@dp.message_handler(commands=['start'])
async def lets_start(message: types.Message):
    await message.answer('Привет! Этот бот обучит тебя финансовой грамотности '
                         'при помощи бесплатного курса. Хочешь узнать '
                         'побольше?', reply_markup=inline)
@dp.message_handler(Text(equals='Давай'))
async def beginnging(message: types.Message):
    await message.answer('Есть ли у тебя карманные деньги?', reply_markup=inline1)
@dp.message_handler(Text(equals=('Да!', 'Нет!')))
async def beginnging1(message: types.Message):
    await message.answer('Тогда курс тебе точно понадобится!', reply_markup=inline2)


executor.start_polling(dp, skip_updates=True)

