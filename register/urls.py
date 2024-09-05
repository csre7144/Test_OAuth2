from django.urls import path, include
from . import views
from allauth.account.views import LoginView

urlpatterns = [
    path('homepage/', views.home, name='home'),
    path('register_list/', views.register_list, name='register_list'),
    path('', views.signin_list, name='signin_list'), 
    
]