from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Mahsulotlar"),
            KeyboardButton(text="🛒 Buyurtmalar"),
        ],
        [
            KeyboardButton(text="📞 Aloqa uchun"),
            KeyboardButton(text="👤 Profil"),
        ]
    ], resize_keyboard=True
)

user_main_menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ], resize_keyboard=True
)


async def all_product_menu_def():
    products = db_manager.get_all_product()
    user_product_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    back = KeyboardButton(text="⬅️ Orqaga")
    user_product_menu.row(back)

    product_buttons = []
    for product in products:
        keyboard = KeyboardButton(text=product[1])
        product_buttons.append(keyboard)

        if len(product_buttons) == 2:
            user_product_menu.row(*product_buttons)
            product_buttons = []
    if product_buttons:
        user_product_menu.row(*product_buttons)

    return user_product_menu
