from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

button_yes = KeyboardButton(text=LEXICON_RU['yes'])
start_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_yes]],
                                    resize_keyboard=True)

but_articles_1 = KeyboardButton(text='Философия')
but_articles_2 = KeyboardButton(text='IT')
but_articles_3 = KeyboardButton(text='Литература')
but_articles_4 = KeyboardButton(text='Другое')
articles_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[but_articles_1, but_articles_2 ],
                                              [but_articles_3, but_articles_4]],
                                    resize_keyboard=True)

button_stat = KeyboardButton(text=LEXICON_RU['statya'])
stat_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_stat]],
                                    resize_keyboard=True)