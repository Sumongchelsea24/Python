#for-loop
# s='morning'
# for x in s:
#   print(x)

# s=input("Enter any string : ")
# i=0
# for x in s:
#   print(f"The charater present at {i} index is {x}")
#   i=i+1

#printing Hello for 10 times
# for x in range(10):#0 to 9
#   print("Hello")

#odd number upto 20
# for x in range(21):#0 to 21
#   if(x%2!=0):
#     print(x)

#Odd number upto 20 tara ulto tarikaile
# for x in range(20,0,-1):
#   if(x%2!=0):
#     print(x)

#Example1
# list=eval(input("Enter List:"))
# sum=0
# for x in list:
#   sum=sum+x
# print("The sum is : ",sum)

#while-loop
# x=1
# while x <=10:
#   print(x)
#   x=x+1

# Number divisible by 3 upto 20
# x=1
# while x<=20:
#   if x%3==0:
#     print(x)
#   x=x+1

#Sum of n natural number
# n=int(input("Enter nubmer : "))
# sum=0
# i=0
# while i<=n:
#   sum=sum+1
#   i=i+1
# print(f"The sum of first {n} natural number is",sum)

#satisfy navaya samm value magna
# name=input("Enter name : ")
# while name !="Balendra":
#   name=input("Try another name : ")
# print("Thanks for conformation.")

#nested loop:
# for i in range(3):
#   for j in range(2):
#     print("hello")

#Example
# n=int(input("Enter the number"))
# for i in range(n):
#   print("*",end="")

#Example
# n=int(input('Enter number or rows '))
# for i in range(n):
#   for j in range(n):
#     print("*",end=" ")
#   print(" ")

# n=int(input('Enter number or rows '))
# for i in range(n):
#   print("* "*n)

# for i in range(100):
#   if i==10:
#     print("I am done !")
#     break
#   print(i)

#Example of break
# l=[10,20,30,600,400,2,30,80,90]
# for i in l:
#   if i>=500:
#     print("You cannot buy the items priced more than 500")
#     break
#   print(i)
# print("shopping completed.")

#Example of continue
# for i in range(10):
#   if i==5:
#     continue
#   print(i)

#loops with else block yo pythonma matrai valied xa. break part encounter vayana vani matrai else execute hunxa
# l=[10,20,30,400,2,30,80,90]
# for i in l:
#   if i>=500:
#     print("You cannot buy the items priced more than 500")
#     break
#   print(i)
# else:
#   print("This if else part of for loop")
# print("shopping completed.")

#example of pass
# def hello():
#   pass
# a=2

#example of pass
# name = input("Enter name :  ")
# if name == "john":
#   print("name is correct")
# else:
#   pass

#del example
# a=10
# print(a)
# del a
# print(a)

#None
# x=10
# x=None
# print(x)

#prime number
# prime number is a number which is divisible by 1 and itself only
#eg: 2,3,5,7,11,13,17,19
#in Nepali, prime number lai "pratham sankhya" vanincha jasle 1 ra aafnai matra le divide huncha

# l=int(input("Enter number : "))
# if l>1:
#   for i in range(2,l):
#     if l%i==0:
#       print("Not a prime number")
#       break
#   else:
#     print("It is a prime number")
#strong number
#it is number whose sum of factorial of digits is equal to the number itself
#eg: 145
#1!+4!+5!=145
#4! = 4*3*2*1=24
#in Nepali, strong number lai "balio sankhya" vanincha jasle aafnai digit haruko factorial ko sum le aafnai matra lai barabar huncha
# l=int(input("Enter number : "))
# sum=0
# temp=l
# while temp>0:
#   digit=temp%10
#   fact=1
#   for i in range(1,digit+1):
#     fact=fact*i
#   sum=sum+fact
#   temp=temp//10
# if sum==l:
#   print("It is a strong number")
# else:
#   print("It is not a strong number")


#palindrome
#palindrome is a number or string which is same when read from left to right and right to left
#eg: 121, 12321, madam, malayalam
#in Nepali, palindrome lai "palindrome sankhya" vanincha jasle left to right ra right to left padhna same huncha
# s=input("Enter string or number : ") 
# if s==s[::-1]:
#   print("It is a palindrome")
# else:
#   print("It is not a palindrome") 

#perfect number
#it is a number which is equal to the sum of its proper divisors
#eg: 6 (1+2+3=6), 28 (1+2+4+7+14=28)
#in Nepali, perfect number lai "sampurna sankhya" vanincha jasle aafnai proper divisors ko sum le aafnai matra lai barabar huncha
# n=int(input("Enter number : "))
# sum=0
# for i in range(1,n):  
#   if n%i==0:
#     sum=sum+i
# if sum==n:
#   print("It is a perfect number")
# else:
#   print("It is not a perfect number")
#armstrong number
#it is a number which is equal to the sum of its own digits each raised to the power of the number of digits
#eg: 153 (1^3 + 5^3 + 3^3
#in Nepali, armstrong number lai "armstrong sankhya" vanincha jasle aafnai digit haruko sum le aafnai matra lai barabar huncha
# n=int(input("Enter number : "))
# sum=0
# temp=n
# order=len(str(n))
# while temp>0:
#   digit=temp%10
#   sum=sum+digit**order
#   temp=temp//10
# if sum==n:
#   print("It is an armstrong number")
# else:
#   print("It is not an armstrong number")


#fibonacci series (number or not)
#it is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1
#eg: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#in Nepali, fibonacci series lai "fibonacci shrankhala" vanincha jasle aafnai paila duita number ko sum le aafnai matra lai barabar huncha
# n=int(input("Enter number : "))
# a=0
# b=1   
# if n==a or n==b:
#   print("It is a fibonacci number")
# else:
#   while b<n:
#     c=a+b
#     a=b 
#     b=c 
#   if b==n:
#     print("It is a fibonacci number") 
#   else:
#     print("It is not a fibonacci number")


#Harshad (niven) number (eg: 18 1+8=9 9 le 18 lai divide garxa vane harshad number ho hoina vane hoina)
# l=int(input("Enter number : "))
# sum=0
# temp=l
# while temp>0:
#   digit=temp%10
#   sum=sum+digit
#   temp=temp//10
# if l%sum==0:
#   print("It is a harshad number")
# else:
#   print("It is not a harshad number")

#Twin number(consequtive prime number ho hi hoina 11 , 13 differe 2 xa yo twin number ho)
# n=int(input("Enter number : "))
# def is_prime(num):
#   if num<=1:
#     return False  
#   for i in range(2,num):
#     if num%i==0:
#       return False  
#   return True
# if is_prime(n) and is_prime(n+2):
#   print(f"{n} and {n+2} are twin prime numbers")
# else:
#   print(f"{n} and {n+2} are not twin prime numbers")
  

