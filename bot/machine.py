from aiogram.dispatcher.filters.state import State,StatesGroup

class order_by_date(StatesGroup):
    date = State()

class msg_to_admin(StatesGroup):
    msg = State()