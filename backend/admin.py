from django.contrib import admin
from .models import BotUser,Template,Cake,User_Order,Simple_User_Order

# Register your models here.
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'full_name', 'lang', 'status']
    list_display_links = ['full_name']
    search_fields = ['chat_id', 'full_name']
    
@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body_uz', 'body_ru']
    list_display_links = ['title']
    search_fields = ['title', 'body_uz', 'body_ru']
    
@admin.register(Cake)
class CakesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cake_name', 'cake_price']
    list_display_links = ['title', 'cake_name']
    search_fields = ['title']
     
    
    
@admin.register(User_Order)
class User_OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'cake_name', 'cake_num', 'ordered_date', 'ordered_time', 'status']
    list_display_links = ['cake_name', 'chat_id']
    search_fields = ['ordered_date', 'status', 'cake_name']


@admin.register(Simple_User_Order)
class User_OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'cake_name', 'cake_num', 'ordered_date', 'ordered_time', 'status']
    list_display_links = ['cake_name', 'chat_id']
    search_fields = ['ordered_date', 'status', 'cake_name']
