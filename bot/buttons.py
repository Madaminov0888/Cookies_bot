import config
from templates import Templates
from aiogram import types
from backend.models import Cake




def category(my_lang):
    info = [Templates.category_1.get(my_lang), Templates.category_2.get(my_lang), Templates.category_3.get(my_lang), Templates.category_0.get(my_lang), Templates.category_4.get(my_lang)]
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    menu.add(*info)
    return menu


'''
def accept_cancel_markup(my_lang,c_data_1, c_data_2,m,p):
    a = types.InlineKeyboardButton(text='➖', callback_data=m),
    b = types.InlineKeyboardButton(text=lang[my_lang]['cancel'], callback_data=c_data_1),
    c = types.InlineKeyboardButton(text=lang[my_lang]['accept'], callback_data=c_data_2),
    d = types.InlineKeyboardButton(text='➕', callback_data=p)
    return [a,b,c,d]
'''


delete_keyboard = types.ReplyKeyboardRemove()



def exit(my_lang):
    exit_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    exit_button.add(Templates.back.get(my_lang))
    return exit_button


def calculator_keyboard(my_lang):
    calculator_keyboard = types.InlineKeyboardMarkup()
    calculator_keyboard.row(
        types.InlineKeyboardButton(text='1', callback_data='1'),
        types.InlineKeyboardButton(text='2', callback_data='2'),
        types.InlineKeyboardButton(text='3', callback_data='3')
    )
    calculator_keyboard.row(
        types.InlineKeyboardButton(text='4', callback_data='4'),
        types.InlineKeyboardButton(text='5', callback_data='5'),
        types.InlineKeyboardButton(text='6', callback_data='6')
    )
    calculator_keyboard.row(
        types.InlineKeyboardButton(text='7', callback_data='7'),
        types.InlineKeyboardButton(text='8', callback_data='8'),
        types.InlineKeyboardButton(text='9', callback_data='9')
    )
    calculator_keyboard.row(
        types.InlineKeyboardButton(text=' ', callback_data=' '),
        types.InlineKeyboardButton(text='0', callback_data='0'),
        types.InlineKeyboardButton(text=' ', callback_data=' ')
    )
    calculator_keyboard.row(
        types.InlineKeyboardButton(Templates.back.get(my_lang), callback_data=f'{Templates.back.get(my_lang)} '),
        types.InlineKeyboardButton(text='C', callback_data='c'),
        types.InlineKeyboardButton(text='✅ Ok', callback_data='ok')
    )
    return calculator_keyboard

def settings_keyboard(my_lang):
    settings_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,  keyboard=[
        [
            types.KeyboardButton(Templates.change_lang.get(my_lang))
        ],
        [
            types.KeyboardButton(Templates.back.get(my_lang))
        ]
    ])
    return settings_keyboard


def changing_lang(lang):
    change_lang = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            types.KeyboardButton(text=Templates.uz.get(lang)),
            types.KeyboardButton(text=Templates.ru.get(lang))
        ]
    ])
    return change_lang

def order_category(my_lang):
    order_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,  keyboard=[
        [
            types.KeyboardButton(Templates.todays_orders.get(my_lang)),
            types.KeyboardButton(Templates.by_date.get(my_lang))
        ],
        [
            types.KeyboardButton(Templates.all_orders.get(my_lang))
        ],
        [
            types.KeyboardButton(Templates.back.get(my_lang))
        ]
    ])
    return order_keyboard


def products_buttons(my_lang):
    products_buttons = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    cake_names = [i.cake_name for i in Cake.objects.all()]
    for i in cake_names:
        buttons.append(types.InlineKeyboardButton(text=i, callback_data=i))
    products_buttons.add(*buttons)
    products_buttons.row(
        types.InlineKeyboardButton(Templates.back.get(my_lang),callback_data=f' {Templates.back.get(my_lang)}')
    )

    return products_buttons

def do_continue(l):
    conti = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text=Templates.cancel_1.get(l), callback_data=Templates.cancel_1.get(l)),
            types.InlineKeyboardButton(text=Templates.accept_1.get(l), callback_data=Templates.accept_1.get(l))
        ]
    ])
    return conti

def order_and_back(l):
    btn = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text=Templates.do_order2.get(l), callback_data=f'{Templates.do_order2.get(l)}')
        ],
        [
            types.InlineKeyboardButton(text=Templates.back.get(l), callback_data=f' {Templates.back.get(l)} ')
        ]
    ])
    
    return btn
