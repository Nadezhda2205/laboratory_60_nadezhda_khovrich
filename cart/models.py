from django.db import models
from products.models import Product


class ProductInCart(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Продукт', on_delete=models.CASCADE, unique=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    
    def __str__(self):
        return f'{self.product.name}: {self.quantity}'
