from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('new_product/', views.add_product, name="new_product"),
    path('account/', views.my_account, name='my_account'),
    path('listings/', views.my_listings, name='my_listings'),
    path('orders/', views.order_history, name='order_history'),
    path('cart/add/', views.add_to_cart, name='add'),
    path('listings/delete', views.delete, name='delete'),
    path('listings/update', views.update, name='update'),
    path('cart/remove', views.remove, name='remove'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('cart/purchase', views.buy, name='buy'),
    path('cart/address', views.address, name='address'),




]