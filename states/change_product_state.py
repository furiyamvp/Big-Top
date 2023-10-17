from aiogram.dispatcher.filters.state import StatesGroup, State


class UpdateProduct(StatesGroup):
    product_name = State()
    photo = State()
    price = State()
    quantity = State()
    description = State()