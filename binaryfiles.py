# f1=open("image.jpg",'rb')
# f2=open("newimage.jpg",'wb')
# a=f1.read()
# print(type(a)) #bytes
# f2.write(a)
# print("I hope image is copied.")

#write garna
# import csv
# with open("emp.csv","w",newline='')as f:
#   w=csv.writer(f)
#   #print(type(w))
#   w.writerow(['E-number',"E-name","E-Salary","E-Address"])
#   n=int(input("Enter the number of employees : "))
#   for i in range(n):
#     eno=input("Enter Employee number : ")
#     name=input("Enter Employee name : ")
#     salary=input("Enter Employee Salary : ")
#     address=input("Enter Employee Address : ")
#     w.writerow([eno,name,salary,address])
# print("Our csv file is created")

#Read garna
# import csv
# f=open("emp.csv","r",newline='')
# r=csv.reader(f)
# # print(type(r))
# # print(r)
# data=list(r)
# for line in data:
#   for word in line:
#     print(word,"\t",end='')
#   print()

# from zipfile import *
# f=ZipFile("files.zip","w",ZIP_DEFLATED)
# f.write("file1.txt")
# f.write("file2.txt")
# f.write("file3.txt")
# f.write("file4.txt")
# f.close()
# print("My files.zip is created . You can check it")

# from zipfile import *
# f=ZipFile("files.zip","r",ZIP_STORED)
# names=f.namelist()
# #print(names)
# for name in names:
#   print("Unzipped files are", name)
#   print("content of the files are : ")
#   f1=open(name,'r')
#   print(f1.read())
#   print()

#To know current working directory

# import os
# cwd=os.getcwd()
# print("My current working directory is : ",cwd)

#creating directory
# import os
#os.mkdir("mysubdirectory/subdirectory")
#os.makedirs("mysubdirectory/subdirectory/sub/subsub/subsubsub")

#remove directory 
# import os
# os.rmdir("mysubdirectory")
# #os.removedirs("mysubdirectory/subdirectory/sub/subsub/subsubsub")
# print("directiory is deleted")

#rename directory
# import os
# os.name("myfolder","yourfolder")
# print("Rename operation is completed.")

import os
os.listdir()
