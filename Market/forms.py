from django.forms import ModelForm
from .models import Product
from django import forms


class NewProductForm(ModelForm):
    product_picture = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['product', 'product_picture', 'description', 'price', 'stock']
