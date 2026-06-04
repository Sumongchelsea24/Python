#Concept of composition in python


# class Engine:
#   a=10
#   def __init__(self):
#     self.b=20
#   def m1(self):
#     print("This is engine.")
# class Car:
#   def __init__(self):
#     self.engine=Engine()
#   def m2(self):
#     print("Car object using Engine")
#     print(self.engine.a)
#     print(self.engine.b)
#     self.engine.m1()
# c=Car()
# c.m2()

# class Car:
#   def __init__(self,name,model,color):
#     self.name=name
#     self.model=model
#     self.color=color
#   def getinfo(self):
#     print(f"Car Name: {self.name} \n  Car model: {self.model} \n Car color : {self.color}")

# class Employee:
#   def __init__(self,ename,eno,car):
#     self.ename=ename
#     self.eno=eno
#     self.car=car
#   def empinfo(self):
#     print("Employee Name: ",self.ename)
#     print("Empolyee Number: ",self.eno)
#     print("Empolyee car Information :")
#     self.car.getinfo()
# c=Car("Telsa","V2","RED")
# e=Employee("Ramesh","E323",c)
# e.empinfo()

class X:
  a=10
  def __init__(self):
    self.b=20
  def m1(self):
    print("class X method")
class Y:
  c=30
  def __init__(self):
    self.d=40
  def m2(self):
    print("class Y m2 method")
    
  def m3(self):
    x1=X()
    print(x1.a)
    print(x1.b)
    x1.m1()
    print(Y.c)
    print(self.d)
    self.m2
    print("class Y m3 method")
y=Y()
y.m3()
    
  
    