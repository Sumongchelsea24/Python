#function in python
#function is a block of code which perform specific task and return result when called.
#function is defined using def keyword followed by function name and parentheses ().
# def function_name():
#   #function body  
#function can take parameters and return values
# def function_name(parameters):
#Example of function
# def calculate(a,b):
#   print("The sum of a and b is : ",a+b)
#   print("The difference of a and b is : ",a-b)
#   print("The product of a and b is : ",a*b)
#   print("The quotient of a and b is : ",a/b)
# calculate(10,5)
# calculate(20,10)
# calculate(30,15)

#types of function in python
#1. built-in function - a function that is already defined in python and can be used directly without defining it.
#Example of built-in function
# print() - used to print the output
# len() - used to find the length of a string, list, tuple, etc.
# type() - used to find the data type of a variable
# input() - used to take input from the user
#2. user-defined function - a function that is defined by the user to perform a specific task.
#Example of user-defined function
# def greet(name):
#   print("Hello, ",name) 
# greet("Balendra")
# greet("Suman")

# def hello(name):
#   print("Hello, World!",name)
# hello("Alice")
# hello("Bob")
# hello("Charlie")

#Write progrma to generate square of a number
# def square(num):
#   return num*num
# number = int(input("Enter a number: "))
# print( f"The square of the {number} is : {square(number)}")

# def add(a,b):
#   sum=a+b
#   return sum
# num1=int(input("Enter first number : "))
# num2=int(input("Enter second number : "))
# add(num1,num2)
# print(f"The sum of {num1} and {num2} is : {add(num1,num2)}")

#Write a program to check whether a number is odd or even

# def check(num):
#   if num%2==0:  
#     return "Even"
#   else:
#     return "Odd"
# number=int(input("Enter a number : "))
# print(f"The number {number} is : {check(number)}")

#Write a program to find the factorial of a number
# def factorial(num):
#   result=1
#   while num>=1:
#     result=result*num
#     num=num-1
#   return result
# number=int(input("Enter a number : "))
# print(f"The factorial of {number} is : {factorial(number)}")

# def sum_sub(a,b):
#   sum=a+b
#   sub=a-b
#   return sum,sub
# num1=int(input("Enter first number : "))
# num2=int(input("Enter second number : "))
# a,b=sum_sub(num1,num2)#yaha tuple unpacking ho rha hai kyuki function se do value return ho rhi hai
# print(f"The sum of {num1} and {num2} is : {a}")
# print(f"The difference of {num1} and {num2} is : {b}")

#Types of function arguments in python
#1. positional arguments - arguments that are passed to a function in the correct order.
# def greet(name,age):
#   print(f"Hello, {name}. You are {age} years old.")
# greet("Alice",25)#positional arguments
#greet(25,"Alice")#positional arguments but order is wrong
#2. keyword arguments - arguments that are passed to a function by specifying the parameter name.
# def greet(name,age):
#   print(f"Hello, {name}. You are {age} years old.")
# greet(name="Alice",age=25)#keyword arguments
#greet(age=25,name="Alice")#keyword arguments but order is not important
#3. default arguments - arguments that are given a default value in the function definition.
# def greet(name,age=30):
#   print(f"Hello, {name}. You are {age} years old.")
# greet("Alice")#default arguments
#greet("Bob",25)#default arguments but age is given by user
#4. variable-length arguments - arguments that can take a variable number of values.
# def greet(*names):
#   for name in names:
#     print(f"Hello, {name}.")
# greet("Alice","Bob","Charlie")#variable-length arguments
#greet("Alice")#variable-length arguments but only one argument is passed

# def sum(*args):
#   total=0
#   for num in args:
#     total=total+num
#   return total
# print(sum(1,2,3))#6
# print(sum(4,5))#9

# def f(a,*args):
#   print("The value of a is : ",a)
#   print("The value of args is : ",args)

# f(1,2,3,4)
# def f(*args, a):
#   print("The value of a is : ",a)
#   print("The value of args is : ",args)

# f(1,2,3,4, a=5)

#variable-length keyword arguments - arguments that can take a variable number of keyword arguments.
#yasle dictionary banaucha rahecha
# def f(**kwargs):
#   print("The value of kwargs is : ",kwargs)
# f(name="Alice",age=25,city="New York")  

def f(*args, **kwargs):
  print("The value of args is : ",args)
  print("The value of kwargs is : ",kwargs)
f(1,2,3, name="Alice", age=25, city="New York")