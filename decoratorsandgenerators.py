#revision of function
# def f():
#   print("Hello")
# print(f)
# print(id(f))
# f()

# def wish(name):
#   print("Hello",name)
# #wish("Hello wish you were here")
# greeting=wish
# # print(id(greeting))
# # print(id(wish))
# greeting("Hariya")
# greeting("Mukhiya")

# def outer():
#   print("Outer function")
#   def inner():
#     print("Inner function")
# # inner()
#   return inner
# a=outer()
# a()

# def f1(func):
#   func()
# def f2():
#   print("This is 2nd function.")
# f1(f2) 

#filfer(f,seq)
#map(f,seq)
#reduce(f,seq)

# def decor(func):
#   def inner():
#     print("Send person to decorator")
#     print("Decorated Person")
#   return inner
# @decor
# def display():
#   print("Showing person as it is. ")

# display()

# def decor(func):
#   def inner(name):
#     if name=='isha':
#       print("Hello Isha,Good morning")
#     else:
#       func(name)
#   return inner
# @decor
# def wish(name):
#   print("Hello",name)
# wish("Sunita")

#without decor function
# def decor(func):
#   def inner(name):
#     if name=='isha':
#       print("Hello Isha,Good morning")
#     else:
#       func(name)
#   return inner

# def wish(name):
#   print("Hello",name)
# decorfunction=decor(wish)
# decorfunction("isha")

# def smart_div(func):
#   def inner(a,b):
#     print("We are dividing",a ,"with",b)
#     if b==0:
#       print("OOps..cannot divide ")
#       return
#     else:
#       return func(a,b)
#   return inner

# @smart_div
# def division(a,b):
#   return a/b
# print(division(20,10))
# print(division(20,0))

#decorator chaining
# def decor1(func):
#   def inner():
#     x=func()
#     return x*x
#   return inner


# def decor(func):
#   def inner():
#     x=func()
#     return 2*x
#   return inner
# @decor1
# @decor
# def num():
#   return 10

# print(num())


#g=(x*x for x in range(1,10))
#print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# while True:
#   print(next(g))

# def mygen():
#   yield "A"
#   yield "B"
#   yield "C"
# g=mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# import time
# def countdown(num):
#   print("Start Countdown")
#   while(num>0):
#     yield num
#     num=num-1
# values=countdown(10)
# for x in values:
#   print(x)
#   time.sleep(1)

# import random
# import time
# names=["Hariya","Daniya","Mukhiya","Sukhiya"]
# subjects=["Python","Java" ,"C++","C"]

# def people_list(num_people):
#   result=[]
#   for i in range(num_people):
#     person={
#       'id':i,
#       'name':random.choice(names),
#       'subject':random.choice(subjects)
#     }
#   result.append(person)
#   return result
# def people_generator(num_people):
#   for i in range(num_people):
#     person={
#       'id':i,
#       'name':random.choice(names),
#       'subject':random.choice(subjects)
#     }
#   yield person
# t1=time.time()
# people=people_generator(1000000)
# t2=time.time()
# print("Total time taken to make generator: ",t2-t1)
# t1=time.time()
# people=people_list(1000000)
# t2=time.time()
# print("Total time taken to make list: ",t2-t1)