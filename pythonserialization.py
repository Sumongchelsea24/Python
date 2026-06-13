#Pickle

# import pickle

# class Employee:
#   def __init__(self,eno,ename,esal,eaddr):
#     self.eno=eno
#     self.ename=ename
#     self.esal=esal
#     self.eaddr=eaddr
#   def display(self):
#     print(f"Eno:{self.eno} \n Ename:{self.ename} \n Esal:{self.esal} \n Eaddress:{self.eaddr}")
# e=Employee("e104","Rahul",300000,"Kathmandu")
# with open("emp.dat","wb")as f:
#   pickle.dump(e,f)
#   print("Pickling finished")
# with open("emp.dat","rb")as f:
#   obj=pickle.load(f)
#   print("Unpickling finished.")
# obj.display()

#With JSON
# import json
# employee={
#   "name":'Suman',
#   "age":20,
#   "salary":40000,
#   "ismarried":None
# }
# json_string=json.dumps(employee)
# print(json_string)
# with open("emp.json",'w')as f:
#   json.dump(employee,f,indent=4)

#deserialization
# import json
# json_string='''{
#     "name": "Suman",
#     "age": 20,
#     "salary": 40000,
#     "ismarried": null
# }'''
# emp_dict=json.loads(json_string)
# print(emp_dict)
# print("Emp Name",emp_dict["name"])
# print("Emp Age",emp_dict["age"])
# print("Emp Salary",emp_dict["salary"])
# print("Emp Married?",emp_dict["ismarried"])

# import json
# with open("emp.json",'r')as f:
#   emp_dict=json.load(f)
# print(emp_dict)
# print("Emp Name : ",emp_dict["name"])
# print("Emp Age : ",emp_dict["age"])
# print("Emp Salary: ",emp_dict["salary"])
# print("Emp Married? : ",emp_dict["ismarried"])

# import json
# class Employee:
#   def __init__(self,eno,ename,esal,eaddr):
#     self.eno=eno
#     self.ename=ename
#     self.esal=esal
#     self.eaddr=eaddr
#   def display(self):
#     print(f"Eno:{self.eno} \n Ename:{self.ename} \n Esal:{self.esal} \n Eaddress:{self.eaddr}")
# e=Employee(101,"Dipu",200000,"Kathmandu")
# #emp_dict={"eno":e.eno,"ename":e.ename,"esal":e.esal,"eaddr":e.eaddr}
# #mathiko sattama
# emp_dict=e.__dict__
# with open("emp.json","w")as f:
#   json.dump(emp_dict,f,indent=4)

# with open("emp.json","r")as f:
#   edict=json.load(f)
# print(edict)

# import jsonpickle
# class Employee:
#   def __init__(self,eno,ename,esal,eaddr,isMarried):
#     self.eno=eno
#     self.ename=ename
#     self.esal=esal
#     self.eaddr=eaddr
#     self.isMarried= isMarried
#   def display(self):
#     print(f"Eno:{self.eno} \n Ename:{self.ename} \n Esal:{self.esal} \n Eaddress:{self.eaddr}")
# e=Employee(101,"Dipu",200000,"Kathmandu",None)
#serialization to string:
#json_string=jsonpickle.encode(e)
#print(json_string)

#serialization to file:
# with open("emp.json","w")as f:
#   f.write(json_string)

# json_string=jsonpickle.decode(e)
# #deserialization to string:
# emp_string=jsonpickle.decode(e)
# print(emp_string)

# # deserialization to file:
# with open("emp.json","w")as f:
#   f.write(json_string)

# with open("emp.json",'r')as f:
#   json_string=f.readline()
# newEmp=jsonpickle.decode(json_string)
# print(newEmp)
# newEmp.display()

#Ymal
# from pyaml import yaml

# employee={
#   "name":'Suman',
#   "age":20,
#   "salary":40000,
#   "ismarried":None
# }
# yaml_string=yaml.dump(employee)
#print(yaml_string)
# print(type(yaml_string))

# with open("emp.yaml","w")as f:
#   yaml.dump(employee,f)

# with open("emp.json","r")as f:
#   a=yaml.safe_load(f)
# print(a)