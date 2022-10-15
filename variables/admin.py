from django.contrib import admin
from .models import CakeDescription, Total_num, Going_to_Order,Where_User,Category_msg

# Register your models here.
@admin.register(CakeDescription)
class CakesDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'ids']
    
@admin.register(Total_num)
class Total_numAdmin(admin.ModelAdmin):
    list_display = ['id', 'num']
    
@admin.register(Going_to_Order)
class Going_to_OrderAdmin(admin.ModelAdmin):
    list_display = ['id','chat_id','name']
    
@admin.register(Where_User)
class Where_UserAdmin(admin.ModelAdmin):
    list_display = ['id','chat_id','location']
    
@admin.register(Category_msg)
class Category_msgAdmin(admin.ModelAdmin):
    list_display = ['id','chat_id','text_id', 'title']