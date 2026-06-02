#Banking System
import sys
class Customer:
  '''This is Bank System'''
  bankname="Chelsea"
  def __init__(self,name,balance=0.0):
    self.name=name
    self.balance=balance
  def deposit(self,amt):
    self.balance=self.balance +amt
    print("New Balance after deposit : " ,self.balance)
  def withdraw(self,amt):
    if amt >self.balance:
      print("Insfficient Balance.Please Deposit first")
      sys.exit()#yasle program crash navae safe land garne kaam garxa
    else:
      self.balance=self.balace-amt
      print("Balance after withdraw : ",self.balance)
print()
print("#"*50)
print("Welcome to Chelsea Bank")
print("#"*50)
name=input("Enter your name : ")
c=Customer(name)
while True:
  print("d-Deposit \n w-Withdraw \n e-exit ")
  option=input("Enter your option : ")
  if option=='d' or option=="D":
    amt=float(input("Enter the amount you want to deposit. "))
    c.deposit(amt)
  elif option=='w' or option=="W":
    amt=float(input("Enter the amount you want to withdraw. "))
    c.withdraw(amt)
  elif option=='e' or option=="E":
     print("Thank you for using our service.")
     sys.exit()
  else:
    print("Invalid optin. Please choose valid option. ")
   
  
