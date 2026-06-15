from django.contrib import admin
from django.urls import path
from myFirstApp import views

urlpatterns = [
    
    path('',views.display ),
]