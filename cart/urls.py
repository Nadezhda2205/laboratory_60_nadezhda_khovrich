from django.urls import path
from cart.views import cartaddproductview, CartProductsView

urlpatterns = [
    path('add/product/<int:pk>', cartaddproductview, name='cart_add_product'),
    path('', CartProductsView.as_view(), name='cart_products'),
]