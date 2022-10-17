from products.models import Product

def get_categories(requesr):
    categories = Product.CATEGORY_CHOICES
    context = {'categories': categories}
    return context
    