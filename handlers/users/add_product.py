from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin_main_menu import add_product_menu_def, admin_main_menu_back, admin_main_menu
from keyboards.inline.change_product import admin_product_change_def

from loader import dp, db_manager
from states.AddProductState import AddProduct


@dp.message_handler(text="🛍 Mahsulotlar", chat_id=ADMINS)
async def start_handler(message: types.Message, state: FSMContext):
    await state.set_state('all-product-state')
    text = "Mahsulotlar menyusiga xush kelibsiz."
    await message.answer(text=text, reply_markup=await add_product_menu_def())


@dp.message_handler(text="➕ Mahsulot qo'shish", chat_id=ADMINS, state="all-product-state")
async def start_handler(message: types.Message):
    text = "Mahsulot nomini kiriting."
    await message.answer(text=text, reply_markup=admin_main_menu_back)
    await AddProduct.product_name.set()


@dp.message_handler(state=AddProduct.product_name, chat_id=ADMINS)
async def get_sticker_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "product_name": message.text
    })
    text = "Mahsulot narxini kiriting."
    await message.answer(text=text)
    await AddProduct.price.set()


@dp.message_handler(state=AddProduct.price, chat_id=ADMINS)
async def get_price_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "price": message.text
    })
    text = "Mahsulot haqida ma'lumot kiriting."
    await message.answer(text=text)
    await AddProduct.description.set()


@dp.message_handler(state=AddProduct.description, chat_id=ADMINS)
async def get_description_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "description": message.text
    })
    text = "Mahsulot sonini kiriting."
    await message.answer(text=text)
    await AddProduct.quantity.set()


@dp.message_handler(state=AddProduct.quantity, chat_id=ADMINS)
async def get_quantity_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "quantity": message.text
    })
    text = "Mahsulot rasmini kiriting."
    await message.answer(text=text)
    await AddProduct.photo.set()


@dp.message_handler(state=AddProduct.photo, chat_id=ADMINS, content_types=types.ContentType.PHOTO)
async def get_photo_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "photo": message.photo[-1].file_id
    })
    data = await state.get_data()
    if db_manager.append_product(data):
        text = "Mahsulot qo'shildi. ✅"
    else:
        text = "Mahsulot qo'shish jarayonida xatolik bor ❌"
    await message.answer(text=text, reply_markup=await add_product_menu_def())
    await state.set_state("all-product-state")


@dp.message_handler(chat_id=ADMINS, state="all-product-state")
async def get_one_sticker_handler(message: types.Message):
    product_name = message.text
    product = db_manager.search_product_by_name(product_name)
    if product:
        product_id = product[0]
        product_name = product[1]
        price = product[2]
        description = product[3]
        photo = product[4]
        quantity = product[5]
        caption = f"{product_name} | {price} so'm | {quantity} ta bor\n\n{description}"
        await message.answer_photo(photo=photo, caption=caption,
                                   reply_markup=await admin_product_change_def(product_id))
