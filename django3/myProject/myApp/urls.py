
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contacts/',views.contacts,name="contacts"),
    path('business/',views.business,name="business"),
    path('portfolio',views.portfolio,name="portfolio")
]
