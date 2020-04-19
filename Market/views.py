from django.shortcuts import render

# Create your views here.
from Market.forms import NewProductForm
from Market.models import Product


def add_product(request):
    context = {}
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.owner = request.user
            prod.save()
        context['form'] = form
    return render(request, 'Market/new_product.html', context)


def cart(request):
    # cart_list = Product.objects.order_by('price')
    # context = {'cart_list': cart_list}
    return render(request, 'Market/cart.html')
