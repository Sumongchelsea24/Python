# print("This s first line of program.")
# print(10/0)
# print("This is last line of program.")

# print("This s first line of program.")
# try:
#     print(10/0)
# except ZeroDivisionError:
#   print(10/2)
# print("This is last line of program.")

#try with except
# try:
#   x=int(input("Enter the first number: "))
#   y=int(input("Enter the second number: "))
#   print("The result of division is : ",x/y)
# except BaseException as a:
#   print("Type of excepction occured is : ",type(a))
#   print("Type of excepction occured is : ",a.__class__)
#   print("Type of excepction occured is : ",a.__class__.name)

#try with multiple except
# try:
#   x=int(input("Enter the first number: "))
#   y=int(input("Enter the second number: "))
#   print("The result of division is : ",x/y)
# except ZeroDivisionError:
#   print("Sorry ! you cannot divide by 0.")
# except ValueError:
#   print("Sorry ! You must enter integer by number")
# print("This is end of the program")

#Example
# try:
#   x=int(input("Enter the first number: "))
#   y=int(input("Enter the second number: "))
#   print("The result of division is : ",x/y)
# except (ZeroDivisionError,ArithmeticError,ValueError):
#   print("Zero Division Error")

#Default except block
# try:
#   x=int(input("Enter the first number: "))
#   y=int(input("Enter the second number: "))
#   print("The result of division is : ",x/y)
# except ZeroDivisionError:
#   print("Zero Division Error")
# except:
#   print("Even value error is handled.")

#finally for clean up 

# try:
#   x=int(input("Enter the first number: "))
#   y=int(input("Enter the second number: "))
#   print("The result of division is : ",x/y)
# except ZeroDivisionError:
#   print("Zero Division Error")
# finally:
#   print("This is cleanup activities.")