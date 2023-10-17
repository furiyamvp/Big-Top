from aiogram.dispatcher.filters.state import StatesGroup, State


class AddProduct(StatesGroup):
    product_name = State()
    photo = State()
    price = State()
    quantity = State()
    description = State()
