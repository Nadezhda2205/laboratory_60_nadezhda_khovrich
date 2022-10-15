from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.core.handlers.wsgi import WSGIRequest
from products.forms import ProductForm, SearchForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


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


class ProductCreateView(CreateView):
    template_name: str = 'product_add.html'
    model = Product
    fields = ('name', 'description', 'photo', 'category', 'balance', 'price')
    
    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'products'

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('products')


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
