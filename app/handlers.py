from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.Keyboard as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.BD.SQl3 import reg_users, out_data

router = Router()

class Reg(StatesGroup):
    name = State()
    password = State()
    number = State()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.first_name}, {message.from_user.last_name}!", reply_markup=kb.main)


@router.message(F.text == 'help')
async def help(message: Message) -> None:
    await message.answer(f"This is help batton")

@router.message(F.text == 'Конвертировать мой файл')
async def convertator(message: Message) -> None:
    await message.answer("Отправьте мне Excel-файл для конвертации в формате '.YML.' или '.yml'")

@router.message(F.text == 'Файл пример')
async def file_xmpl(message: Message) -> None:
    await message.answer(f'Вот файл-пример, содержащий нужные поля: ')

@router.message(F.text == 'Регистрация')
async def one_step(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите Ваше имя!')

@router.message(Reg.name)
async def two_step(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.password)
    await message.answer('Создайте пароль')

@router.message(Reg.password)
async def three_step(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    await state.set_state(Reg.number)
    await message.answer('Отправьте Ваш номер', reply_markup=kb.get_number_phone)

@router.message(Reg.number, F.contact)
async def four_step(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Регистрация завершена!\nВаше имя: {data["name"]}\nВаш номер: {data["number"]}\nВаш пароль: {data["password"]}', reply_markup=kb.main)
    reg_users(data['name'], data['password'], data['number'])
    await state.clear()
    out_data()