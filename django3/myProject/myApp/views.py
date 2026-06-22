from django.shortcuts import render,redirect
from .models import Employee
from .forms import *

# Create your views here.
def home(request):
  employees=Employee.objects.all()
  if request.method=="POST":
    form=EmployeeForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
      form=EmployeeForm()
  context={
    "employees":employees,
    'form':form
  }
  return render(request,'myApp/home.html',context=context)
def contacts(request):
  count =int(request.COOKIES.get('count',0))
  newcount=count+1
  context={'count':newcount}
  response=render(request,'myApp/contacts.html',context=context)
  response.set_cookie('count',newcount,max_age=60)
  return response

def business(request):
  return render(request,'myApp/business.html')

def portfolio(request):
  return render(request,'myApp/portfolio.html')

def name_view(request):
  form=NameForm()
  context={'form':form}
  return render(request,'myApp/name.html',context=context)

def age_view(request):
  name=request.GET['name']
  request.session['name']=name
  form=AgeForm()
  context={'form':form}
  return render(request,'myApp/age.html',context=context)

def salary_view(request):
  age=request.GET['age']
  request.session['age']=age
  form=SalaryForm()
  context={'form':form}
  return render(request,'myApp/salary.html',context=context)

def result_view(request):
  salary=request.GET['salary']
  request.session['salary']=salary
  context={}
  return render(request,'myApp/result.html',context=context)
