
from django.contrib import admin
from django.urls import path
from .views import MyView,MyRedirectView,MySecondView,BookListView,BookUpdateView,BookCreateView,BookDeleteView


urlpatterns = [
    #path('', views.hello,name='hello'),
    path('',MyView.as_view(),name='hello'),
    path('mysecond/',MySecondView.as_view(),name='hellohello'),
    path('myredirectview/',MyRedirectView.as_view(),name='myredirect'),
    path('books/',BookListView.as_view(),name='book-list'),
    path('update/<int:pk>/',BookUpdateView.as_view(),name='update'),
    path('add/',BookCreateView.as_view(),name='create'),
    path('delete/<int:pk>/',BookDeleteView.as_view(),name='delete')
]