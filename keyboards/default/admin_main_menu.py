from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager

admin_main_menu: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Mahsulotlar"),
            KeyboardButton(text="🛒 Buyurtmalar")
        ],
        [
            KeyboardButton(text="🔎 Buyurtma qidirish")
        ]
    ], resize_keyboard=True
)


admin_main_menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ], resize_keyboard=True
)


async def add_product_menu_def():
    products = db_manager.get_all_product()
    admin_product_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    back = KeyboardButton(text="⬅️ Orqaga")
    product_plus = KeyboardButton(text="➕ Mahsulot qo'shish")
    admin_product_menu.insert(back)
    admin_product_menu.insert(product_plus)
    for product in products:
        keyboard = KeyboardButton(text=product[1])
        admin_product_menu.insert(keyboard)

    return admin_product_menu

