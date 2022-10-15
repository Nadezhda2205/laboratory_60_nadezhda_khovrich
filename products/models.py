from email.policy import default
from random import choices
from django.db import models

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('milk', 'Молочные'),
        ('meat', 'Мясные'),
        ('bread', 'Хлебобулочные'),
        ('juice', 'Соки'),
        ('other', 'Разное'),
    ]

    name = models.CharField(verbose_name='Наименование', max_length=100, null=False)
    description = models.TextField(verbose_name='Описание', max_length=2000, null=True, blank=True)
    photo = models.TextField(verbose_name='Фото', max_length=2000, null=True, blank=True)
    category = models.CharField(
        verbose_name='Категория', 
        max_length=10, 
        choices=CATEGORY_CHOICES, 
        default='other'
        )
    balance = models.PositiveIntegerField(verbose_name='Остаток', null=False)
    price = models.DecimalField(verbose_name='Стоимость', null=False, max_digits=7, decimal_places=2)


    def __str__(self):
        return self.name

