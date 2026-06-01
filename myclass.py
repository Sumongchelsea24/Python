# class A:
#   '''This is demo class .This class does nothing'''
#   #Attributes/variables
#   #Behaviour/method()
# print(A.__doc__)
# help(A)

# #Empty class
# class A:
#   pass

# class Student:
#   def __init__(self):
#     self.name="Sujan Shrestha"
#     self.age=36
#     self.marks=99
#   def talk(self):
#     print("Hello my name is :",self.name)
#     print("My age is : " ,self.age)
#     print ("Marks :",self.marks)

# s=Student()
# s.talk()

# class Student:
#   def __init__(self,name,age,marks):
#     self.name=name
#     self.age=age
#     self.marks=marks
#   def talk(self):
#     print("Hello my name is :",self.name)
#     print("My age is : " ,self.age)
#     print ("Marks :",self.marks)

# s=Student("Sujan Shrestha",36,99)
# s.talk()

class Student:
  def __init__(self,name,age,marks):
    self.name=name
    self.age=age
    self.marks=marks
  def info(self):
    print("Hello my name is :",self.name)
    print("My age is : " ,self.age)
    print ("Marks :",self.marks)

list_of_students=[]

while True:
  name=input("Enter name of student :")
  age=int(input("Enter age of student :"))
  marks=int(input("Enter marks of student :"))
  s=Student(name,age,marks)
  list_of_students.append(s)
  print("Student added successfully !")
  choice=input("Do you want to add more students ? (y/n) :")
  if choice.lower() == 'n':
    break 
for student in list_of_students:
  student.info()
  print("-------------")

