from aiogram import types,Bot
from buttons import *
import aiogram
from aiogram.dispatcher.storage import FSMContext
import datetime
from backend.models import BotUser,Cake, Simple_User_Order,User_Order
from templates import Templates
from variables.models import CakeDescription, Category_msg, Going_to_Order, Total_num, Where_User



def user_exists(BotUser: BotUser, chat_id):
    try:
        BotUser.objects.get(chat_id=chat_id).full_name
        r = True
        return r
    except Exception as ex:
        print(ex)
        r = False
        return r
    
    
def get_daate(date):
    d = str(date).split()[0]
    return d


def make_description(l,cake_name, cake_price):
    result = f'<b>➖➖➖➖➖➖➖\n{Templates.name.get(l)}  {cake_name}\n➖➖➖➖➖➖➖\n{Templates.price.get(l)}  💰 {format(cake_price, ",d")} {Templates.sum.get(l)}\n➖➖➖➖➖➖➖</b>'
    return result

def make_d(l,date, cake_name, num):
    result = f'<b>{Templates.date.get(l)}  {date}\n{Templates.name.get(l)}  {cake_name}\n{Templates.num.get(l)}  {num}</b>'
    return result


# Main categories functions
async def Settings(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'menu':
        await message.answer(Templates.choose_text.get(lang),reply_markup=settings_keyboard(lang))
        location.location = 'settings_category'
        location.save()

async def Product(message: types.Message, lang, bot=''):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location in ['menu']:
        msg = await message.answer(Templates.category.get(lang)+message.text, reply_markup=delete_keyboard)
        await message.answer(Templates.choose_text.get(lang), reply_markup=products_buttons(lang))
        try:
            c = Category_msg.objects.get(chat_id=message.chat.id,title='product')
            c.text_id = msg.message_id
            c.save()
        except:
            Category_msg.objects.create(chat_id=message.chat.id, text_id=msg.message_id, title='product')
        location.location = 'product_category'
        location.save()

async def Send_Message(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'menu':
        await message.answer(Templates.not_works_yet.get(lang))
        #location.location = 'send_message_category'
        #location.save()


async def Orders(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'menu':
        await message.answer(Templates.choose_text.get(lang), reply_markup=order_category(lang))
        location.location = 'orders_category'
        location.save()



async def send_menu(message: types.Message, lang, bot=None):
    await message.delete()
    try:
        await bot.delete_message(chat_id=message.chat.id,message_id=Category_msg.objects.get(chat_id=message.chat.id,title='product').text_id)
    except Exception as ex:
        print(ex)
        
    try:
        await bot.delete_message(chat_id=message.chat.id,message_id=Category_msg.objects.get(chat_id=message.chat.id,title='bucket').text_id)
    except Exception as ex:
        print(ex)
        
        
    try:
        r = Where_User.objects.get(chat_id=message.chat.id)
        r.location = 'menu'
        r.save()
    except:
        Where_User.objects.create(location='menu', chat_id=message.chat.id)
    await message.answer(Templates.menu.get(lang), reply_markup=category(lang))


# Settings commands

async def Changing_lang(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'settings_category':
        await message.answer(Templates.choose_text.get(lang), reply_markup=changing_lang(lang))
        location.location = 'changing_lang'
        location.save()
        
async def Back(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location in ['settings_category', 'orders_category']:
        await message.answer(Templates.menu.get(lang), reply_markup=category(lang))
        location.location = 'menu'
        location.save()

async def lang_ru(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'changing_lang':
        id = message.from_user.id
        user = BotUser.objects.get(chat_id=id)
        user.lang = 'ru'
        user.save()
        lang = BotUser.objects.get(chat_id=id).lang
        await message.answer(Templates.lang_changed.get(lang), reply_markup=settings_keyboard(lang))
        location.location = 'settings_category'
        location.save()

async def lang_uz(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'changing_lang':
        id = message.from_user.id
        user = BotUser.objects.get(chat_id=id)
        user.lang = 'uz'
        user.save()
        lang = BotUser.objects.get(chat_id=id).lang
        await message.answer(Templates.lang_changed.get(lang), reply_markup=settings_keyboard(lang))
        location.location = 'settings_category'
        location.save()

async def all_cakes(bot: aiogram.Bot,call: types.CallbackQuery, lang, c_name=''):
    cake = Cake.objects.get(title=c_name)
    cake_name = cake.cake_name
    cake_price = cake.cake_price
    description = make_description(lang,cake_name,cake_price)
    #msg = await call.message.edit_text(description,reply_markup=order_and_back(lang))
    print(cake.cake_photo)
    photo = open(f'{cake.cake_photo}','rb')
    await call.message.delete()
    await bot.send_photo(call.message.chat.id,photo=photo,caption=description,reply_markup=order_and_back(lang))
        
    try:
        ord = Going_to_Order.objects.get(chat_id=call.message.chat.id)
        ord.name = cake_name
        ord.save()
    except:
        Going_to_Order.objects.create(name=cake_name, chat_id=call.message.chat.id)
    
    #await call.message.answer(result,reply_markup=order_and_back(lang))
    

async def back_to_products(message: types.Message, lang, bot):
    await message.delete()
    await message.answer(Templates.choose_text.get(lang), reply_markup=products_buttons(lang))
    
async def doing_order(message: types.Message, lang, bot):
    await message.delete_reply_markup()
    try:
        r = Total_num.objects.get(chat_id=message.chat.id)
        r.num = 0
        r.save()
    except:
        Total_num.objects.create(chat_id=message.chat.id, num='')
    await message.delete()
    nm = Going_to_Order.objects.get(chat_id=message.chat.id).name
    msg = await message.answer(f'Ism:  {nm}\nNarxi: {Cake.objects.get(cake_name=nm).cake_price}')
    try:
        r = CakeDescription.objects.get(chat_id=message.chat.id)
        r.ids = msg.message_id
        r.save()
    except:
        CakeDescription.objects.create(ids=msg.message_id, chat_id=message.chat.id)
    await message.answer(Templates.box_quantity.get(lang),reply_markup=calculator_keyboard(lang))

async def back_to_products_2(message: types.Message, lang, bot):
    id = CakeDescription.objects.get(chat_id=message.chat.id).ids
    await bot.delete_message(chat_id=message.chat.id, message_id=id)
    await message.edit_text(Templates.choose_text.get(lang), reply_markup=products_buttons(lang))

def two_date(d):
    d = str(d).split()
    date = d[0]
    time = d[1].split('.')[0]
    return [date,time]
    
    


async def keyboard(bot: Bot, cd: types.CallbackQuery, my_lang):
    data = cd.data
    user_id = cd.message.chat.id
    data = cd.data
    if data == 'ok':
        total_num = Total_num.objects.get(chat_id=user_id).num
        if total_num in ['','0']:
            await cd.answer(Templates.print_boxes_num.get(my_lang))
        else:
            await cd.answer(Templates.added_to_bucket.get(my_lang),show_alert=True)
            await cd.message.answer(Templates.Continue.get(my_lang), reply_markup=do_continue(my_lang))
            r = Total_num.objects.get(chat_id=user_id)
            
            
            cake_name = Going_to_Order.objects.get(chat_id=user_id).name

            res = two_date(datetime.datetime.today())
            user_status = BotUser.objects.get(chat_id=user_id).status
            if user_status == 'user':
                user_order = Simple_User_Order.objects.create(chat_id=user_id, cake_name=cake_name, cake_num=r.num, ordered_date=res[0], ordered_time=res[1], status='in_bucket')
            else:
                user_order = User_Order.objects.create(chat_id=user_id, cake_name=cake_name, cake_num=r.num, ordered_date=res[0], ordered_time=res[1], status='in_bucket')
                
            r.num = '0'
            r.save()

    if data == 'ok' and total_num not in ['','0']:
        try:
            #await bot.delete_message(chat_id=cd.message.chat.id,message_id=box_num_msg_id)
            
            await cd.message.delete()
            id = CakeDescription.objects.get(chat_id=cd.message.chat.id).ids
            await bot.delete_message(chat_id=cd.message.chat.id, message_id=id)
            r = Total_num.objects.get(chat_id=user_id)
            r.num = '0'
            r.save()
        except:
            pass
    else:
        total_num = Total_num.objects.get(chat_id=user_id).num
        if data == 'c':
            r = Total_num.objects.get(chat_id=user_id)
            r.num = '0'
            r.save()
            await cd.message.edit_text(f'{Templates.box_quantity.get(my_lang)}', reply_markup=calculator_keyboard(my_lang))
        else:
            t = Total_num.objects.get(chat_id=user_id)
            t.num += data
            t.save()
            total_num = Total_num.objects.get(chat_id=user_id)
            if total_num.num[0] == '0':
                total_num.num = total_num.num[1:]
                total_num.save()
            await cd.message.edit_text(f'{Templates.box_quantity.get(my_lang)}  {total_num.num}', reply_markup=calculator_keyboard(my_lang))
    await bot.answer_callback_query(cd.id)

    # user goes to the Bucket




def get_orders(message: types.Message, lang):
    r = ''
    s = 0
    if BotUser.objects.get(chat_id=message.chat.id).status == 'client':
        orders = User_Order.objects.filter(chat_id=message.chat.id, status='in_bucket')
    else:
        orders = Simple_User_Order.objects.filter(chat_id=message.chat.id, status='in_bucket')
    btn = types.InlineKeyboardMarkup(row_width=5)
    total_price = 0
    call_data = []
    if len(orders) == 0:
        return None
    else:
        for i in orders:
            s += 1
            cake_name = i.cake_name
            cake_num = i.cake_num
            btn.add(
                types.InlineKeyboardButton(text=f'{s}. ❌ '+cake_name, callback_data=f'id {i.pk}'),
            )
            cake_price = Cake.objects.get(cake_name=cake_name).cake_price
            total_price += cake_price*cake_num
            r += f'{s}. {cake_name}:\n<code>{cake_num} x {cake_price} = {format(cake_num*cake_price, ",d")}</code>\n\n'
    r += f'Umumiy:  {format(total_price, ",d")} so`m'
    btn.row(
        types.InlineKeyboardButton(text=Templates.back.get(lang), callback_data=f' {Templates.back.get(lang)}'),
        types.InlineKeyboardButton(text=Templates.do_order.get(lang), callback_data='id do_order')
        )

    return [r,btn,s]


async def get_orders_from_bucket(message: types.Message, lang, bot=''):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location in ['menu','product_category']:
        if location.location == 'product_category':
            await bot.delete_message(chat_id=message.chat.id, message_id=Category_msg.objects.get(chat_id=message.chat.id,title='product').text_id) 
        r = get_orders(message, lang)
        if r is None:
            if location.location == 'product_category':
                await message.delete()
            await message.answer(Templates.no_orders.get(lang), reply_markup=category(lang))
                
        else:
            if location.location == 'menu':
                msg = await message.answer(Templates.category.get(lang)+message.text,reply_markup=delete_keyboard)
                await message.answer(r[0], reply_markup=r[1])
                try:
                    c = Category_msg.objects.get(chat_id=message.chat.id,title='bucket')
                    c.text_id = msg.message_id
                    c.save()
                except:
                    Category_msg.objects.create(chat_id=message.chat.id, text_id=msg.message_id, title='bucket')
            else:
                await message.edit_text(r[0], reply_markup=r[1])
            location.location = 'bucket_category'
            location.save()
        
async def bucket_buttons(call: types.CallbackQuery, lang, bot):
    data = call.data.split()
    user_status = BotUser.objects.get(chat_id=call.message.chat.id).status
    if data[1] != 'do_order':
        if user_status == 'client':
            order = User_Order.objects.get(pk=int(data[1]))
        else:
            order = Simple_User_Order.objects.get(pk=int(data[1]))
    try:
        if data[1] == 'do_order':
            await call.answer(Templates.order_accepted.get(lang), show_alert=True)
            if user_status == 'client':
                orders_in_bucket = User_Order.objects.filter(chat_id=call.message.chat.id,status='in_bucket')
            else:
                orders_in_bucket = Simple_User_Order.objects.filter(chat_id=call.message.chat.id,status='in_bucket')
            for i in orders_in_bucket:
                i.status = 'ordered'
                i.save()
            await call.message.delete()
            try:
                await bot.delete_message(chat_id=call.message.chat.id, message_id=Category_msg.objects.get(chat_id=call.message.chat.id,title='bucket').text_id) 
            except:
                pass
            await call.message.answer(Templates.menu.get(lang), reply_markup=category(lang))
            location = Where_User.objects.get(chat_id=call.message.chat.id)
            location.location = 'menu'
            location.save()
            
            
        else:
            order.status = 'cancelled'
            order.save()
            r = get_orders(call.message, lang)
            await call.message.edit_text(r[0],reply_markup=r[1])
        
        
    except:
        await call.message.delete()
        await call.answer(Templates.no_orders.get(lang))
        await call.message.answer(Templates.menu.get(lang), reply_markup=category(lang))
        location = Where_User.objects.get(chat_id=call.message.chat.id)
        location.location = 'menu'
        location.save()

async def get_order_by_argument(message: types.Message, date):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'orders_category':
        r = ''
        s = 0
        if date == 'today':
            d = two_date(datetime.datetime.now())[0]
        elif date == 'by_date':
            d = str(message.text)
        if BotUser.objects.get(chat_id=message.chat.id).status == 'client':
            user_orders = User_Order.objects.filter(chat_id=message.chat.id, ordered_date=d)
        else:
            user_orders = Simple_User_Order.objects.filter(chat_id=message.chat.id, ordered_date=d)
        for num,i in enumerate(user_orders):
            cake_price = Cake.objects.get(cake_name=i.cake_name).cake_price
            r += f'{num+1}. {i.cake_name}:\nSana: {i.ordered_date} {i.ordered_time}\n<code>{i.cake_num} x {cake_price} = {format(i.cake_num*cake_price, ",d")}</code>\n\n'
            s += i.cake_num*cake_price
        r += f'Umumiy: {format(s, ",d")} So`m'
        await message.answer(r)

async def get_orders_by_date(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'orders_category':
        await message.answer(Templates.print_date.get(lang))


async def get_today_orders(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'orders_category':
        await get_order_by_argument(message, 'today')


async def get_all_orders(message: types.Message, lang):
    location = Where_User.objects.get(chat_id=message.chat.id)
    if location.location == 'orders_category':
        pass

async def sending_msg(message: types.Message,bot:Bot):
    text = str(message.text)
    chat_id = message.chat.id
    user_name = BotUser.objects.get(chat_id=chat_id).full_name
    await bot.send_message(chat_id=-1001788161122, text=f'Ism: {user_name}\nID: {chat_id}\nXabar: {text}')

def c_c(lang):
    category_commands = {
        '/start': send_menu,
        Templates.category_0.get(lang): Settings,#settings
        Templates.category_1.get(lang): Product,#products
        Templates.category_3.get(lang): Orders,#orders
        Templates.category_4.get(lang): get_orders_from_bucket, #bucket
        Templates.change_lang.get(lang): Changing_lang,#Change language
        Templates.back.get(lang): Back, #Back
        Templates.ru.get(lang): lang_ru, #Language Ru
        Templates.todays_orders.get(lang): get_today_orders,
        Templates.uz.get(lang): lang_uz, #Language Uz
        Templates.all_orders.get(lang): ''
    }
    return category_commands


def cakes_callback_c():
    callback_commands = {}
    for i in Cake.objects.all():
        callback_commands[i.cake_name] = all_cakes
    return callback_commands

def backs(lang):
    back = {
        f' {Templates.back.get(lang)} ': back_to_products,
        f' {Templates.back.get(lang)}': send_menu,
        Templates.do_order2.get(lang): doing_order,
        f'{Templates.back.get(lang)} ': back_to_products_2,
        Templates.accept_1.get(lang): back_to_products,
        Templates.cancel_1.get(lang): get_orders_from_bucket,
    }
    return back

def keyboard_callback(lang):
    keyboard_c = {}
    for i in range(0,10):
        keyboard_c[str(i)] = keyboard
    keyboard_c['c'] = keyboard
    keyboard_c['ok'] = keyboard
    
    return keyboard_c

async def getting_orders(call: types.CallbackQuery, lang, bot):
    if call.data.split()[0] == 'id':
        await bucket_buttons(call, lang, bot)

