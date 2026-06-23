
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('contacts/', views.contacts,name="contacts"),
    path('data_security/', views.data_security,name="data_security"),
    path('license_policy/', views.license_policy,name="license_policy"),
    path('user_agreement/', views.user_agreement,name="user_agreement"),
    path('dashboard/', views.dashboard,name="dashboard"),
]
