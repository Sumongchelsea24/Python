from sys import argv

print("The number of command line argument ", len(argv))
print("The command line arguments are",argv)

print("The command line arguments one by one")

for x in argv:
  print(x)