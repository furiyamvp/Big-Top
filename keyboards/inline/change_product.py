from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

admin_product_change_photo = CallbackData("change_product_photo", "action", "product_id")
admin_product_change_price = CallbackData("change_product_price", "action", "product_id")
admin_product_change_name = CallbackData("change_product_name", "action", "product_id")
admin_product_change_quantity = CallbackData("change_product_quantity ", "action", "product_id")
admin_product_change_description = CallbackData("change_product_description", "action", "product_id")
admin_product_delete = CallbackData("change_product_delete", "action", "product_id")


async def admin_product_change_def(product_id: int):
    admin_product_change = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Rasm",
                    callback_data=admin_product_change_photo.new(action="change_product_photo", product_id=product_id)),
                InlineKeyboardButton(
                    text="Nomi",
                    callback_data=admin_product_change_name.new(action="change_product_name", product_id=product_id))
            ],
            [
                InlineKeyboardButton(
                    text="Narxi",
                    callback_data=admin_product_change_price.new(action="change_product_price", product_id=product_id)),
                InlineKeyboardButton(
                    text="Ma'lumot",
                    callback_data=admin_product_change_description.new(action="change_product_description",
                                                                       product_id=product_id))
            ],
            [
                InlineKeyboardButton(
                    text="Soni",
                    callback_data=admin_product_change_quantity.new(action="change_product_quantity",
                                                                    product_id=product_id)),
                InlineKeyboardButton(
                    text="O'chirish",
                    callback_data=admin_product_delete.new(action="change_product_delete",
                                                           product_id=product_id))
            ],
        ]
    )
    return admin_product_change
