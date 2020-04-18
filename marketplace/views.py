from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic


# should use generics but have not learned that yet. Also need to build the back end data structs
from marketplace.forms import SignUpForm


def index(request):
    return render(request, 'browse.html')


def register(request):
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('browse'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
