# s="python"
# print(type(s))

#use of doc string
# s='''my
# name 
# is 
# python
# '''
# print(s)

#use of Escape sequence in string
# s='My name is \n Python'
# a="My name is \"Python\""
# print(s)
# print(a)

#use of Indexing
# s="python is fun"
# print(s[4])
# print(s[-9])

#Example of Indexing
# s="python is fun"
# i=0
# print("Index of given string in both positive and negative index")
# for x in s:
#   print(f"The character {x} is present at positive {i} index and negative {i-len(s) } index")
#   i=i+1

#Example of slicing operator
# s="Hello world this is python"
# print(s[0:5])
# print(s[0:5:2])

#Example2 of slicing operator
# s="Hello world this is python"
# print(s[::-1])
# b=reversed(s)
# for x in b:
#   print(x,end="")

#Behaviour of slice operator
# s="abcdefghijkl"
# print(s[1:6:1])
# print(s[::1])
# print(s[::-1])
# print(s[3:7:-1])
# print(s[7:4:-1])
# print(s[-4:1:-1])
# print(s[-4:1:1])

#Mathematical operation in string
# print("Hello" +"world")
# print("Hello" * 8)

#stringko length pata lagaune method
# a='python'
# print(len(a))
# print(a._len_())

#Membership operator in string(in,not in)
# a='python'
# print('p' in a)
# print('p' not in a)

#comparision operter in string
# a='apple'
# b='apple'

# print(a=b)

#ASCII value patha lagauna
# print(chr(98))
# print(ord('b'))

#Userle input dida space rakhyo vani wrong output aauna sakxa
#So , to solve this hami rstrip(),lstrip() ra strip() use garxau
# name=input('Enter any name you like : ').strip()#Chaining of funciton baninxa yaslai
# if name=='Sujan':
#   print("your name is correct")
# else:
#   print("Wrong name.")

#finding substring in string
#four function is used find(),rfind(),index() and rindex()
# a="Learning Python is fun"
# print(a.find('i'))
# print(a.find('i',7,10))
# print(a.rfind('i'))

#kati ota xa vanera pata lagauna count() use garxau
# a="Learning Python is fun"
# print(a.count('i'))
# print(a.count('i',10,15))

#Replacing substring we use replace
#string immutable ho tara yaha purai referece id change gardinxa replace gare paxi mathiko value GC janxa 
# a=" Python is always beautiful"
# print(a.replace('beautiful','easy'))

#Splitting of string
# a=" Python is always beautiful".split()
# print(a)
# for i in a:
#   print(i)

#Splitting of string example 2
# a="2083-02-10".split('-')
# for i in a:
#   print(i)


#Join join()
# l=['Python', 'is', 'always', 'beautiful']
# t=('Python', 'is', 'always', 'beautiful')
# a=' '.join(l)
# b=' '.join(t)
# print(a)
# print(b)

#Changing case of string(upper(),lower(),swapcase(),title(),captialize)

# a=" python is always BEAUTIFUL"
# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.title())
# print(a.capitalize())

#Checking starting and ending part of string
#startswith() and endswith()

# s="Learning python is fun"
# print(s.startswith('L'))
# print(s.startswith('Learning'))
# print(s.endswith('n'))
# print(s.endswith('fun'))

#To check type of characters present in a string

# print("LearningPython312".isalnum())
# print("LearningPython".isalpha())
# print("312".isdigit())
# print("hellohello".islower())
# print('HELLOHEOLOAA'.isupper())
# print(" ".isspace())
# print("Python Is Fun".istitle())

#Formatting of string

# name='prayan'
# age=20

# print(f"My name is {name} and my age is {age}")
# print("My name is {0} and my age is {1}".format(name,age))
# print("My name is {a} and my age is {b}".format(a=name,b=age))

# print("The integer number is {}".format(123))
# print("The integer number is {:d}".format(123))
# print("The integer number is {:5d}".format(123))
# print("The integer number is {:05d}".format(123))






