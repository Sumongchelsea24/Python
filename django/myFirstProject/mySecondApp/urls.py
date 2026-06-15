from django.contrib import admin
from django.urls import path
from mySecondApp import views

urlpatterns = [
    
    path('second/',views.secondindex),
]