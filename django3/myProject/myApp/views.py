from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

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
  return render(request,'myApp/contacts.html')

def business(request):
  return render(request,'myApp/business.html')

def portfolio(request):
  return render(request,'myApp/portfolio.html')
