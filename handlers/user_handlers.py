from aiogram import F, Router 
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, URLInputFile, FSInputFile
from keyboards.keyboards import start_kb, stat_kb, articles_kb
from lexicon.lexicon_ru import LEXICON_RU
from aiogram import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from articles import articles
from random import randint




router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_kb)

@router.message(F.text == LEXICON_RU['yes'])
async def choose_theme(message: Message):
    await message.answer(text='Выбери направление', reply_markup=articles_kb)

@router.message(F.text.in_(['Философия', 'Литература', 'Другое', 'IT']))
async def yes_command(message: Message):
    number = randint(1, len(articles[message.text]))
    url_button = InlineKeyboardButton(
    text='Читать',
    url=articles[message.text][number])
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button]])
    await message.answer(text = "Нашел кое-что интересное для тебя!", reply_markup=keyboard)
    await message.answer(text= "Хочешь еще статью?", reply_markup=start_kb)

