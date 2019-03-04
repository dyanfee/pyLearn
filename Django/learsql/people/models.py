from django.db import models

# Create your models here.
# https://code.ziqiangxuetang.com/django/django-models.html

class Person(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()