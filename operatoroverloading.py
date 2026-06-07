#overloading 
# print(10+20)
# print("Hello"+"World")

# class Book:
#   def __init__(self,pages):
#     self.pages=pages
#   def __add__(self, other):
#     return self.pages + other.pages
  
# b1=Book(200)
# b2=Book(100)
# print(b1+b2)

# class Student:
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks=marks
#   def __gt__(self, other):
#     return self.marks>other.marks
#   def __ge__(self, other):
#     return self.marks>=other.marks
# s=Student("Dipesh",99)
# s1=Student("Rupesh",97)
# print(s>s1)
# print(s>=s1)

# class Employee:
#   def __init__(self,name,salary):
#     self.name=name
#     self.salary=salary
#   def __mul__(self, other):
#     return self.salary * other.days
# class AttendenceSheet:
#   def __init__(self,name,days):
#     self.name=name
#     self.days=days
# e=Employee("Alina",5000);
# t=AttendenceSheet("Alina",15)
# print("Total Salary:" ,e*t)

# class Student:
#   def __init__(self,name,roll,marks):
#     self.name=name
#     self.marks=marks
#     self.roll=roll
#   def __str__(self):
#     return f"This is {self.name} object"
# s1=Student("Sujan",101,90)
# s2=Student("Sangita",202,99)
# print(s1)
# print(s2)

# class Book:
#   def __init__(self,pages):
#     self.pages=pages
#   def __add__(self, other):
#     #return self.pages + other.pages
#     return Book(self.pages+other.pages)
#   def __str__(self):
#     return f"Total Number of pages is {self.pages}"
#   def __mul__(self,other):
#     print("This is multiplication")
#     return Book(self.pages*other.pages)
   
  
# b1=Book(200)
# b2=Book(100)
# b3=Book(100)
# b4=Book(900)
# #print(b1+b2+b3)
# print(b1+b2*b3+b4)


#Concept of method overloading in python is not possible in pyhton
# class Test:
#   def m1(self):
#     print("No-arg method")
#   def m1(self,a):
#     print("One-arg method")
#   def m1(self,a,b):
#     print("Two-arg method")
# a=Test()
# a.m1()#Error aauxa

#But we can
# class Test:
#   def sum(self,a=None,b=None,c=None):
#     if a!=None and b!=None and c!=None:
#       print("The sum of  numbers is : ",a+b+c)
#     elif a!=None and b!=None:
#       print("The sum of numbers is : ",a+b)
#     else:
#       print("Please give two or three numbers to add")
# a=Test()
# #a.sum(10)
# a.sum()
# a.sum(10,20,30)
# a.sum(10,20)


# class Test:
#   def sum(self,*a):
#     total=0
#     for x in a:
#       total=total+x
#     print("The sum is : ",total)
# t=Test()
# t.sum()
# t.sum(10)
# t.sum(10,29)
# t.sum(19,30,13)
# t.sum(10,20,30,90,301)

# class Test:
#   def __init__(self):
#     print("No arg constructor")
#   def __init__(self, a):
#     print("one arg constructor")
#   def __init__(self, a,b):
#     print("Two arg constructor")
# t=Test(10,20)#lastko consturtor call hunxa


# class Test:
#   def __init__(self,*a):
#     print("Constructor with different arguments")
# #t=Test()
# t=Test(10,30,50)