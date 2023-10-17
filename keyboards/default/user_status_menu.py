from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_order_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳ Kutilayotganlar"),
            KeyboardButton(text="✅ Qabul qilinganlar")
        ],
        [
            KeyboardButton(text="❌ Bekor qilinganlar")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga")
        ],
    ], resize_keyboard=True
)
