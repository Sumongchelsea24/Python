#Types of variables in functional Programming # OOPma chuttai hunxa yo
#1. Global variable - a variable that is defined outside of any function and can be accessed from anywhere in the program.
#Example of global variable 
# global_var = "I am a global variable"
# def print_global():
#   print(global_var)
# print_global()  

#Example #Jata bata pani access garna sakinxa global variable lai
# a=10
# print(a)
# def f1():
#   print(a)
# def f2():
#   print(a)
# f1()
# f2()
# print(a)


#2. Local variable - a variable that is defined inside a function and can only be accessed within that function.
#Example of local variable
# def print_local():
#   local_var = "I am a local variable"
#   print(local_var)
# print_local()

#Example #Local variable lai function vitra matra access garna sakinxa
# def f1():
#   a=10
#   print(a)  
# def f2():
#   a=20
#   print(a)

#a lai global variable banauna sakinchha ani matrai bahira bata access garna sakinxa
# def f1():
#     global a
#     a=10  
#     print(a)
# f1()
# print(a) 

#Example #Local variableko priroti global vanxa aghi hunxa so output 30 aauxa
# b=20
# def f2():
#     b=30
#     print(b)
# f2()

#Example
# a=10 #Global variable
# def f():
#   a=20 #Local variable
#   print(a) #20  
#   print(globals()['a']) #10
#   print(globals().get)
#   print(locals()['a']) #20
# f()

#Recursive function - a function that calls itself in order to solve a problem.
#Example of recursive function
# def factorial(num):
#   if num==0 or num==1:
#     return 1
#   else:
#     return num * factorial(num-1)
#   return result
# print( "factorial is : ", factorial(int(input("Enter a number : "))))

# def square(num):
#   return num*num
# number = int(input("Enter a number: "))
# print( f"The square of the {number} is : {square(number)}")

#Anonymous function - a function that is defined without a name and is usually used for short-term tasks.
#Example of anonymous function
# square = lambda x: x*x
# print(square(5))

#Example of anonymous function with two arguments
# s= lambda a,b: a+b
# print(s(10,20))

#Example of anonymous function with two arguments and a condition
# s= lambda a,b: a if a>b else b
# print(s(10,20))

#Example of anonymous function with three arguments and a condition
# s= lambda a,b,c: a if a>b and a>c else b if b>c else c
# print("The largest number is: ", s(10,20,30))

#function as the argument - a function that is passed as an argument to another function.
#filter()
#map()
#reduce()
#yasto function haru hami lambda function ko argument ma pass garna sakchhau
#Example of function as the argument
# def square(num):
#   return num*num
# def cube(num):
#   return num*num*num
# def apply_function(func, num):
#   return func(num)
# print(apply_function(square, 5))
# print(apply_function(cube, 5))

#filter() - a function that is used to filter the elements of a sequence based on a condition.
#syntax: filter(function, sequence)
#Example of filter()
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

#Example
# students = ["Alice", "Bob", "Avash", "Charlie", "David","Ayush", "Eve","Alina"]
# starsWithA = list(filter(lambda name: name.startswith('A'), students))
# print(starsWithA)

#Example of above without use of filter() #Standard way to find even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def is_even(num):
#   if num%2==0:
#     return True
#   else:
#     return False
# even_numbers = []
# for num in numbers:  
#   if is_even(num)==True:
#     even_numbers.append(num)
# print(even_numbers)


#map() - a function that is used to apply a function to all the elements of a sequence.
#syntax: map(function, sequence)
#Example of map() without using lambda function
# def square(num):
#   return num*num
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(square, numbers))
# print(squares)

#Example of map()
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x*x, numbers))
# print(squares)

#Example of map() with two sequences
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [10, 20, 30, 40, 50]
# sums = list(map(lambda x, y: x + y, numbers1, numbers2))
# print(sums)




#reduce() - a function that is used to apply a function to all the elements of a sequence and reduce it to a single value.
#syntax: reduce(function, sequence)
#reduce() function is not a built-in function in python, it is a part of functools module so we need to import it before using it.
#Example of reduce() without using lambda function
# from functools import reduce
# def multiply(x, y):
#   return x * y
# numbers = [1, 2, 3, 4, 5]
# product = reduce(multiply, numbers)
#Example of reduce()
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)

#Function Aliasing - a technique in which a function is assigned to a variable, allowing the function to be called using the variable name.
#Example of function aliasing
# def greet(name):
#   print("Hello, ",name)
# say_hello = greet
# say_hello("Alice")

#Nested function - a function that is defined inside another function.
#Example of nested function
# def outer_function():
#   print("This is the outer function")
#   def inner_function():
#     print("This is the inner function")
#   inner_function()
# outer_function()






