from django.shortcuts import render


# Create your views here.
def display(request):
  my_dict={
    'name':"Rahul",
     'age':20
  }
  return render(request,'myFirstApp/html/index.html',context=my_dict)
 
