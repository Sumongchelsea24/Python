#Inheritance
# class P:
#   def m(self):
#     print("This is m method of class P")
# class C(P):
#   def m1(self):
#     print("This is m method of class C")
    
# c=C()
# c.m()
# c.m1()

# class P:
#   a=10
#   def __init__(self):
#     self.b=20
#   def m1(self):
#     print("This is instance method.")
#   @classmethod
#   def m2(cls):
#     print("This is class method")
#   @staticmethod
#   def m3():
#     print("This is static method.")

# class C(P):
#   pass
# c=C()
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()

# class Person:
#   def ___init__(self,name,age):
#     self.name=name
#     self.age=age
#   def eat(self):
#     print("Person can eat momos.")
    
# class Employee(Person):
#   def ___init__(self, name, age,eno,esal):
#     super().__init__(name,age)
#     self.eno=eno
#     self.esal=esal
#   def work(self):
#     print("Employee can work")
#   def empinfo(self):
#     print("Employee Name: ",self.name)
#     print("Employee Age : ",self.age)
#     print("Employee Number : ",self.eno)
#     print("Employee Salary : ", self.esal)
# e=Employee("Ram",47,"e232",50000)
# e.eat()
# e.work()
# e.empinfo()

class Car:
  def __init__(self,name,model,color):
    self.name=name
    self.model=model
    self.color=color
  def getinfo(self):
    print(f"Car name: {self.name} \n Car model : {self.model} \n Car color : {self.color}")

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def eatanddrink(self):
    print("Eat momos and drink coca-cola.")
class Employee(Person):
  def __init__(self, name, age,eno,esal,car):
    super().__init__(name, age)
    self.eno=eno
    self.esal=esal
    self.car=car
    
  def work(self):
    print("Employee can work")
  def empinfo(self):
    print("Employee Name: ",self.name)
    print("Employee Age : ",self.age)
    print("Employee Number : ",self.eno)
    print("Employee Salary : ", self.esal)
    print("Car Info of Employee")
    self.car.getinfo()
c=Car("Tesla","V2","Black")
e=Employee("Dipesh",30,"E212",40000,c)
e.eatanddrink()
e.work()
e.empinfo()