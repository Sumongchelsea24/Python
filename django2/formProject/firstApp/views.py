from django.shortcuts import render
from firstApp.models import Employee
from firstApp.forms import EmployeeForm

# Create your views here.
def index(request):
  my_obj=Employee.objects.all()
  context={"my_obj":my_obj}
  return render(request,"firstApp/index.html",context=context)

def formIndex(request):
  form=EmployeeForm()
  if request.method=="POST":
    form=EmployeeForm(request.POST)
    if form.is_valid():
      # Employee.objects.create(ename=form.cleaned_data['ename'],eno=form.cleaned_data['eno'] ,esal=form.cleaned_data['esal'],eaddr=form.cleaned_data['eaddr'])
      #Better practice
      form.save(commit=True)
  context={"form":form}
  return render(request,"firstApp/employeerecord.html",context=context)

