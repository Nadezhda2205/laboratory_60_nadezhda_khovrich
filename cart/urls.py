from django.urls import path
from cart.views import cartaddproductview, CartProductsView, CartInProductDeleteView

urlpatterns = [
    path('add/product/<int:pk>', cartaddproductview, name='cart_add_product'),
    path('', CartProductsView.as_view(), name='cart_products'),
    path('product/delete/<int:pk>', CartInProductDeleteView.as_view(), name='cart_product_delete'),
    
]