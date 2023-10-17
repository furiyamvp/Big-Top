from aiogram import types

from data.config import ADMINS
from keyboards.inline.admin_buy_message import admin_order_decision_def, admin_order_canceled_def, \
    admin_order_accepted_def
from loader import db_manager, dp


@dp.message_handler(text="⏳ Kutilayotganlar", chat_id=ADMINS)
async def user_order_waiting_handler(message: types.Message):
    orders = db_manager.get_all_orders_by_status_admin("Kutilmoqda")
    if len(orders) == 0:
        text = "Hozirda buyurtmalar mavjud emas."
        await message.answer(text=text)
    else:
        for order in orders:
            order_items = db_manager.get_order_items_by_order_id(order[2])
            user = db_manager.get_user_by_id(order[1])
            products = ""
            counter = 1
            total_price = 0
            for item in order_items:
                total_price += float(item[4]) * float(item[3])
                products += f"{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n"
                counter += 1
            text = f"""

🆔 {order[2]}

☎️ {user[3]}
👤 {user[2]}
⏳ {order[3]}
⏰ {order[4]}

{products}
Jami: {total_price} so'm
    """
            await message.answer(text=text, reply_markup=await admin_order_decision_def(order[2], order[1]))


@dp.message_handler(text="✅ Qabul qilinganlar", chat_id=ADMINS)
async def user_order_waiting_handler(message: types.Message):
    orders = db_manager.get_all_orders_by_status_admin("Qabul qilingan")
    if len(orders) == 0:
        text = "Hozirda buyurtmalar mavjud emas."
        await message.answer(text=text)
    else:
        for order in orders:
            order_items = db_manager.get_order_items_by_order_id(order[2])
            user = db_manager.get_user_by_id(order[1])
            products = ""
            counter = 1
            total_price = 0
            for item in order_items:
                total_price += float(item[4]) * float(item[3])
                products += f"{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n"
                counter += 1
            text = f"""

🆔 {order[2]}

☎️ {user[3]}
👤 {user[2]}
⏳ {order[3]}
⏰ {order[4]}

{products}
Jami: {total_price} so'm
    """
            await message.answer(text=text, reply_markup=await admin_order_accepted_def(order[2], order[1]))


@dp.message_handler(text="❌ Bekor qilinganlar", chat_id=ADMINS)
async def user_order_waiting_handler(message: types.Message):
    orders = db_manager.get_all_orders_by_status_admin("Bekot qilingan")

    if len(orders) == 0:
        text = "Hozirda buyurtmalar mavjud emas."
        await message.answer(text=text)
    else:
        for order in orders:
            order_items = db_manager.get_order_items_by_order_id(order[2])
            user = db_manager.get_user_by_id(order[1])
            products = ""
            counter = 1
            total_price = 0
            for item in order_items:
                total_price += float(item[4]) * float(item[3])
                products += f"{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n"
                counter += 1
            text = f"""

🆔 {order[2]}

☎️ {user[3]}
👤 {user[2]}
⏳ {order[3]}
⏰ {order[4]}

{products}
Jami: {total_price} so'm
    """
            await message.answer(text=text, reply_markup=await admin_order_canceled_def(order[2], order[1]))
