from aiogram.dispatcher.filters.state import State,StatesGroup

class Log(StatesGroup):
    msg = State()
    
class login_next_step(StatesGroup):
    log_pas = State()
    
class get_user_id(StatesGroup):
    id = State()
    
class get_new_user_data(StatesGroup):
    data = State()
    
class getting_user_message_to_admin(StatesGroup):
    msg = State()
    
class category_0_next_step(StatesGroup):
    ans = State()
    
class choosing_lang(StatesGroup):
    lang = State()
    
class Order_category(StatesGroup):
    select = State()
    
class order_by_date(StatesGroup):
    date = State()
    
class will_continue(StatesGroup):
    yes_or_no = State()
    
class category_0_next_step(StatesGroup):
    ans = State()