from django.shortcuts import render, redirect
from django.http import HttpResponse
from assets.models import *

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required 
# Create your views here.

def home(request):
    return render(request, 'home.html')

def table(request):
    assets = Assets.objects.all()

    return render(request, 'table.html', {'assets' : assets} )

def form(request):
    return render(request, 'form.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email or Password is Incorrect')

    context = {}
    return render(request, 'registration/login.html')

def logoutUser(request):
        logout(request)
        return redirect('login')
