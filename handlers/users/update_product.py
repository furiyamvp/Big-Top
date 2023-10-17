from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin_main_menu import admin_main_menu
from keyboards.inline.change_product import *

from loader import dp, db_manager
from states.change_product_state import UpdateProduct


@dp.callback_query_handler(admin_product_change_photo.filter(action="change_sticker_photo"),
                           state="admin-stickers-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(sticker_id=product_id)
    text = "Yangi rasmni kiriting."
    await call.message.answer(text=text)
    await UpdateProduct.photo.set()


@dp.message_handler(state=UpdateProduct.photo, content_types=types.ContentType.PHOTO)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    photo = message.photo[-1].file_id

    if db_manager.update_admin_sticker(product_id, "photo", photo):
        text = "Rasm yangilandi."
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_name.filter(action="change_sticker_name"),
                           state="admin-stickers-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(product_id=product_id)
    text = "Yangi nomni kiriting."
    await call.message.answer(text=text)
    await UpdateProduct.product_name.set()


@dp.message_handler(state=UpdateProduct.product_name)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    name = message.text

    if db_manager.update_admin_sticker(product_id, "name", name):
        text = "nom yangilandi."
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_price.filter(action="change_sticker_price"),
                           state="admin-stickers-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(sticker_id=product_id)
    text = "Yangi narxini kiriting."
    await call.message.answer(text=text)
    await UpdateProduct.price.set()


@dp.message_handler(state=UpdateProduct.price)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    price = message.text

    if db_manager.update_admin_sticker(product_id, "price", price):
        text = "narx yangilandi."
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_description.filter(action="change_sticker_description"),
                           state="admin-stickers-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(product_id=product_id)
    text = "Yangi ma'lumotni kiriting."
    await call.message.answer(text=text)
    await UpdateProduct.description.set()


@dp.message_handler(state=UpdateProduct.description)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    description = message.text

    if db_manager.update_admin_sticker(product_id, "description", description):
        text = "ma'lumot yangilandi."
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_quantity.filter(action="change_sticker_quantity"),
                           state="admin-stickers-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(product_id=product_id)
    text = "Yangi ma'lumotni kiriting."
    await call.message.answer(text=text)
    await UpdateProduct.quantity.set()


@dp.message_handler(state=UpdateProduct.quantity)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    quantity = message.text

    if db_manager.update_admin_sticker(product_id, "quantity", quantity):
        text = "ma'lumot yangilandi."
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_quantity.filter(action="change_sticker_delete"),
                           state="admin-stickers-state")
async def admin_change_delete_handler(call: types.CallbackQuery, callback_data: dict):
    product_id = callback_data.get('product_id')

    if db_manager.delete_product(product_id):
        text = "ma'lumot ochirildi."
    else:
        text = "Xatolik bor."
    await call.message.answer(text=text, reply_markup=admin_main_menu)
