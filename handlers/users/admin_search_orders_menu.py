from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.user_main_menu import user_main_menu_back
from keyboards.inline.admin_buy_message import admin_order_search_def
from loader import db_manager, dp


@dp.message_handler(text="🔎 Buyurtma qidirish", chat_id=ADMINS)
async def user_order_search_handler(message: types.Message, state: FSMContext):
    text = "Iltimos buyurtma ID raqamini kiriting."
    await message.answer(text=text, reply_markup=user_main_menu_back)
    await state.set_state('admin-get-order-id')


@dp.message_handler(state="admin-get-order-id", chat_id=ADMINS)
async def user_order_get_id_handler(message: types.Message, state: FSMContext):
    order = db_manager.get_order_by_id(int(message.text))

    if order:
        text = ""
        order_items = db_manager.get_order_items_by_order_id(order[2])
        user = db_manager.get_user_by_id(order[1])
        products = ""
        counter = 1
        total_price = 0
        for item in order_items:
            total_price += float(item[4]) * float(item[3])
            products += f"{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n"
            counter += 1
        text += f"""
🆔 {order[2]}

☎️ {user[3]}
👤 {user[2]}
⏳ {order[3]}
⏰ {order[4]}

{products}
Jami: {total_price} so'm
"""
        await message.answer(text=text, reply_markup=await admin_order_search_def(order[2], order[1]))
    else:
        text = "Bu ID raqamli buyurtma mavjud emas. Iltimos ko'zinga qarab yozing."
        await message.answer(text=text)
    await state.finish()