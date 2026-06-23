from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  context={}
  return render(request,'myApp/home.html',context=context)

def contacts(request):
  context={}
  return render(request,'myApp/contacts.html',context=context)

def data_security(request):
  context={}
  return render(request,'myApp/data_security.html',context=context)
def license_policy(request):
  context={}
  return render(request,'myApp/license_policy.html',context=context)
def user_agreement(request):
  context={}
  return render(request,'myApp/user_agreement.html',context=context)
@login_required
def dashboard(request):
  context={}
  return render(request,'myApp/dashboard.html',context=context)


      


