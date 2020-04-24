from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('cart/add/', views.add_to_cart, name='add'),
    path('cart/remove', views.remove, name='remove'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('cart/purchase', views.buy, name='buy'),
    path('cart/address', views.address, name='address'),
    path('new_product/', views.add_product, name="new_product"),
    path('account/', views.my_account, name='my_account'),
    path('listings/', views.my_listings, name='my_listings'),
    path('listings/delete', views.delete, name='delete'),
    path('listings/update', views.update, name='update'),
    path('orders/', views.order_history, name='order_history'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
