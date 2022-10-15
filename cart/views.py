from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from cart.models import ProductInCart


def cartaddproductview(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.balance == 0:
        return redirect('products')
    products = ProductInCart.objects.all().values('product')
    print(products)
    products_list = []
    for item in products:
        products_list.append(item.get('product'))
    print(products_list)
    if pk in products_list:
        productInCart = ProductInCart.objects.get(product=pk)
        productInCart.quantity += 1
        if productInCart.quantity > product.balance:
            return redirect('products')
        productInCart.save()
        print(productInCart)
    else:
        productInCart = ProductInCart(product=product, quantity=1)
        productInCart.save()
    return redirect('products')
