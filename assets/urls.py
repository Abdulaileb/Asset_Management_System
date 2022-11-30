from django.urls import path
from .views import AssetsListView, loginPage
from . import views

urlpatterns = [
    path('', AssetsListView.as_view(), name='home'),
    path('login/', views.loginPage, name="login")
]