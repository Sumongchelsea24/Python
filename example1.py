#Ternary Operator example
# a=int(input("Enter the First Number: "))
# b=int(input("Enter the Second Number: "))
# min= a if a<b else b
# print(min)

#Yasto ni garna milxa
# a=int(input("Enter the First Number: "))
# b=int(input("Enter the Second Number: "))
# print("Both numbers are equal" if a==b else "First number is less" if a<b else "First number is greater")

#Nesting of ternary operation
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
c=int(input("Enter the Third Number: "))
min= a if a<b and a<c else b if b<c else c
print("The min value is :",min)