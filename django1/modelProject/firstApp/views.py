from django.shortcuts import render
from firstApp.models import Employee

# Create your views here.
def index(request):
  emp_list=Employee.objects.all()
  context={'emp_list':emp_list}
  return render(request,"firstApp/index.html",context=context)
