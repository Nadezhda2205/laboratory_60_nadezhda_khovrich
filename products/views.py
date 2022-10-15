from dataclasses import field
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.core.handlers.wsgi import WSGIRequest
from products.forms import ProductForm, SearchForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse


class ProductListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'
    ordering = ('category', 'name')
    paginate_by = 6
    paginate_orphans = 2

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        context['categories'] = Product.CATEGORY_CHOICES
        return context


    def get_queryset(self):
        queryset = super().get_queryset().filter(balance__gt=0)
        if self.search_value:
            queryset = queryset.filter(name__iregex=self.search_value)
        return queryset


class ProductDetailView(DetailView):
    template_name: str = 'product.html'
    model = Product
    context_object_name = 'product'




# def product_add_view(request:WSGIRequest):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if not form.is_valid():
#             context = {
#             'choices': Product.CATEGORY_CHOICES,
#             'form': form
#             }  
#             return render(request=request, template_name='product_add.html', context=context)

#         product: Product = Product.objects.create(**form.cleaned_data)
#         return redirect('product', pk=product.pk)
        
#     form = ProductForm()
#     context = {
#         'choices': Product.CATEGORY_CHOICES,
#         'form': form
#     }    
#     return render(request=request, template_name='product_add.html', context=context)




class ProductCreateView(CreateView):
    template_name: str = 'product_add.html'
    model = Product
    fields = ('name', 'description', 'photo', 'category', 'balance', 'price')
    
    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


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
    context = {
        'product': product
    }
    return render(request, 'product_confirm_delete.html', context)

    
def product_confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')

def products_category_view(request, category):
    products = Product.objects.filter(category=category)
    for item in Product.CATEGORY_CHOICES:
        if category == item[0]:
            category = item[1]
            break
    context = {
        'category': category,
        'categories': Product.CATEGORY_CHOICES,
        'products': products 
    }
    return render(request, 'products_category.html', context)
