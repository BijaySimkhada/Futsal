from django.contrib import admin
from django.urls import path, include
from . import views

#

urlpatterns = [
    path('login', views.returnLogin, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.register, name="register")
]