# try:
#   print("Outer try block")
#   try:
#     print("Inner try block")
#     print(10/0)
#   except ZeroDivisionError:
#     print("Inner except block")
#   finally:
#     print("Inner finally block")
# except:
#   print("Outer except block.")
# finally:
#   print("Outer finally block")

# try:
#   print("try")
#   print(10/0)
# except:
#   print("Except")
# else:
#   print("Else")
# finally:
#   print("Finally")

#Example of userdefined exception

class TooYoungException(Exception):
  def __init__(self, args):
    self.msg=args

class TooOldException(Exception):
  def __init__(self, args):
    self.msg=args
    
age=int(input("Enter Your Age : "))
if age>60:
  raise TooOldException("Oh! Wait some more years and you will get a better one.")
elif age<18:
  raise TooYoungException("Oh! boy focus on your study !")
else:
  print("You will get your match! Wait sometime !")