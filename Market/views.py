from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import F
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from Market.forms import NewProductForm, AddressForm
from Market.models import Product, Listing, Purchase, Cart


@login_required
def add_product(request):
    context = {}
    if request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.owner = request.user
            prod.save()
        context['form'] = form
    return render(request, 'Market/new_product.html', context)


@login_required
def cart(request):
    user = User.objects.get(username=request.session['username'])
    my_cart = user.cart_set.all()
    context = {'my_cart': my_cart}
    return render(request, 'Market/cart.html', context)


@login_required
def my_account(request):
    return render(request, 'Market/Account.html')


@login_required
def my_listings(request):
    my_listing = Product.objects.filter(owner__username=request.session['username'])
    context = {'my_listing': my_listing}
    return render(request, 'Market/Listings.html', context)


@login_required
def order_history(request):
    order_hist = Purchase.objects.filter(user__username=request.session['username'])
    context = {'order_hist': order_hist}
    return render(request, 'Market/Order History.html', context)


@login_required
def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    username = request.GET.get('username')
    user = User.objects.get(username=username)
    product = Product.objects.get(pk=product_id)
    product.stock = product.stock - 1
    product.save()
    cart_obj = Cart.objects.create(buyer=user, product=product)
    cart_obj.save()
    ser_prod = serializers.serialize('json', [product, ])
    return JsonResponse({"prod": ser_prod}, status=200)


@login_required
def delete(request):
    prod_id = request.GET.get('prod_id')
    Product.objects.filter(pk=prod_id).delete()
    return JsonResponse({"valid": True}, status=200)


@login_required
def remove(request):
    cart_id = request.GET.get('cart_id')
    cart_obj = Cart.objects.get(pk=cart_id)
    product = Product.objects.get(pk=cart_obj.product_id)
    product.stock = product.stock + 1
    product.save()
    cart_obj.delete()

    return JsonResponse({"valid": True}, status=200)

@login_required
def checkout(request):
    user = User.objects.get(username=request.session['username'])
    cart_list = user.cart_set.all()
    sum = 0
    for cart_obj in cart_list:
        sum = sum + cart_obj.product.price

    context = {'sum': sum, 'cart_list': cart_list}
    return render(request, 'Market/checkout.html', context)


@login_required
def buy(request):
    username = request.GET.get('user')
    user = User.objects.get(username=username)
    cart_list = user.cart_set.all()
    for cart_obj in cart_list:
        pur = Purchase.objects.create(user=cart_obj.buyer, product_bought=cart_obj.product)
        pur.save()
        cart_obj.delete()
    print(sum)
    return JsonResponse({"valid": True}, status=200)

@login_required
def address(request):
    form = AddressForm(request.POST)
    if form.is_valid():
        addr = form.save()
        ser_instance = serializers.serialize('json', [addr, ])
        return JsonResponse({"instance": ser_instance}, status=200)
    else:
        return JsonResponse({"error": form.errors}, status=400)