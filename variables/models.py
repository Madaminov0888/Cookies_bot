from email.policy import default
from django.db import models

# Create your models here.
class CakeDescription(models.Model):
    chat_id = models.IntegerField(default=0)
    ids = models.IntegerField()
    
class Total_num(models.Model):
    chat_id = models.IntegerField(default=0)
    num = models.CharField(max_length=255,default='')

class Going_to_Order(models.Model):
    chat_id = models.IntegerField(default=0)
    name = models.CharField(max_length=255)

class Where_User(models.Model):
    chat_id = models.IntegerField(default=0)
    location = models.CharField(max_length=255)

class Category_msg(models.Model):
    title = models.CharField(max_length=255,default='')
    chat_id = models.IntegerField(default=0)
    text_id = models.CharField(max_length=255)
