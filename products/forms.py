from django import forms
from products.models import Product
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'category', 'balance', 'price']


class SearchForm(forms.Form):
    search = forms.CharField(required=False)