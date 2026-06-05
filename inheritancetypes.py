#single Inheritance
# class P:
#   def m1(self):
#     print("Parent class")
# class C(P):
#   def m2(self):
#     print("Child class")
# c=C()
# c.m1()
# c.m2()

#MultiLevel Inheritance
# class P:
#   def m1(self):
#     print("Parent class")
# class C(P):
#   def m2(self):
#     print("Child class")
# class CC(C):
#   def m3(self):
#     print("Child Child class")
# c=CC()
# c.m1()
# c.m2()
# c.m1()

#Hierarchicla Inheritance
# class P:
#   def m1(self):
#     print("Parent class")
# class C1(P):
#   def m2(self):
#     print("Child class first")
# class C2(P):
#   def m3(self):
#     print("Child class second")
# c=C1()
# c.m1()
# c.m2()

# cc=C2()
# cc.m1()
# cc.m3()

#Multiple Inheritance
# class P1:
#   def m1(self):
#     print("Parent one method")
# class P2:
#   def m2(self):
#     print("Parent two method")
# class C(P1,P2):
#   def m1(self):
#     print("This is child class method")
# c=C()
# c.m1()
# c.m2()
# c.m3()

#Hybrid Inheritance
# class A:
#   def m1(self):
#     print("A class method")
# class B(A):
#   def m1(self):
#     print("B class method")
# class C(A):
#   def m1(self):
#     print("C class method")
# class D(B,C):
#   def m1(self):
#     print("D class method")
# d=D()
# d.m1()

# class A:
#   def m1(self):
#     print("A class method")
# class B:
#   def m1(self):
#     print("B class method")
# class C:
#   def m1(self):
#     print("C class method")
# class X(A,B):
#   def m3(self):
#     print("X class method")
# class Y(B,C):
#   def m1(self):
#     print(" Y class method")
# class P(X,Y,C):
#   def m2(self):
#     print("P class method")
# p=P()
# p.m1()
#print(p.mro())

# class A:pass
# class B(A):pass
# class C(A):pass
# class D(B,C):pass
# print(A.mro())
# print(B.mro())
# print(C.mro())
# print(D.mro())
