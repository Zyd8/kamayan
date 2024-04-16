from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from shopitem import views 


urlpatterns = [
    path('', views.sell , name="sell")
]