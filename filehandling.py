#properties of file object

# f=open("abc.txt",'r')

# print("The file that is opened : ",f.name)#name
# print("The file mode is : ",f.mode)#mode
# print("Is file closed ? : ",f.closed)
# print("Is file readable ? : ",f.readable())
# print("Is file writeable ? : ",f.writable())
# f.close()
# print("Is file closed ? : ",f.closed)

# f=open("abd.txt",'w')
# f.write("Sujan\n")
# f.write("Sangita \n")
# f.write("Ram \n")
# f.write("Sita \n")
# print("Written in file successfully.")
# f.close()


# f=open("abd.txt",'w')
# #list=["Vaskar\n","Dipesh\n","Pragyan\n","Nikita\n","Geeta\n","Babita\n"]
# # f.writelines(list)
# d={'A':'Vaskar\n', 'B':'Dipesh\n','C':'Nikita\n','D':'Geeta\n'}
# f.writelines(d.values())
# print("I think data is written on file.")
# f.close()

# fname=input("Enter the file name you want.")
# f=open(fname,'w')
# while True:
#   data=input("Enter Data you want to add : ")
#   f.write(data +'\n')
#   option=input("Do you want to add more data ? ")
#   if option.lower() == 'no':
#     break
# f.close()
# print("Data written successfully.")

# f=open('abd.txt','r')
# # data=f.read()
# data=f.readline()
# print(data)
# f.close()

# f=open('abd.txt','r')
# line=f.readline()
# while line!='':
#   print(line,end='')
#   line=f.readline()
# f.close()

# f=open('abd.txt','r')
# lines=f.readlines()
# for line in lines:
#   print(line,end='')
# f.close()

# a=input("Enter the name of file from which you want to read : ")
# b=input("Enter the name of file in which you want to write : ")
# f1=open(a,'r')
# f2=open(a,'w')
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

#good practice
# with open('abd.txt','w') as f1:
#   f1.write("I have written something.")
#   print("Is file Closed ? ",f1.closed)
# print("Is file Closed ? ",f1.closed)

# f=open("abd.txt",'r')
# print(f.tell())
# print(f.read(5))
# print(f.tell())

# import os,sys
# fname=input("Enter the file name : ")
# if os.path.isfile(fname):
#   print(fname,"is in our system")
#   f=open(fname, 'r')
#   data=f.read()
#   print(data)
#   f.close()
# else:
#   print("File does not exist.")
#   sys.exit(0)

import os,sys
fname=input("Enter the file name : ")
if os.path.isfile(fname):
  print(fname,"is in our system")
  lcount=wcount=ccount=0
  f=open(fname, 'r')
  for line in f:
    lcount=lcount+1
    no_of_words=len(line.split())
    wcount= wcount + no_of_words
    no_of_character=len(line)
    ccount=ccount +no_of_character
    
  
else:
  print("File does not exist.")
  sys.exit(0)
print("Number of line : ",lcount)
print("Number of words : ",wcount)
print("Number of Character : ",ccount)