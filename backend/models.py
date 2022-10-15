from typing_extensions import Self
from django.db import models

# Create your models here.
class BotUser(models.Model):
    class Lang(models.TextChoices):
        UZ = 'uz'
        RU = 'ru'
        EN = 'en'
    chat_id = models.IntegerField(default=0)
    full_name = models.CharField(max_length=255)
    lang = models.CharField(max_length=3, choices=Lang.choices, default=Lang.UZ)
    status = models.CharField(max_length=255,default='') 
    
    def __str__(self) -> str:
        return self.full_name
    
class Template(models.Model):
    title = models.CharField(max_length=255)
    body_uz = models.TextField()
    body_ru = models.TextField()
    
    def get(self, lang):
        return getattr(self, f"body_{lang}")
    
class Cake(models.Model):
    title = models.CharField(max_length=255)
    cake_name = models.CharField(max_length=255)
    cake_price = models.IntegerField()
    cake_photo = models.ImageField(upload_to='photos')

    
class User_Order(models.Model):
    chat_id = models.IntegerField()
    cake_name = models.CharField(max_length=255)
    cake_num = models.IntegerField()
    ordered_date = models.CharField(max_length=255)
    ordered_time = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    

class Simple_User_Order(models.Model):
    chat_id = models.IntegerField()
    cake_name = models.CharField(max_length=255)
    cake_num = models.IntegerField()
    ordered_date = models.CharField(max_length=255)
    ordered_time = models.CharField(max_length=255)
    status = models.CharField(max_length=255)