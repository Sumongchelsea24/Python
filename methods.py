#Instance method
# class Student:
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks =marks
#   def display(self):
#     print("Hi",self.name)
#     print("Your marks is",self.marks)
  
#   def grade(self):
#     if self.marks >=60:
#       print("first Grade student...")
#     elif self.marks >=50:
#       print("Second grade Student... ")
#     else:
#       print("You are fail...")
# n=int(input("Please Enter How many students ? : "))
# for i in range(n):
#   name=input("Enter your name : ")
#   marks=int(input("Enter your marks :"))
#   s=Student(name,marks)
#   s.display()
#   s.grade()
#   print()

#2 special Instance method setter() and getter()
# when object is unknown and constructor initialization is unknown

# class Student:
#   def setName(self,name):#namelai initialize garxa
#     self.name=name
#   def getName(self):#namelai access garne kaam garxa
#     return self.name
#   def setMarks(self,marks):
#     self.marks=marks
#   def getMarks(self):
#     return self.marks
# n=int(input(" Enter no of students  : "))
# for i in range(n):
#   s=Student( )
#   name=input("Enter your name : ")
#   s.setName(name)
#   marks=int(input("Enter your marks :"))
#   s.setMarks(marks)
  
#   print("Hi" ,s.getName())
#   print("Your marks is :",s.getMarks())
#   print()

#class method
# class ACEM:
#   department=4
#   @classmethod
#   def work(cls,name):#no way related to object .object banaunu ramro hoina
#     print(f"Acem has {cls.department} department.")
# # a=ACEM() # not recommended
# # a.work("computer")# not recommended
# ACEM.work("Computer")#recommended.correct way

# class Test:
#   count=0
#   def __init__(self):
#     Test.count=Test.count+1
#   @classmethod
#   def noOfObjects(cls):
#     print("The number fo objects created for test class ," ,cls.count)

# t1=Test()
# Test.noOfObjects()

#static method
class AcemMath:
  @staticmethod
  def add(x,y):
    print("The sum is : ",x+y)
  @staticmethod
  def sub(x,y):
    print("The sum is : ",x-y)
  @staticmethod
  def mul(x,y):
    print("The sum is : ",x*y)
AcemMath.add(10,20)
AcemMath.mul(10,20)
AcemMath.sub(10,20)

