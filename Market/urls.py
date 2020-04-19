from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('new_product/', views.add_product, name="new_product"),

]