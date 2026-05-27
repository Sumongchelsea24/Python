#t=() #empty tuple
#t=(10) #not a tuple, it is an integer
#t=(10,) #single element tuple
#t=(10,20,30) #multiple element tuple
#t=10,20,30 #tuple packing
#t=10, #single element tuple without parentheses
#L=[10,20,30] #list to tuple conversion
#t=tuple(L) #list to tuple conversion

# t=(10,20,30,40,50)
# print(t[0])
# print(type(t))
# print("Tuple ",t)

#Accessing tuple elements
#Indexing and slicing
#Indexing and slicing is possible in tuples just like lists. The only difference is that tuples are immutable, which means you cannot change the elements of a tuple after it has been created.
#Indexing and slicing a tuple returns a new tuple. The original tuple remains unchanged.
#Indexing and slicing is possible in tuples due to inseration order. The elements of a tuple are stored in the order they were inserted. This means that you can access the elements of a tuple using their index.
# t=(10,20,30,40,50)
# print(t[0])
# print(t[-4])
# print(t[1:4])
# print(t[2:6:2])

#Mathematical operations on tuples
#Mathematical operations on tuples are not possible because tuples are immutable. However, you can perform mathematical operations on the elements of a tuple if they are of a compatible type (e.g., numbers).
 

# #Example of mathematical operations on tuples
# t1=(10,20,30)
# t2=(40,50,60)
# print(t1+t2) #tuple concatenation
# print(t1*2) #tuple repetition
# print(t1==t2) #tuple comparison
# print(t1!=t2) #tuple comparison
# print(t1>t2) #tuple comparison
# print(t1< t2) #tuple comparison
# print(t1>=t2) #tuple comparison
# print(t1<=t2) #tuple comparison
# print(10 in t1) #membership test
# print(100 in t1) #membership test

#Important tuple functions
#len() - returns the number of elements in a tuple
#count() - returns the number of occurrences of a specified element in a tuple
#index() - returns the index of the first occurrence of a specified element in a tuple
#max() - returns the maximum element in a tuple 
#min() - returns the minimum element in a tuple
#sum() - returns the sum of all elements in a tuple (only for numeric tuples)
#sorted() - returns a sorted list of the elements in a tuple
#reversed() - returns a reversed iterator of the elements in a tuple
#Example of important tuple functions
# t=(10,20,30,40,50)
# print(len(t)) #returns the number of elements in a tuple
# print(t.count(20)) #returns the number of occurrences of a specified element in a tuple
# print(t.index(30)) #returns the index of the first occurrence of a specified element in
# print(max(t)) #returns the maximum element in a tuple
# print(min(t)) #returns the minimum element in a tuple 
# print(sum(t)) #returns the sum of all elements in a tuple (only for numeric tuples)
# print(sorted(t)) #returns a sorted list of the elements in a 
# print(reversed(t)) #returns a reversed iterator of the elements in a tuple #tuple nai didaina yaslai list ma convert garna parcha
# print(list(reversed(t))) #returns a reversed list of the elements in a tuple

#packing and unpacking of tuples
#Packing of tuples is the process of creating a tuple by assigning multiple values to a single variable
#Unpacking of tuples is the process of assigning the elements of a tuple to multiple variables
#Example of packing and unpacking of tuples
#Packing of tuples
# t=10,20,30 #packing of tuples
# print(t) #output: (10, 20, 30)
# #Unpacking of tuples
# a,b,c=t #unpacking of tuples
# print(a) #output: 10
# print(b) #output: 20
# print(c) #output: 30


# a=40
# b=50
# c=60
# t=a,b,c #packing of tuples
# print(t) #output: (40, 50, 60)
# print(type(t)) #output: <class 'tuple'>

#tuple comprehension
#Tuple comprehension is not possible in Python because tuples are immutable. However, you can create a tuple using a generator expression, which is similar to a list comprehension but returns a generator object instead of a list. You can then convert the generator object to a tuple using the tuple() function.
#Example of tuple comprehension using generator expression
# t=tuple(x for x in range(10)) #tuple comprehension using generator expression
# print(t) #output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#print(type(t)) #output: <class 'tuple'>

#Difference between tuples and lists
#Tuples and lists are both used to store collections of items. However, there are some key differences between the two:
#1. Mutability: Tuples are immutable, which means that once a tuple is created, its elements cannot be changed. Lists, on the other hand, are mutable, which means that you can change the elements of a list after it has been created.
#2. Syntax: Tuples are defined using parentheses (), while lists are defined using square brackets [].
#3. Performance: Tuples are generally faster than lists because they are immutable and have a smaller memory footprint. Lists, on the other hand, are more flexible and can be modified, which can lead to slower performance in certain cases.
#4. Use cases: Tuples are often used to represent fixed collections of items, such as coordinates or database records. Lists are more commonly used for collections of items that may need to be modified, such as a list of tasks or a list of user inputs.
  