# n=int(input("Enter a number of rows : "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

# n=int(input("Enter a number of rows : "))
# k=1
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         print("*", end=" ")
#         k=k+2
#     print()

n=int(input("Enter a number of rows : "))
for i in range(1, n+1):
    for j in range(i, i-1):
        print("*", end=" ")
    print()

