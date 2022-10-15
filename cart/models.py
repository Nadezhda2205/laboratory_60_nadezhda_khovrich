from django.db import models
from products.models import Product


class ProductInCart(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    