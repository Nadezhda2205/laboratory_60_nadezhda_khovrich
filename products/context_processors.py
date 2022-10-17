from products.models import Product
from cart.models import ProductInCart

def get_categories(requesr):
    categories = Product.CATEGORY_CHOICES
    quantity_product_in_cart = ProductInCart.objects.all().count()
    context = {
        'categories': categories,
        'quantity_product_in_cart': quantity_product_in_cart
        }

    return context
    