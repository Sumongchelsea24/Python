
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contacts/',views.contacts,name="contacts"),
    path('business/',views.business,name="business"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('name/',views.name_view,name="name"),
    path('age/',views.age_view,name="age"),
    path('salary/',views.salary_view,name="salary"),
    path('result/',views.result_view,name="result"),
    
]
