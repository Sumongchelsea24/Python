# class Test:
#   def __init__(self):
#     print("This is constructor")
#   def __del__(self):
#     print("This is destructor")
# t=Test()
# print("End of Application")

# import time
# class Test:
#   def __init__(self):
#     print("This is constructor")
#   def __del__(self):
#     print("This is destructor")
# t=Test()
# print("Constructor is just called")
# t1=t
# t2=t
# print("Test object has 3 ref now")
# del t
# print("t reference is deleted")
# time.sleep(5)
# del t1
# print("t1 reference is deleted")
# time.sleep(5)
# del t2
# print("t2 reference is deleted")
# time.sleep(5)
# print("End of Application")

#In python per object constructor call hunxa and destructor ko pani tei o
# class Test:
#   def __init__(self):
#     print("This is constructor")
#   def __del__(self):
#     print("This is destructor")
# l=[Test(),Test(),Test()]

# import sys
# class Test:
#   pass
# t=Test()
# t1=t
# t2=t
# t3=t
# print(sys.getrefcount(t))#self thapera 5 hunxa