#python dictionary
#A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are mutable, meaning that you can change their contents after they have been created.
#Dictionaries are defined using curly braces {} and key-value pairs are separated by commas. The key and value in a key-value pair are separated by a colon :.
#Example of a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# print(d)
# print(type(d)) #output: <class 'dict'>

#Properties of dictionaries
# Duplicate values are allowed but duplicate keys are not allowed in dictionaries. If you try to create a dictionary with duplicate keys, the last key-value pair will overwrite the previous ones.
# d={'name':'John','age':30,'city':'New York','name':'Jane  Smith'} #dictionary with duplicate keys
# print(d) #output: {'name': 'Jane  Smith', 'age': 30, 'city': 'New York'}  

#Heterogeneous objects are allowed for both keys and values in dictionaries. This means that you can have keys and values of different data types in a dictionary.
# d={'name':'John','age':30,'is_student':True,'hobbies':['reading','traveling'],'address':{'street':'123 Main St','city':'New York'}} #dictionary with heterogeneous objects

#Dictionaries is mutable, which means that you can change their contents after they have been created. You can add, remove, or modify key-value pairs in a dictionary.
# d={'name':'John','age':30,'city':'New York'} #dictionary  
# d['age']=31 #modifying a value in a dictionary
# print(d) #output: {'name': 'John', 'age': 31, 'city': 'New York'}

#Dictionary is dynamic and growable in nature, which means that you can add or remove key-value pairs from a dictionary as needed. You can also change the values of existing keys in a dictionary.
# d={'name':'John','age':30,'city':'New York'} #dictionary
# d['country']='USA' #adding a new key-value pair to a dictionary
# print(d) #output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

#Insertion order is preserved in dictionaries, which means that the order of key-value pairs in a dictionary is the same as the order in which they were added. This is a feature of Python 3.7 and later versions.
#Indexing and slicing is not possible in dictionaries because dictionaries are unordered and unindexed. You cannot access the elements of a dictionary using their index because dictionaries are not ordered collections. Instead, you can access the values in a dictionary using their keys.
# d={'name':'John','age':30,'city':'New York'} #dictionary
# d['country']='USA' #adding a new key-value pair to a dictionary
# print(d) #output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

#Accessing elements in a dictionary
#You can access the values in a dictionary using their keys. You can use square brackets [] or the get() method to access the values in a dictionary.
#Example of accessing elements in a dictionary  
# d={'name':'John','age':30,'city':'New York'} #dictionary
# print(d['name']) #accessing a value using square brackets []
# print(d.get('age')) #accessing a value using the get() method 

# l=[(100,'John'),(200,'Jane'),(300,'Smith')] #list of tuples
# d=dict(l) #converting a list of tuples to a dictionary
# print(d) #output: {100: 'John', 200: 'Jane', 300: 'Smith'}
# print(type(d)) #output: <class 'dict'>

# d=eval(input("Enter a dictionary: ")) #taking input from the user and converting it to a dictionary
# print(d) #output: {'name': 'John', 'age': 30, 'city': 'New York'}
# print(type(d)) #output: <class 'dict'>

# n=int(input("Enter the number of Students: ")) #taking input from the user for the number of students
# students={} #creating an empty dictionary to store student information
# for i in range(n):
#     name=input("Enter the name of the student: ") #taking input from the user for the name of the student
#     age=int(input("Enter the age of the student: ")) #taking input from the user for the age of the student
#     students[name]=age #adding the name and age of the student to the dictionary
# print(students) #output: {'John': 30, 'Jane': 25, 'Smith': 35}  

# rec={
# }
# n=int(input("Enter the number of students: ")) #taking input from the user for the number of students
# i=1
# while i<=n:
#     name=input("Enter the name of the student: ") #taking input from the user for the name of the student
#     marks=int(input("Enter the marks of the student: ")) #taking input from the user for the marks of the student
#     rec[name]=marks #adding the name and marks of the student to the dictionary
#     i+=1
# print(rec) #output: {'John': 30, 'Jane': 25, 'Smith': 35}  
# for k,v in rec.items():
#     print(f"The marks for {k} is {v}") 

#updating a dictionary
#You can update a dictionary by adding new key-value pairs or modifying the values of existing keys. You can use the update() method to update a dictionary with another dictionary or with key-value pairs.
#Example of updating a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# d.update({'country':'USA'}) #updating a dictionary with another dictionary  
# print(d) #output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
# d.update(name='Jane',age=25) #updating a dictionary with key-value
# print(d) #output: {'name': 'Jane', 'age': 25, 'city': 'New York', 'country': 'USA'}

#Deleting elements from a dictionary
#You can delete elements from a dictionary using the del statement or the pop() method. The del statement removes a key-value pair from a dictionary, while the pop() method removes a key-value pair and returns the value of the removed key.
#Example of deleting elements from a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# del d['age'] #deleting a key-value pair using the del statement 
# print(d) #output: {'name': 'John', 'city': 'New York'}
# age=d.pop('age') #deleting a key-value pair using the pop() method  
# print(d) #output: {'name': 'John', 'city': 'New York'}
# print(age) #output: 30  

#clear() - removes all key-value pairs from a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary  
# d.clear() #removing all key-value pairs from a dictionary
# print(d) #output: {}

#Mathematical operations on dictionaries
#You cannot perform mathematical operations on dictionaries because dictionaries are not ordered collections and do not support arithmetic  
#Membership operations on dictionaries
#in - returns True if a key is present in a dictionary, otherwise returns False 
# d={'name':'John','age':30,'city':'New York'} #dictionary
# print('name' in d) #returns True if a key is present in a dictionary  
# print('country' in d) #returns True if a key is present in a dictionary, otherwise returns False

#not in - returns True if a key is not present in a dictionary, otherwise returns False
# d={'name':'John','age':30,'city':'New York'} #dictionary  
# print('name' not in d) #returns True if a key is not present in a dictionary, otherwise returns False
# print('country' not in d) #returns True if a key is not present in a dictionary, otherwise returns False

#functions that are not valid for dictionaries
#+ - * / % ** // = == != > < >= <= [] () {} @ \
#Functions that are not valid for dictionaries because dictionaries are unordered and unindexed

#len() - returns the number of key-value pairs in a dictionary
#Example of len() function on a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# print(len(d)) #output: 3

#get() - returns the value of a specified key in a dictionary. If the key is not found, it returns a default value (None if not specified).
#Example of get() function on a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# print(d.get('name')) #output: John
# print(d.get('country')) #output: None
# print(d.get('country','USA')) #output: USA

#keys() - returns a view object that contains the keys of a dictionary
#Example of keys() function on a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# print(d.keys()) #output: dict_keys(['name', 'age', 'city']) 
#for x in d.keys():
#     print(x) #output: name age city

#values() - returns a view object that contains the values of a dictionary
#Example of values() function on a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# print(d.values()) #output: dict_values(['John', 30, 'New York 
#for x in d.values():
#     print(x) #output: John 30 New York

#items() - returns a view object that contains the key-value pairs of a dictionary as tuples
#Example of items() function on a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary  
# print(d.items()) #output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
#for k,v in d.items():
#     print(k,v) #output: name John age 30 city New York

#pop() - removes a specified key-value pair from a dictionary and returns the value of the removed key. If the key is not found, it raises a KeyError.
#Example of pop() function on a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# age=d.pop('age') #removing a key-value pair from a dictionary and returning the value of the removed key
# print(d) #output: {'name': 'John', 'city': 'New York'}
# print(age) #output: 30

#popitem() - removes and returns an arbitrary key-value pair from a dictionary as a tuple. If the dictionary is empty, it raises a KeyError.
#Example of popitem() function on a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# item=d.popitem() #removing and returning an arbitrary key-value pair from a dictionary as a tuple
# print(d) #output: {'name': 'John', 'age': 30}

#Aliasing
#Aliasing is the process of creating a new reference to an existing object in memory. When you assign a dictionary to a new variable, both variables point to the same dictionary in memory. This means that changes made to the dictionary through one variable will affect the other variable as well.
#Example of aliasing in dictionaries
# d={'name':'John','age':30,'city':'New York'} #dictionary
# d1=d #d1 is an alias of d
# d1['age']=31 #modifying a value in the dictionary through d1
# print(d) #output: {'name': 'John', 'age': 31,
# print(d1) #output: {'name': 'John', 'age': 31, 'city': 'New York'}

#copying a dictionary
#Copying a dictionary creates a new dictionary object in memory with the same key-value pairs as
#the original dictionary. Changes made to the copied dictionary will not affect the original dictionary and vice versa.
#Example of copying a dictionary    
# d={'name':'John','age':30,'city':'New York'} #dictionary  
# d1=d.copy() #creating a copy of the dictionary
# d1['age']=31 #modifying a value in the copied dictionary  

#setdefault() - returns the value of a specified key in a dictionary. If the key is not found, it inserts the key with a specified default value and returns the default value.
#Example of setdefault() function on a dictionary
# d={'name':'John','age':30,'city':'New York'} #dictionary
# print(d.setdefault('name','Jane')) #output: John
# print(d.setdefault('country','USA')) #output: USA
# print(d) #output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

#update() - updates a dictionary with key-value pairs from another dictionary or from an iterable of key-value pairs. If a key already exists in the dictionary, its value will be updated with the new value.
#Example of update() function on a dictionary 
# d={'name':'John','age':30,'city':'New York'} #dictionary
# d.update({'age':31,'country':'USA'}) #updating a dictionary with another dictionary
# print(d) #output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}
# d.update(name='Jane',age=25) #updating a dictionary with key-value
# print(d) #output: {'name': 'Jane', 'age': 25, 'city': 'New York', 'country': 'USA'}

#dictionary comprehension
#Dictionary comprehension is a concise way to create dictionaries. It consists of an expression followed by a for clause, and optionally, one or more if clauses. The expression is evaluated for each item in the iterable, and the resulting key-value pairs are added to the dictionary.
#Example of dictionary comprehension
# squares={x:x**2 for x in range(10)} #dictionary comprehension to create a dictionary of squares
# print(squares) #output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#Merging of collections
# l1=[(100,'John'),(200,'Jane'),(300,'Smith')] #list of tuples
# l2={'name':'John','age':30,'city':'New York'} #dictionary
# l3=[*l1, *l2]
# print(l3) #output: [(100, 'John'), (200, 'Jane'), (300, 'Smith'), 'name', 'age', 'city']

# t1=(10,20,30) #tuple
# t2=(40,50,60) #tuple
# t3=(*t1, *t2)
# print(t3) #output: (10, 20, 30, 40, 50, 60)

# s1={10,20,30} #set
# s2={40,50,60} #set
# s3={*s1, *s2}
# print(s3) #output: {40, 10, 50, 20, 60, 30}

# d1={'name':'John','age':30,'city':'New York'} #dictionary
# d2={'country':'USA','occupation':'Developer'} #dictionary
# d3={**d1, **d2}
# print(d3) #output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA', 'occupation': 'Developer'}
  

#Nested Collections
#A nested collection is a collection that contains other collections as its elements. You can have nested lists, nested tuples, nested sets, and nested dictionaries. Nested collections can be used to represent complex data structures and can be accessed using multiple levels of indexing or key access.
#Example of nested collections  
# nested_list=[[1,2,3],[4,5,6],[7,8,9]] #nested list
# print(nested_list) #output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nested_tuple=((1,2,3),(4,5,6),(7,8,9)) #nested tuple
# print(nested_tuple) #output: ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# nested_set={frozenset({1,2,3}), frozenset({4,5,6}), frozenset({7,8,9})} #nested set
# print(nested_set) #output: {frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9})}
# nested_dict={'dict1':{'name':'John','age':30},'dict2':{'name':'Jane','age':25}} #nested dictionary
# print(nested_dict) #output: {'dict1': {'name': 'John', 'age': 30}, 'dict2': {'name': 'Jane', 'age': 25}}  
