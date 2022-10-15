from django.urls import path
from cart.views import cartaddproductview

urlpatterns = [
    path('add/product/<int:pk>', cartaddproductview, name='cart_add_product'),
]