# a=input("Enter the two number : ")
# print(a)
# b=a.split(); #["10","20","30"]
# print(b)
# c=[int(x) for x in b ] # List comperhensive
# print(c)

# x,y=c # unpacking of list
# print("The sum is",x+y)
# print(type(c))

# print(type(a))
# print(type(b))

a,b=[int(x) for x in input("Enter the two number : ").split()]
print("The sum is", a+b)