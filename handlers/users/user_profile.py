from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.user_main_menu import user_main_menu_back, user_main_menu
from keyboards.inline.change_profle import user_profile_menu
from loader import dp, db_manager
from states.change_profile_state import ProfileUpdate


@dp.message_handler(text="👤 Profil")
async def profile_menu_handler(message: types.Message):
    user = db_manager.get_user(message)
    if user:
        text = f"""
👤: {user[2]}
📞: {user[3]}
♾: {user[4]}
"""
        await message.answer(text=text, reply_markup=user_profile_menu)
    else:
        text = "Siz haqingizda ma'lumot topilmadi."
        await message.answer(text=text)


@dp.callback_query_handler(text="change_full_name")
async def change_full_name_handler(call: CallbackQuery):
    text = "Yangi ismni kiriting."
    await call.message.answer(text=text, reply_markup=user_main_menu_back)
    await ProfileUpdate.full_name.set()


@dp.message_handler(state=ProfileUpdate.full_name)
async def update_user_full_name(message: types.Message, state: FSMContext):
    if db_manager.update_user_profile(message, "full_name"):
        text = "Ismingiz yangilandi ✅"
    else:
        text = "Botda xatolik bor ❌"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()


@dp.callback_query_handler(text="change_age")
async def change_age_handler(call: CallbackQuery):
    text = "Yangi yoshingizni kiriting."
    await call.message.answer(text=text, reply_markup=user_main_menu_back)
    await ProfileUpdate.age.set()


@dp.message_handler(state=ProfileUpdate.age)
async def update_age_handler(message: types.Message, state: FSMContext):
    if db_manager.update_user_profile(message, "age"):
        text = "Yoshingiz yangilandi ✅"
    else:
        text = "Botda xatolik bor ❌"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()
