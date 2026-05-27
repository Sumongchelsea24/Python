#List
# a=[10,20,30,40,10,"Hello"]
# a.append(2000)
# a.remove("Hello")
# print(a)
# print(type(a))

# l=eval(input("Enter the list : "))
# print(l)
# print(type(l))

# l=list(range(10,21))
# print(l)
# print(type(l))

# l="learing Python is easy and beautiful".split()
# print(l)

# l=[10,20,30,40,50,60]
# print(l[4])
# print(l[-2])
#concept of slicing
#print(l[1:5])#output:[20,30,40,50]
#print(l[1:5:2])#output:[20,40]
#print(l[6:2:-2])#output:[60,40](yaha left aba 1 xadadai index 2 samman jannu paryo)
#print(l[4:40000])#output:[50,60](slicing le range error didaina)
#print(l[::])#output:[10,20,30,40,50,60]

#list vs Immutability
# l=[10,20,30,40,50,60]
# print(l)
# print(id(l))
# l[0]=90
# print(l)
# print(id(l))
# #naya reference id paudaina same hunxa so mutable hunxa 

#Traversing of element of list by using while loop

# l=[10,20,30,40,50,60,70]
# i=0
# while i<len(l):
#   print(l[i])
#   i+=1

#Traversing of element of list by using for loop
# l=[10,20,30,40,50,60,70]
# for x in l:
#   print(x)

# l=[10,20,30,40,50,60,70]
# print(len(l))#default function of python vayara yasari use garxau
#print(l.len())#list specific vayako vaya yasari use gartheu

# l=[10,20,30,40,50,60,70]
# print(l.count(10))# kina ki you list specific function so yasari use gareko

# l=[10,20,30,40,50,60,70]
# print(l.index(10))# elementko first occurance dine kam garxa

#Manipulating element of list
#Using append()
# l=[30,40,50]
# l.append(70)
# l.append("Hello")
# l.append(10.4)
# print(l)

#Real time programming ma pahilai list thaha hudaina\
#so value aauxa list ma rakhdai janu parxa
#Example: 0 dekhi 100 number samma listma  janu paryo tara divisible by 10
# l=[]
# for i in range(1,101):
#   if i%10==0:
#     l.append(i)
# print(l)

# l=[22,25,82,21]
# l[2]=43#yasto garyo vani chahi 43 le 25 lai replace garxa ra aru value change hudaina
# print(l)

#insert()
# l=[22,25,82,21]
# l.insert(2,43)#pahilo numberle index janauxa ra dosro numberle thapnu parne value janauxa
# print(l)

#extend
# l1=[10,20,101,88,72, 13,88]
# l2=["Manakamana","Shiva",80]
# l3="Hello"
# l1.extend(l2)
# print(l1)
# l2.extend(l3)
# print(l2)
# l1.remove(88)
# print(l1)

#yahi dohariyako element sabai remove garna paryo vani hami loop use garxau

# l=[10,80,12,18,10,79,10,10,45,89,10]
# x=int(input("Enter the number you want to remove : "))
# while True:
#   if x in l:
#     l.remove(x)
#   else:
#     break
# print(l)

#pop()
# l=[10,20,20,40,30,38]
# l.pop()
# print(l)

#Ordering element of list

#reverse yo list specific function ho
# l=[10,20,60,80,100]
# l.reverse()
# print(l)

#reversed yo chali string ma padheko thio bhujhnako lagi matrai ho yo bulit in function ho
# l=[10,20,60,80,100]
# a=reversed(l)
# print(a)
# print(type(a))
# for i in a :
#   print(i,end=' ')

#sort garnu payo vani (sano dekhi thulo karmasa)
# l=[10,20,60,80,100,10,59,45,39]
# l.sort()#ascending order hunxa number haru
# print(l)
#l.sort(reverse=True)#desending order ma
# print(l)

#Aliasing and cloning of list
# x=[10,20,30,40]
# y=x
# print(x)
# print(y)
# print(id(x))
# print(id(y))
# y[2]=500
# print(x)# yo ani problem ho aliasing ko to solve this we use cloning

#By using slice
# x=[10,20,30,40]
# y=x[:]
# print(id(x))
# print(id(y))
# y[2]=400
# print(x)
# print(y)

#By using copy()
# x=[10,20,30,40]
# y=x.copy
# print(id(x))
# print(id(y))
# y[2]=400
# print(x)
# print(y)

#Sabai element list bata hatauna
#clear()
# x=[10,20,30,40]
# x.clear()
# print(x)

#Mathematical operator
# x=[10,20,30,40]
# y=[100,200,300,400]
# print(x+y)# list extend hunxa .thapinxa
# print(x*2)
# print(x==y)

#nested list
# x=[20,30,40,[80,100,120]]
# print(x[0])
# print(x[3])
# print(x[3][2])

# l=[[20,30,40],[80,100,120],[70,60,90]]
# print(l)
# print("Row wise : ")
# for x in l:
#   print(x)
# print("Matrix wise : ")
# for x in l:
#   for y in x:
#     print(y,end=" ")
#   print()

# l=[]
# for i in range(1,11):
#   l.append(i)
# print(l)

#Using list comprehension
# l= [i for i in range(1,11)]
# print(l)

# words=["Bhaskar","Isha","Kabin","Nikita"]
# l=[w[0] for w in words]
# print(l)

# l=[10,20,30,40,40,65,42,51,53,28,36,71]
# m= [x for x in l if x%2==0]
# print(m)

s="The quick brown fox jumps over the lazy dog".split()
p=[[x.upper(),len(x)]for x in s ]
print(p)