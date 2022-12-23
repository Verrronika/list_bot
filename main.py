
import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio

logging.basicConfig(level=logging.INFO)
TOKEN = '5878737412:AAHcFcHDRf7zrTQCrJ9dSHPliIoqVYRNKYc'
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

mas = list()
i = 1

@dp.message_handler(commands=["show"])
async def show(message: types.Message):
    global i, mas
    await message.answer(str(mas))


@dp.message_handler(commands=["add_next"])
async def add_next(message: types.Message):
    global i, mas
    mas.append(i)
    i += 1
    await message.answer(str(mas))


@dp.message_handler(commands=["delete"])
async def delete(message: types.Message):
    global i, mas
    if len(mas) > 0:
        mas.pop()
        i -= 1
    await message.answer(str(mas))


@dp.message_handler(commands=["length"])
async def length(message: types.Message):
    global i, mas
    await message.answer(str(len(mas)))


@dp.message_handler(commands=["clear"])
async def clear(message: types.Message):
    global i, mas
    i = 1
    mas = []
    await message.answer(str(mas))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = 'Вывести: /show\nДобавить следующий элемент: /add_next\nУдалить последний элемент: /delete\nОчистить: /clear\nВывести длину: /length\n'
    await message.answer(text)


executor.start_polling(dp)
