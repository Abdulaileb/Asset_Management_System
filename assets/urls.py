from django.urls import path
from .views import loginPage
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    path('table/', views.table, name="table"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.loginPage, name="logout"),
    
]