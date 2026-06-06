#super() method
# class P:
#   def m1(self):
#     print("This is parent method")
# class C(P):
#   def m1(self):
#     super().m1()#mero classko parent class call garnu
#     print("This is child method")
# c=C()
# c.m1()#child le priority pauxa

# class P:
#   a=10
#   def __init__(self):
#     self.b=20
#     print("Parent constructor is child.")
#   def m1(self):
#     print("Parent class instance method is called.")
#   @classmethod
#   def m2(cls):
#     print("Parent class class method is called")
#   @staticmethod
#   def m3():
#     print("Parent class static method is called")
# class C(P):
#   a=55
#   def __init__(self):
#     self.b=66
#     print("Child constructor is called")
#     super().__init__()#mero parent classlai call garnu object banne bitikai
#     super().m1()
#     super().m2()
#     super().m3()
# c=C()
# c.m1()
#print(c.b)

# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def display(self):
#     print("Name : ",self.name)
#     print("Age : ",self.age)
# class Student(Person):
#   def __init__(self, name, age,roll, marks):
#     super().__init__(name, age)
#     self.roll=roll
#     self.marks=marks
#   def display(self):
#     super().display()#parent class ko display
#     print("Roll Number : ",self.roll)
#     print("Marks : ",self.marks)
    
# s=Student("Shreejan",36,101,99)
# s.display()

# class A:
#   def m1(self):
#     print("A class Method")
# class B(A):
#   def m1(self):
#     print("B class Method")
# class C(B):
#   def m1(self):
#     print("C class Method")
# class D(C):
#   def m1(self):
#     print("D class Method")
# class E(D):
#   def m1(self):
#     #super().m1()
#     #A.m1(self)
#     super(C,self).m1()
#     print("E class Method")
# e=E()
# e.m1()

#Case:1
#From child class we are not allowed to access parent class instancde variable by super()
#Compulsory we shoud use self only but class variable /static variable we can use super()

# class P:
#   a=10
#   def __init__(self):
#     self.b=20
# class C(P):
#   def m1(self):
#     print(super().a)
#     print(self.b)# instance variable vayara self use gare super use garyo vani error aauxa
# c=C() 
# c.m1()

#Case:2
#From child class constructor and instance method we can access parent class instance,static  and class method by using super()
# class P:
#   def __init__(self):
#     print("Parent class constructor")
#   def m1(self):
#     print("Parent class instance method")
#   @classmethod
#   def m2(cls):
#     print("Parent class class method")
#   @staticmethod
#   def m3():
#     print("Parent class instanc method")
# class C(P):
#   def __init__(self):
#     super().__init__()
#     super().m1()
#     super().m2()
#     super().m3()
#   def m1(self):
#     super().__init__()
#     super().m1()
#     super().m2()
#     super().m3()
# c=C()
# c.m1()

#case:3
#from child class class method we cannot access parent class instance method and consturctor by using super()
#But we can access class /static method (indirectly)

# class P:
#   def __init__(self):
#     print("Parent class constructor")
#   def m1(self):
#     print("Parent class instance method")
#   @classmethod
#   def m2(cls):
#     print("Parent class class method")
#   @staticmethod
#   def m3():
#     print("Parent class instanc method")
# class C(P):
#   @classmethod
#   def m1(cls):
#     #super().__init__()#paedaina
#     #super().m1()#paedaina
#     super().m2()#paenxa
#     super().m3()#paenxa
#     #indirectly call garna consturctor 
#     super(C,cls).__init__(cls)
#     #instance class indirectly
#     super(C,cls).m1(cls)
# c=C()
# c.m1()

#case:4
#In child class static methods we are not allowed to use super() generally but we can in a special way
# class P:
#   def __init__(self):
#     print("Parent class constructor")
#   def m1(self):
#     print("Parent class instance method")
#   @classmethod
#   def m2(cls):
#     print("Parent class class method")
#   @staticmethod
#   def m3():
#     print("Parent class instanc method")
# class C(P):
#     @staticmethod
#     def m1():
#       super(C,C).m2()
#       super(C,C).m3()
# c=C()
# c.m1()
