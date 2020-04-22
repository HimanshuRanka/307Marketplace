from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from Market.models import Product
from . import forms


# should use generics but have not learned that yet. Also need to build the back end data structs

def index(request):
    products = Product.objects.all().order_by('-pub_date')[:20]
    context = {'products': products}
    return render(request, 'account/browse.html', context)


def register(request):
    context = {}
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'])
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                return HttpResponseRedirect(reverse('user_login'))
            except IntegrityError:
                form.add_error('username', 'Username is taken')

        context['form'] = form
    return render(request, 'account/signup.html', context)


def user_login(request):
    context = {}
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                request.session['username'] = form.cleaned_data['username']
                request.session['email'] = user.email
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect(reverse('home'))
            else:
                form.add_error(None, 'Unable to log in')
        context['form'] = form
    return render(request, 'account/login.html', context)


def user_logout(request):	
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

