
from django.contrib import admin
from django.urls import path
from products.views import ProductListView, ProductDetailView, product_add_view, product_delete_view, product_edit_view, product_confirm_delete, products_category_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/add/', product_add_view, name='product_add'),
    path('product/edit/<int:pk>', product_edit_view, name='product_edit'),
    path('product/delete/<int:pk>', product_delete_view, name='product_delete'),
    path('product/confirm-delete/<int:pk>', product_confirm_delete, name='product_confirm_delete'),
    path('products/<str:category>', products_category_view, name='products_category_view'),
]
