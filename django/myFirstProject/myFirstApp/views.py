from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
  s = '<h1 style="color: blue; text-align: center;">Hello this is my first request.</h1>'
  return HttpResponse(s)
 
