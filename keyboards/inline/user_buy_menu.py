from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def user_product_buy_def(quantity, total):
    user_product_buy = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➖", callback_data="minus_product"),
                InlineKeyboardButton(text=f"{quantity}/{total}", callback_data="total"),
                InlineKeyboardButton(text="➕", callback_data="plus_product"),
            ],
            [
                InlineKeyboardButton(text="👀 Savatni ko'rish", callback_data="show_basket"),
            ]
        ]
    )
    return user_product_buy


user_basket_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛍 Zakaz berish", callback_data="order_basket"),
            InlineKeyboardButton(text="🧹 Savatni tozalash", callback_data="clear_basket"),
        ]
    ]
)

user_delivery_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📥 Olib ketish", callback_data="take_away_basket"),
            InlineKeyboardButton(text="📦 Buyurtma Berish", callback_data="delivery_basket"),
        ]
    ]
)
