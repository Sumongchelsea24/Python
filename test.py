
# def add(a,b,c):
#     print("This is add function in test.py file")
#     return a+b+c;

# def mul(a,b):
#     print("This is mul function in test.py file")
#     return a*b;

import time
import importlib
import modules

print(modules.add(20,30,40))
print("Our program is on sleep")
time.sleep(30)
print("Our program is wake up")
importlib.reload(modules)
print(modules.add(20,30,40))