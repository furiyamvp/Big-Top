from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.admin_main_menu import admin_main_menu
from keyboards.default.little import phone_number_share
from keyboards.default.user_main_menu import user_main_menu
from loader import dp, db_manager
from states.RegisterState import Register


@dp.message_handler(commands="start", chat_id=ADMINS)
async def admin_start_handler(message: types.Message):
    text = "Botga xush kelibsiz ADMIN. 😊"
    await message.answer(text=text, reply_markup=admin_main_menu)


@dp.message_handler(commands="start", state="*")
async def start_handler(message: types.Message, state: FSMContext):
    if db_manager.get_user(message):
        text = "Botga xush kelibsiz. 😊"
        await message.answer(text=text, reply_markup=user_main_menu)
        await state.finish()
    else:
        text = "Iltimos to'liq ism familyangizni kiriting.\nMasalan: Rixsiboyev Muhammad Yunus"
        await message.answer(text=text)
        await Register.full_name.set()


@dp.message_handler(state=Register.full_name)
async def full_name_state(message: types.Message, state: FSMContext):
    await state.update_data({
        "full_name": message.text
    })
    text = "Iltimos telefon raqamingizni kiriting."
    await message.answer(text=text, reply_markup=phone_number_share)
    await Register.phone_number.set()


@dp.message_handler(state=Register.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number_state(message: types.Message, state: FSMContext):
    await state.update_data({
        "phone_number": message.contact.phone_number,
        "user_id": message.chat.id
    })
    text = "Iltimos yoshingizni kiriting.\nMasalan: 21"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await Register.age.set()


@dp.message_handler(state=Register.age)
async def age_id_state(message: types.Message, state: FSMContext):
    await state.update_data({
        "age": message.text
    })
    data = await state.get_data()
    if db_manager.append_user(data):
        text = "Siz muvaffaqiyatli ro'yxatdan o'tdingiz. ✅"
    else:
        text = "Botda muammo mavjud, biz bilan bog'laning"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()
