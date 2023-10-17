from aiogram import types

from keyboards.default.user_main_menu import user_main_menu
from loader import dp


@dp.message_handler(text="📞 Aloqa uchun")
async def start_handler(message: types.Message):
    text = "Biz bilan muloqotga chiqish uchun.\nTel: +998938630699\nTelegram: @FURIYA_MVP"
    await message.answer(text=text, reply_markup=user_main_menu)
