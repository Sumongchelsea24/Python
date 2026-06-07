from abc import abstractmethod,ABC

# class Test:
#   @abstractmethod
#   def m1():
#     pass

#abstract class
# class Vehicle(ABC):
#   @abstractmethod
#   def noofwheels(self):
#     pass
# class Bus(Vehicle):
#   def noofwheels(self):
#     return 6
# class Bike(Vehicle):
#   def noofwheels(self):
#     return 2
# b=Bus()
# print(b.noofwheels())
# b1=Bike()
# print(b1.noofwheels())

#Valid
# class Test:
#   pass
# t=Test()

#Valid
# class Test(ABC):
#   pass
# t=Test()

#Not valid Object banunau mildaina abstract classko
# class Test(ABC):
#   @abstractmethod
#   def m1(self):
#     pass
# t=Test()

#ABC inhert gareko xaina teslaile  object baunau pauxa
# class Test:
#   @abstractmethod
#   def m1(self):
#     pass
# t=Test()

# class Test(ABC):
#   def m1(self):
#     print("This is not abstract method")
#   @abstractmethod
#   def m1(self):
#     pass
# class SubTest(Test):
#   #m2 compulsory chahinxa abstract classko vayara
#   def m2(self):
#     print("This is m2 method")
# s=SubTest()
# s.m1()
# s.m2()

#Interface

class A(ABC):
  @abstractmethod
  def m1(self):pass
  @abstractmethod
  def m2(self):pass
  @abstractmethod
  def m3(self):pass
  
class DipeshImplementation(A):
  def m1(self):
    print("m1")
  def m2(self):
    print("m2")
  def m3(self):
    print("m3")
    
class BikesImplementation(A):
  def m1(self):
    print("m1")
  def m2(self):
    print("m2")
  def m3(self):
    print("m3")
    
d=DipeshImplementation()
d.m1()
d.m2()
d.m3()
d=BikesImplementation()
d.m1()
d.m2()
d.m3()
