from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('email_check', views.email_check), #Checking if email exists- Ajax request
    path('login', views.login),
    path('welcome', views.welcome_page),
    path('logout', views.logout),
]