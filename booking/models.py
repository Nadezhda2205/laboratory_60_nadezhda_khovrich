from django.db import models
from products.models import Product

class Booking(models.Model):
    products = models.ManyToManyField(
        to=Product,
        null=False,
        verbose_name='Продукты', 
        related_name='booking', 
        through='BookingProduct',
        through_fields=('booking', 'product')
        )
    username = models.CharField(verbose_name='Имя пользователя', max_length=100, null=False)
    phone = models.CharField(verbose_name='Телефон', max_length=25, null=False)
    address = models.CharField(verbose_name='Адрес', max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    
    def __str__(self):
        return f'{self.username}: {self.created_at}'

class BookingProduct(models.Model):
    booking = models.ForeignKey(to=Booking, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')


