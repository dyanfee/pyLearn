from django.db import models

# Create your models here.
# https://code.ziqiangxuetang.com/django/django-models.html

# QuerySet
# https://code.ziqiangxuetang.com/django/django-queryset-api.html
class Person(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()

    def __str__(self):
        return self.name