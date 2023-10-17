from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

admin_order_accepted_filter = CallbackData("admin_order_delivered", "action", "order_id", "user_id")
admin_order_canceled_filter = CallbackData("admin_order_canceled", "action", "order_id", "user_id")

admin_order_decision_filter = CallbackData("admin_order_accept", "action", "order_id", "user_id")
admin_order_cancel = CallbackData("admin_order_cancel", "action", "order_id", "user_id")


async def admin_order_decision_def(order_id: int, user_id: int):
    admin_order_decision = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Qabul qilish",
                    callback_data=admin_order_decision_filter.new(action="admin_order_accept", order_id=order_id,
                                                                  user_id=user_id)),

                InlineKeyboardButton(
                    text="❌ Bekor qilish",
                    callback_data=admin_order_cancel.new(action="admin_order_cancel", order_id=order_id,
                                                         user_id=user_id))
            ]
        ]
    )
    return admin_order_decision


async def admin_order_accepted_def(order_id: int, user_id: int):
    admin_order_accepted = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Yetkazib berildi",
                    callback_data=admin_order_accepted_filter.new(action="admin_order_delivered", order_id=order_id,
                                                                  user_id=user_id)),

                InlineKeyboardButton(
                    text="❌ Bekor qilish",
                    callback_data=admin_order_cancel.new(action="admin_order_cancel", order_id=order_id,
                                                         user_id=user_id))
            ]
        ]
    )
    return admin_order_accepted


async def admin_order_canceled_def(order_id: int, user_id: int):
    admin_order_canceled = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🗑 O'chirib tashlash",
                    callback_data=admin_order_canceled_filter.new(action="admin_order_canceled", order_id=order_id,
                                                                  user_id=user_id))
            ]
        ]
    )
    return admin_order_canceled


async def admin_order_search_def(order_id: int, user_id: int):
    admin_order_search = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Qabul qilish",
                    callback_data=admin_order_decision_filter.new(action="admin_order_accept", order_id=order_id,
                                                                  user_id=user_id))
            ],
            [

                InlineKeyboardButton(
                    text="❌ Bekor qilish",
                    callback_data=admin_order_cancel.new(action="admin_order_cancel", order_id=order_id,
                                                         user_id=user_id))
            ],
            [
                InlineKeyboardButton(
                    text="🗑 O'chirib tashlash",
                    callback_data=admin_order_canceled_filter.new(action="admin_order_canceled", order_id=order_id,
                                                                  user_id=user_id))
            ],
            [
                InlineKeyboardButton(
                    text="✅ Yetkazib berildi",
                    callback_data=admin_order_accepted_filter.new(action="admin_order_delivered", order_id=order_id,
                                                                  user_id=user_id))
            ]
        ]
    )
    return admin_order_search

