from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from cart.models import ProductInCart
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy


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


class CartProductsView(ListView):
    model = ProductInCart
    template_name = 'cart/cart_products.html'
    context_object_name = 'productsincart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productsincart = ProductInCart.objects.all()
        total = 0
        for productincart in productsincart:
            price = productincart.product.price
            quantity = productincart.quantity
            total += price * quantity
        context['total'] = total
        return context


class CartInProductDeleteView(DeleteView):
    template_name = 'cart/cart_products.html'
    model = ProductInCart
    success_url = reverse_lazy('cart_products')

