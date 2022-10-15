import config
from buttons import *
import aiogram
from aiogram import Bot,Dispatcher,executor,types
from backend.models import BotUser,Template
from commands import *
from templates import *
from machine_session import *
from machine import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext



storage = MemoryStorage()
bot = Bot(config.TOKEN,parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)



'''
@dp.message_handler(commands=['login'])
async def login(message: types.Message):
    chat_id = message.chat.id
    if user_exists(BotUser, chat_id):
        pass
    else:
        await Log.msg.set()
        await message.answer(Templates.print_log_pass.get('uz'))
@dp.message_handler(content_types=['text'], state=Log.msg)
async def check_msg(message: types.Message):
    try:
        login,password = message.text.split()
        user_info = BotUser.objects.all()
        for i in user_info:
            if login == i.login and password == i.password and not i.is_used:
                await message.answer(Templates.data_accepted.get('uz'),reply_markup=category(i.lang))
                BotUser(login=i.login).is_used = True
                BotUser(login=i.login).chat_id = message.chat.id
                break
        else:
            await message.answer(Templates.wrong_data.get('uz'))
    except Exception as ex:
        print(ex)
        await message.answer(Templates.wrong_data.get('uz'))
        
    

"""Categories"""

"""     Send message to Admin    """
@dp.message_handler(Text(equals=(Templates.category_2.get('uz'),Templates.category_2.get('ru'))),lambda msg: user_exists(BotUser, msg.from_user.id))
async def get_user_msg(message: types.Message):
    global Lang
    chat_id = message.chat.id
    Lang = BotUser.objects.get(chat_id=chat_id).lang
    await getting_user_message_to_admin.msg.set()
    await message.answer(Templates.print_msg_to_admin.get(Lang))
@dp.message_handler(content_types=['text'], state=getting_user_message_to_admin.msg)
async def getting_msg(message: types.Message, state: FSMContext):
    msg = message.text
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    await bot.send_message(chat_id=-1001788161122, text=f'From:  {user_fullname}\nUser_ID:  {user_id}\nText:  {msg}')
    await message.answer(Templates.sent.get(Lang))
    await state.finish()
changing_lang

"""     Settings     """
@dp.message_handler(Text(equals=(Templates.category_0.get('uz'),Templates.category_0.get('ru'))),lambda msg: user_exists(BotUser,msg.from_user.id))
async def setting(message: types.Message):
    global Lang
    chat_id = message.chat.id
    Lang = BotUser.objects.get(chat_id=chat_id).lang
    await category_0_next_step.ans.set()
    await message.answer(Templates.choose_text.get(Lang),reply_markup=settings_keyboard(Lang))
@dp.message_handler(content_types=['text'], state=category_0_next_step.ans)
async def category_0(message: types.Message, state: FSMContext):
    if message.text == Templates.change_lang.get(Lang):
        await choosing_lang.lang.set()
        await message.answer(Templates.choose_text.get(Lang), reply_markup=changing_lang(Lang))
    elif message.text == Templates.back.get(Lang):
        await message.answer(Templates.menu.get(Lang),reply_markup=category(Lang))
        await state.finish()
@dp.message_handler(content_types=['text'], state=choosing_lang.lang)
async def two_lang(message:types.Message, state: FSMContext):
    id = message.from_user.id
    if message.text == Templates.ru.get(Lang):
        l = 'ru'
    elif message.text == Templates.uz.get(Lang):
        l = 'uz'
    print(l)
    user = BotUser.objects.get(chat_id=id)
    user.lang = l
    user.save()
    #Lang = botdb.get_user_lang(id)
    lang = BotUser.objects.get(chat_id=id).lang
    await message.answer(Templates.lang_changed.get(lang), reply_markup=category(lang))
    await state.finish()


@dp.message_handler(Text(equals=(Templates.category_1.get('uz'),Templates.category_1.get('ru'))),lambda msg: user_exists(BotUser,msg.from_user.id))
async def send_products(message: types.Message):
    global image_index, my_lang
    id = message.from_user.id
    #image_index = botdb.change_image_index(tel_id=id, num=0)
    my_lang = BotUser.objects.get(chat_id=id).lang
    await message.answer(message.text, reply_markup=delete_keyboard)
    await message.answer(Templates.choose_text.get(my_lang), reply_markup=products_buttons(my_lang))
'''






























@dp.message_handler()
async def message_handler(message: types.Message):
    chat_id = message.chat.id
    user, succes = BotUser.objects.get_or_create(chat_id=chat_id)
    if succes:
        user = BotUser.objects.get(chat_id=chat_id)
        user.full_name = message.from_user.full_name
        user.status = 'user'
        user.save()
    lang = BotUser.objects.get(chat_id=chat_id).lang
        
    # THIS LOOP IS MAIN CATEGORIES'
    for name,command in c_c(lang).items():
        if message.text == name:
            print(message.text, name, command)
            await command(message, lang)
            break
    
    if message.text == Templates.by_date.get(lang):
        await order_by_date.date.set()
        await get_orders_by_date(message,lang)
        
    if message.text == Templates.category_2.get(lang):
        await msg_to_admin.msg.set()
        await message.answer(Templates.print_msg_to_admin.get(lang))


@dp.message_handler(content_types=['text'], state=msg_to_admin.msg)
async def send_message(message: types.Message, state: FSMContext):
    await sending_msg(message,bot)
    await state.finish()
        
@dp.message_handler(content_types=['text'], state=order_by_date.date)
async def get_ords(message: types.Message, state: FSMContext):
    await get_order_by_argument(message,'by_date')
    await state.finish()
    
    
    
@dp.callback_query_handler()
async def callback_query(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    user_lang = BotUser.objects.get(chat_id=chat_id).lang
    for c_name,func in cakes_callback_c().items(): 
        if call.data == c_name:
            await func(bot,call,user_lang,call.data.split()[1].lower())
            
                
    for name, func in keyboard_callback(user_lang).items():
        if call.data == name:
            await func(bot, call, user_lang)
            break
        
    for name, func in backs(user_lang).items():
        if call.data == name:
            print(call.data,name)
            await func(call.message, user_lang, bot)
                
                
    await getting_orders(call, user_lang, bot)
    

    













executor.start_polling(dp, skip_updates=True)