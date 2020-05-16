from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showIndex, name="home"),
    path('booking/<str:name>', views.showBooking, name="booking")
]