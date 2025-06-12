from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard =[
    [KeyboardButton(text='Файл пример')],
    [KeyboardButton(text='Регистрация')],
    [KeyboardButton(text='Конвертировать мой файл')],
    [KeyboardButton(text='help')]
])

get_number_phone = ReplyKeyboardMarkup (keyboard = [
    [KeyboardButton (text='Отправить мой номер', request_contact=True)
]], resize_keyboard=True)