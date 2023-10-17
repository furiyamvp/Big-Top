from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

user_profile_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ism", callback_data="change_full_name"),
            InlineKeyboardButton(text="Yosh", callback_data="change_age")

        ]
    ]
)
