class Employee:
  def __init__(self,eno,ename,esal,eaddr):
    self.eno=eno
    self.ename=ename
    self.esal=esal
    self.eaddr=eaddr
  def display(self):
    print(f"Eno:{self.eno} \n Ename:{self.ename} \n Esal:{self.esal} \n Eaddress:{self.eaddr}")