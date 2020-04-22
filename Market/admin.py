from django.contrib import admin

# Register your models here.
from Market.models import Product, Listing, Cart, Purchase

admin.site.register(Product)
admin.site.register(Listing)
admin.site.register(Cart)
admin.site.register(Purchase)
