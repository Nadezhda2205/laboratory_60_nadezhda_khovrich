from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.core.handlers.wsgi import WSGIRequest
from products.forms import ProductForm, SearchForm

def products_view(request: WSGIRequest):
    search = request.GET.get('search')
    if search:
        form = SearchForm(request.GET)

        products = Product.objects.filter(balance__gt=0).order_by('category', 'name').filter(name__iregex=search)
    else:
        products = Product.objects.filter(balance__gt=0).order_by('category', 'name')
        search = ''
        form = SearchForm()

        
    context = {
        'products': products,
        'search': search,
        'form': form
    }
    return render(request=request, template_name='products.html', context=context)

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request=request, template_name='product.html', context=context)

def product_add_view(request:WSGIRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if not form.is_valid():
            context = {
            'choices': Product.CATEGORY_CHOICES,
            'form': form
            }  
            return render(request=request, template_name='product_add.html', context=context)

        product: Product = Product.objects.create(**form.cleaned_data)
        return redirect('product', pk=product.pk)
        
    form = ProductForm()
    context = {
        'choices': Product.CATEGORY_CHOICES,
        'form': form
    }    
    return render(request=request, template_name='product_add.html', context=context)

def product_edit_view(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if not form.is_valid():
            context = {
            'choices': Product.CATEGORY_CHOICES,
            'form': form
            }  
            return render(request=request, template_name='product_edit.html', context=context)

        form.save()
        return redirect('product', pk=product.pk)
        
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    context = {
        'form': form
    }
    return render(request=request, template_name='product_edit.html', context=context)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')