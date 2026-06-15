from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def secondindex(request):
  s='<h1 style="color: blue; text-align: center;">Second App response</h1>'
  return HttpResponse(s)
