from django.shortcuts import redirect, get_object_or_404
from products.models import Product
from cart.models import ProductInCart
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from booking.forms import BookingForm


def cartaddproductview(request, pk):
    product = get_object_or_404(Product, pk=pk)
    quantity = request.POST.get('quantity')
    print(quantity)
    if product.balance == 0:
        return redirect('products')
    products = ProductInCart.objects.all().values('product')
    products_list = []
    for item in products:
        products_list.append(item.get('product'))
    if pk in products_list:
        productInCart = ProductInCart.objects.get(product=pk)
        productInCart.quantity += quantity
        if productInCart.quantity > product.balance:
            return redirect('products')
        productInCart.save()
    else:
        productInCart = ProductInCart(product=product, quantity=quantity)
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
        context['bookingform'] = BookingForm()

        return context


class CartInProductDeleteView(DeleteView):
    template_name = 'cart/cart_products.html'
    model = ProductInCart
    success_url = reverse_lazy('cart_products')

