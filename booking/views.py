from django.shortcuts import redirect
from booking.models import Booking, BookingProduct
from booking.forms import BookingForm
from django.core.handlers.wsgi import WSGIRequest
from cart.models import ProductInCart


def booking_add_view(request: WSGIRequest):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():

            booking: Booking = Booking.objects.create(**form.cleaned_data)
    products_in_cart = ProductInCart.objects.all()
    for product_in_cart in products_in_cart:
        BookingProduct.objects.create(booking=booking, product=product_in_cart.product, quantity=product_in_cart.quantity)
    ProductInCart.objects.all().delete()

    return redirect('products')
