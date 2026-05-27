#set
#set is a collection of unique elements
#sets are unordered and unindexed
#duplicates are not allowed in sets
#sets are mutable but the elements of a set must be immutable
#insertion order is not preserved in sets.we cannot access the elements of a set using their index because sets are unordered and unindexed
#sets are defined using curly braces {} or the set() function
#Indexing and slicing is not possible in sets because sets are unordered and unindexed

# s={}#yo chahi dictionary ho
# s1=set(s)#set ma paribartan garna parcha
# print(s1)
# print(type(s1))
# print(type(s))

#Important set functions
#add() - adds an element to a set
# s={10,20,30}
# s.add(40)#adds an element to a set
# print(s)

#update() - adds multiple elements to a set
# s={10,20,30}
# s.update([40,50,60])#adds multiple elements to a set
# print(s)

#Aliasing and copying sets
#Aliasing is when two or more variables refer to the same object in memory. In this case, changes made to one variable will affect the other variable because they are referring to the same object.
#Copying is when a new object is created in memory and the values of the original object are copied to the new object. In this case, changes made to one variable will not affect the other variable because they are referring to different objects in memory.
#Example of aliasing and copying sets
# s1={10,20,30}
# s2=s1 #s2 is an alias of s1 
# s2.add(40)
# print(s1)
# print(s2)

# s={10,20,30,40,10}
# s1=s.copy() #s1 is a copy of s
# s1.add(50)
# print(s)
# print(s1)

#pop() - removes and returns an arbitrary element from a set
# s={10,20,30,40,50}
# print(s.pop())#removes and returns an arbitrary element from a set

#remove() - removes a specified element from a set #if the element is not present in the set, it raises a KeyError
# s={10,20,30,40,50}
# s.remove(30)#removes a specified element from a set 30 is present in the set
# print(s)

#discard() - removes a specified element from a set if it is present # if the element is not present in the set, it does nothing
# s={10,20,30,40,50}  
# s.discard(30)#removes a specified element from a set if it is present
# print(s)

#clear() - removes all elements from a set
# s={10,20,30,40,50}  
# s.clear()#removes all elements from a set
# print(s)

#Mathematical operations on sets
#union() - returns a new set that contains all the elements from both sets  
# s1={10,20,30}
# s2={30,40,50}
# print(s1.union(s2))#returns a new set that contains all the elements from both sets

#intersection() - returns a new set that contains only the elements that are common to both sets
# s1={10,20,30}
# s2={30,40,50}
# print(s1.intersection(s2))#returns a new set that contains only the elements that are common to both sets

#difference() - returns a new set that contains only the elements that are present in the first set but not in the second set
# s1={10,20,30}
# s2={30,40,50}
# print(s1.difference(s2))#returns a new set that contains only the elements that are present in the first set but not in the second set

#symmetric_difference() - returns a new set that contains only the elements that are present in either set but not in both sets
# s1={10,20,30}
# s2={30,40,50}
# print(s1.symmetric_difference(s2))#returns a new set that contains only the elements that are present in either set but not in both sets

#Membership operations on sets
#in - returns True if an element is present in a set, otherwise returns False 
# s={10,20,30,40,50}
# print(10 in s)#returns True if an element is present in a set, otherwise returns False
# print(100 in s)#returns True if an element is present in a set, otherwise returns False

#not in - returns True if an element is not present in a set, otherwise returns False
# s={10,20,30,40,50}    
# print(10 not in s)#returns True if an element is not present in a set, otherwise returns False
# print(100 not in s)#returns True if an element is not present in a set, otherwise returns False

#operator that are not valid for sets
#+ - * / % ** // = == != > < >= <= [] () {} @ \ | & ^ ~   not in - is not valid for sets because sets are unordered and unindexed

#set comprehension - a concise way to create sets
# The process of creating a set by iterating over an iterable and applying a condition to filter the elements is called set comprehension.
#Example of set comprehension
# s={x for x in range(10) if x%2==0}#set comprehension
# print(s)  

#Heterogeneous sets - a set that contains elements of different data types
# s={10,"hello",3.14,(1,2,3),[4,5,6],{7,8,9}}#heterogeneous set
# print(s) #output: {10, 'hello', 3.14, (1, 2, 3), [4, 5, 6], {7, 8, 9}}