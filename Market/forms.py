from django.forms import ModelForm
from .models import Product, Address
from django import forms


class NewProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_picture', 'product_name', 'description', 'price', 'stock', 'category']


class AddressForm(ModelForm):
    line_two = forms.CharField(required=False)
    Country = forms.CharField(required=False)

    class Meta:
        model = Address
        fields = ['line_one', 'line_two', 'city', 'province', 'Country', 'Zipcode', 'user']
        widgets = {'user': forms.HiddenInput()}


class UpdateProductForm(ModelForm):
    prodid = forms.IntegerField()

    class Meta:
        model = Product
        fields = ['description', 'price', 'stock', 'prodid']
        widgets = {'prodid': forms.HiddenInput()}
