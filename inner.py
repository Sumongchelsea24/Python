# class Outer:
#   def __init__(self):
#     print("Outer class")
#   class Inner:
#     def __init__(self):
#       print("Inner classes.")
#     def m(self):
#       print("Inner class method.")

# o=Outer()
# i=o.Inner()
# i.m()

# class Outer:
#   def __init__(self):
#     print("Outer object is created.")
#   class Inner:
#     def __init__(self):
#      print("Inner object is created.")
#     class InnerInner:
#       def __init__(self):
#         print("InnerInner object is created.")
#       def m(self):
#         print("Innner Inner class")

# ii=Outer().Inner().InnerInner()
# ii.m()

# class Human:
#   def __init__(self):
#     self.name="Sujan"
#     self.head=self.Head() #object lai nai hold gareko
#     self.brain=self.Brain()
#   def display(self):
#     print("Hello",self.name)
  
#   class Head:
#     def talk(self):
#       print("Head can talk..")
#   class Brain:
#     def think(self):
#       print("Brain can think...")

# h=Human()
# h.display()
# h.head.talk()
# h.brain.think()

# class Human:
#   def __init__(self,name):
#     self.name=name
#     self.head=self.Head()
#   def info(self):
#     print("Hello my name is : ",self.name)
#   class Head:
#     def __init__(self):
#       self.brain=self.Brain()
#     def talk(self):
#       print("Talk")
#     class Brain:
#       def think(self):
#         print("Think")

# human=Human("Sujan")
# human.info()
# human.head.talk()
# human.head.brain.think()

# class Test:
#   def m(self):
#     def calc(a,b):
#       print("Sum : ", a+b)
#       print("Difference : ", a-b)
#       print("Product : ", a*b)
#     calc(20,30)
#     calc(100,80)
# t=Test()
# t.m()



      
    





