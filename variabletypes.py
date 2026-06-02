# class Student:
#   college_name="ACEM" #class variable or static variable
#   def __init__(self,name,rollno):
#     self.name=name #instance variable
#     self.rollno=rollno #instance variable
#   def getStudentInfo(self):
#     #self.age=36 #instance variable
#     print("Student created successfully !")
#     print("Name :",self.name)
#     print("Roll No :",self.rollno)
#     for i in range(10):# here i is local variable
#       print(i)
#   @classmethod #class method
#   def getCollegeInfo(cls):
#     print("College Name :",cls.college_name)
#   @staticmethod #static method: tempoary use ko lagi
#   def m1(a,b):
#     print("Sum :",a+b)

# s1=Student("Sujan Shrestha",101)
# s1.getStudentInfo()
# s1.getCollegeInfo()
# s1.m1(10,20)
# s2=Student("Samir Shrestha",102)
# s2.getStudentInfo()

#self variable inside constructor
# class Employee:
#   def __init__(self):
#     self.name="Sujan Shrestha"
#     self.age=36
#     self.salary=50000
# e=Employee()
# print(e.__dict__)

#instance variable inside method or class
# class Test:
#   def __init__(self):
#     self.a=10
#     self.b=20
#   def m1(self):
#     self.c=30
# t=Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)

#outside class
# class Test: 
#   def __init__(self):
#     self.a=10
#     self.b=20
# t=Test()
# t.c=30 #instance variable created outside class
# print(t.__dict__)

#Accessing instance variable 
# class Test:
#   def __init__(self): 
#     self.a=10
#     self.b=20
#   def display(self):
#     print("Value of a :",self.a) #accessing instance variable inside class
#     print("Value of b :",self.b) #accessing instance variable inside class
# t=Test()
# t.display()
# print(t.a) #accessing instance variable outside class
# print(t.b) #accessing instance variable outside class

#Deleting instance variable
# class Test:
#   def __init__(self):
#     self.a=10
#     self.b=20
#     self.c=30
#     self.d=40
#   def m1(self):
#     del self.c #deleting instance variable inside class
# t=Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# del t.a #deleting instance variable
# print(t.__dict__)

#static variable or class variable
# class Test:
#   a=10 #static variable or class variable
#   b=20 #static variable or class variable
#   def __init__(self):
#     Test.c=30 #static variable or class variable created inside constructor
#   def m1(self):
#     Test.d=40 #static variable or class variable created inside method
#   @classmethod
#   def m2(cls):
#     Test.e=50 #static variable or class variable created inside class method
#     cls.f=60 #static variable or class variable created inside class method
#   @staticmethod
#   def m3():
#     Test.g=70 #static variable or class variable created inside static method
# print(Test.__dict__) #accessing static variable or class variable
# t=Test()
# print(Test.__dict__)#accessing static variable or class variable after creating object
# t.m1()
# print(Test.__dict__)#accessing static variable or class variable after calling method m1()
# Test.m2()
# print(Test.__dict__)#accessing static variable or class variable after calling class method m2()
# Test.m3()
# print(Test.__dict__)#accessing static variable or class variable after calling static method m3()

#Accessing static variable or class variable
# class Test:
#   a=10 #inside class but outside method
#   def __init__(self):
#     print(Test.a) #accessing static variable or class variable inside constructor
#     print(self.a) #accessing static variable or class variable inside constructor using self
#   def m1(self):
#     print(Test.a) #accessing static variable or class variable inside method
#     print(self.a) #accessing static variable or class variable inside method using self
#   @classmethod
#   def m2(cls):
#     print(Test.a) #accessing static variable or class variable inside class method
#     print(cls.a) #accessing static variable or class variable inside class method using cls
#   @staticmethod
#   def m3():
#     print(Test.a) #accessing static variable or class variable inside static method
# t=Test()
# t.m1()
# t.m2()
# t.m3()
# print(Test.a)

#Changing value of static variable or class variable
# class Test:
#   a=10 #static variable or class variable
#   def __init__(self):
#     Test.a=20 #changing value of static variable or class variable inside constructor
#   def m1(self):
#     Test.a=30 #changing value of static variable or class variable inside method
#   @classmethod
#   def m2(cls):
#     Test.a=40 #changing value of static variable or class variable inside class method
#     cls.a=50 #changing value of static variable or class variable inside class method using cls
#   @staticmethod
#   def m3():
#     Test.a=50 #changing value of static variable or class variable inside static method
# print(Test.a) #accessing static variable or class variable before creating object
# t=Test()
# print(Test.a) #accessing static variable or class variable after creating object
# t.m1()
# print(Test.a) #accessing static variable or class variable after calling method m1()
# Test.m2()
# print(Test.a) #accessing static variable or class variable after calling class method m2()
# Test.m3()

# class Test:
#   a=10
#   def m1(self):
#     self.a=20
# t=Test()
# print(Test.a) 
# t.m1()
# print(t.a)
# class Test:
#   a=10
#   def __init__(self):
#     self.b=20
# t1=Test()
# t2=Test()
# print(t1.a,t1.b)#10 20
# print(t2.a,t2.b)#10 20
# t1.a=30 #creating instance variable a for t1
# t2.a=40 #creating instance variable a for t2
# print(t1.a,t1.b) #30 20
# print(t2.a,t2.b) #40 20

# class Test:
#   a=10
#   def __init__(self):
#     self.b=20
# t1=Test()
# t2=Test()
# Test.a=30 #changing value of static variable or class variable
# t1.a=40 #creating instance variable a for t1
# t2.b=50 #creating instance variable b for t2
# print(t1.a,t1.b) #40 20
# print(t2.a,t2.b) #30 50 

# class Test:
#   a=10
#   def __init__(self):
#     self.b=20
#   def m1(self):
#     self.a=30 #creating instance variable a for t1
#     self.b=40 #changing value of instance variable b for t1
# t1=Test()
# t2=Test()
# t1.m1() #creating instance variable a for t1 and changing value of instance variable b for t1
# print(t1.a,t1.b) #30 40
# print(t2.a,t2.b) #10 20

# class Test:
#   a=10
#   def __init__(self):
#     self.b=20
#   @classmethod
#   def m1(cls):
#     cls.a=30 #changing value of static variable or class variable inside method
#     cls.b=40 #changing value of instance variable b for t1
# t1=Test()
# t2=Test()
# t1.m1()
# print(t1.a,t1.b) #30 20
# print(t2.a,t2.b) #30 20
# print(Test.a) #30
# print(Test.b) #40

3#Deleting static variable or class variable
# class Test:
#   a=20  
#   @classmethod
#   def m1(cls):
#     #inside class method we can delete static variable or class variable using del keyword
#     del cls.a #deleting static variable or class variable inside class method 
#     del Test.a #deleting static variable or class variable inside class method using class name
# print(Test.__dict__) #accessing static variable or class variable before deleting
# Test.m1() #deleting static variable or class variable
# del Test.a #deleting static variable or class variable outside class
# print(Test.__dict__) #accessing static variable or class variable after deleting

# class Test:
#   a=10
# t1=Test()
# print(Test.a) #10 # this is because we are accessing static variable or class variable using class name
# print(t1.a) #10 # this is because we are accessing static variable or class variable using object reference variable
#del t1.a # it is not possible to delete static variable or class variable using object reference variable because it will create instance variable a for t1 and delete static variable or class variable a for t1


#local variable
# class Test:
#   def m1(self):
#     a=10 #local variable
#     print("Value of a :",a) #accessing local variable inside method
# t=Test()
# t.m1()

# class Test:
#   @staticmethod
#   def average(list):
#     result= sum(list)/len(list)
#     return result
# list=[10,20,30,40,50]
# t=Test()
# a=t.average(list)#classko through access gareko
# print(a)

# class Test:
#   def m1(self):
#     a=1000
#     print(self.a)
#   def m2(self):
#     b=2000
#     print(self.a)
#     print(b)
# t=Test()
# t.m1
# t.m2

