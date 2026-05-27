#if statement example
# name=input("Enter the name : ")
# if name=="Ram":
#   print("This name was expected")
# print("This might be the end of program")

#if-else example
# name=input("Enter the name : ")
# if name=="Ram":
#   print("This name was expected")
# else:
#   print("This optional name is also okay.")
# print("This might be the end of program")


#if-elif-else
# name=input("Enter the name : ")
# if name=="ram":
#   print("Hello, Ram")
# elif name=="shyam":
#   print("Hello Shyam")
# elif name=="hari":
#   print("Hello Hari")
# elif name=="uttam":
#   print("Hello Uttam")
# else:
#   print("Hello Guest")
# print("This might be the end of program")

#if-elif
# name=input("Enter the name : ")
# if name=="ram":
#   print("Hello, Ram")
# elif name=="shyam":
#   print("Hello Shyam")
# elif name=="hari":
#   print("Hello Hari")
# elif name=="uttam":
#   print("Hello Uttam")

# print("This might be the end of program")

#Greatest number when two number is Given
# n1=int(input("Enter the first number : "))
# n2=int(input('Enter the second number : '))
# if n1>n2:
#   print(f"{n1} is bigger")
# else:
#   print(f"{n2} is bigger")

#Greatest number when three number are given
# n1=int(input("Enter the first number : "))
# n2=int(input('Enter the second number : '))
# n3=int(input('Enter the third number : '))
# if n1>n2 and n1>n3:
#   print(f"{n1} is bigger")
# elif n2>n3:
#   print(f"{n2} is bigger")
# else:
#    print(f"{n3} is bigger")

#Write a program to check whether given number is in between 1 and hundred

# n=int(input("Enter any number : "))
# if n>=1 and n<=100:
#   print("Yes, the number lies in between 1 and 100")
# else:
#   print("Number is out of range.")

#switch statement
# sub = input("Enter your fav sub in Engineering : ")
# match sub:
#   case 'DSA':
#     print("Data Structure and Algorithms")
#   case 'OOP':
#     print("Object Oriented Programming")
#   case 'DM':
#     print("Data Mining")
#   case _:
#     print("Oh No ! You missed exciting subjects.")

#Example
# n=int(input("Enter any number : "))

# if n==0:
#   print("zero")
# elif n==1:
#   print("one")
# elif n==2:
#   print("two")
# elif n==3:
#   print("three")
# elif n==4:
#   print("four")
# elif n==5:
#   print("five")
# elif n==6:
#   print("six")
# elif n==7:
#   print("seven")
# elif n==8:
#   print("eight")
# elif n==9:
#   print("nine")
# else:
#   print("This is not desired number : ")

#Example 1
# list=['zero','one','two','three','four','five','six','seven','eight','nine']
# n=int(input("Enter any number 0 to 99 : "))
# if n<10:
#   print(list[n])
# else:
#   print("This is not desired number : ")


#Example 2

words_upto_19 =['','one','two','three','four','five','six','seven','eight','nine'
                ,'ten','elven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eightteen','nineteen']
words_for_tens=['','' ,'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
n=int(input("Enter any number 0 to 99 : "))
if n==10:
  output = "Zero"
elif n<=19:
  output = words_upto_19[n]
elif n<=99:
  output = words_for_tens[n//10] + " "+ words_upto_19[n%10]
else:
  output = "Please enter numbers between 0 and 99 only :"
print(output)









 
 

