from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Assets

from django.contrib.auth import authenticate, login, logout

# Create your views here.

class AssetsListView(ListView):
    model = Assets
    template_name = 'home.html'

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'registration/login.html')
