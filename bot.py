import logging

from aiogram import Bot,Dispatcher,executor, types
from btn import *
from inline import *

logging.basicConfig(level=logging.INFO)

BOT_TOKEN="6081129928:AAFHShTstU48s__tEDgLssisqXalWUHBDjU"

bot=Bot(token=BOT_TOKEN)
dp=Dispatcher(bot=bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(text="""
🙋‍♀️Привет дорогой друг!
Меня зовут Роберт Бот
Я буду провождать тебя все время когда ты находишся тут.

""",reply_markup=bosh_menu)

@dp.message_handler(text="😎Мои любимые аниме.")
async def send_welcomer(message: types.Message):
    await message.answer("😎Мои любимые аниме.",reply_markup=bosh_menuu)

@dp.message_handler(text="🔙Назад.")
async def send_welcomer(message: types.Message):
    await message.answer("🔙Назад.",reply_markup=bosh_menu)

@dp.message_handler(text="😒Хочу посмотреть но лень")
async def send_welcomere(message: types.Message):
    await message.answer("😒Хочу посмотреть но лень",reply_markup=bosh_menuuk)

@dp.message_handler(text="😄Любимые персонажы.")
async def send_welcomerel(message: types.Message):
    await message.answer("😄Любимые персонажы.",reply_markup=bosh_menuuku)

@dp.message_handler(text="❓Вопросы.")
async def send_welcomereh(message: types.Message):
    await message.answer(text="Все вопросы ко мне профиль @Mister_X_UZ",reply_markup=bosh_menuukuk)

@dp.message_handler(text="😲Смертельные техники.")
async def send_welcomereh(message: types.Message):
    await message.answer(text="😲Смертельные техники.",reply_markup=bosh_menuukuku)

@dp.message_handler(text='⚔️Клинок рассекающий демонов.')
async def send_welcomee(message: types.Message):
    img = types.InputFile("с.jpg")
    await message.answer_photo(photo=img)

if __name__=="__main__":
    executor.start_polling(dp)