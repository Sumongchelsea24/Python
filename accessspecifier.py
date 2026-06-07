#Example public
# class Test:
#   def __init__(self):
#     self.x=10
#   def m1(self):
#     print("This is public method.")
#   def m2(self):
#     print(self.x)
#     self.m1()
# t=Test()
# t.m2()
# #public vayara bahira bata call garna mileko
# print(t.x)
# t.m1()

#Example private
#pythonma yo naming covecation matrai ho
# class Test:
#   def __init__(self):
#     self.__x=10
#   def __m1(self):
#     print("This is private method.")
#   def m2(self):
#     print(self.__x)
#     self.__m1()
# t=Test()
# t.m2()
# print(t._Test__x)

#protected

# class Test:
#   def __init__(self):
#     self._x=10
#   def m1(self):
#     print(self._x)
# class subTest(Test):
#   def m2(self):
#     print(self._x)
# s=subTest()
# s.m1()
# s.m2()
# print(s._x)#napaune parne ho tara paenxa 

#Data hiding
# class Account:
#   def __init__(self,min_balance):
#     self.balance=min_balance
#   def getBalance(self):
#     #validation
#     return self.__balance
# a=Account(2000)
# print(a.getBalance())
# #print(a.__balance)