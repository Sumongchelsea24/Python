from emp import *
import pickle
f=open("emp.dat","wb")
while True:
  eno=int(input("Enter your employee number : "))
  ename=input("Enter employee Name : ")
  esal=int(input("Enter your employee salary : "))
  eaddr=input("Enter your employee Address : ")
  e=Employee(eno,ename,esal,eaddr)
  pickle.dump(e,f)
  option=input("Do you want to serailize more obj [Yes/No] ?")
  if option.lower()=='no':
    break
  
print("Serialization Completed.")
  