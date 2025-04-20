# for x in range(10):
#     print(x)

# t = int(input("Enter which table: "))
# n = int(input("Enter the times: "))

# for i in range(1, n+1):
#     print(f'{i} * {t} = {i * t}')


# if (i == 5 ): break for loop
#     break

#    continue --> continue will skip the number

# while <condition>:
#     statement()
#     change condition


# n = 125

# s = 0

# while n > 0:
#     r = n % 10
#     s = s + r
#     n = int(n/10)

# print(s)

# n = int(input('Enter YOur Number: '))
# m = n
# s = 0

# while m > 0:
#     r = m % 10 
#     s += r ** 3
#     m = int(m/10)

# if n == s:
#     print('This is amstrong number')
# else:
#     print("This is not amstrong number")


# Array  --> 
# 0 to n-1 index

# int a[5] = {1, 2, 3, 4,5}
#  --> free null

# structure 
# function
# oops
# data = ['10', 20, 30, 40, 50, 60]

# print(data[1])

# for i in range(6):
#   print(data[i])

# for j in range(0,6,2):
#   print(data[j])
  
# for k in range(5, -1, -1):
#   print(data[k])

# ----------------------------------------

# data = [11, 25, 87, 13, 24]

# res = data[0]

# for i in range(1, 5):
#     if data[i] > res:
#         res = data[i]

# print("Biggest no:", res)

# ---------------

# o = 0
# e = 0

# for i in range(5):
#     if data[i]%2 == 1:
#         0 += 1
#     else: 
#         e += 1
# print("Odd", o)
# print("Even", e)
# -----------------------------

# ****************
# data = [12, 25, 87, 13, 24]

# for i in range(5):
#     for j in range(i+1, 5):
#         if data[i] > data[j]:
#             t = data[i]
#             data[i] = data[j]
#             data[j] = t

# for k in range(5):
#     print(data[k])


# Array-Object (Dynamic Array)
# list
# tuple
# set
# dict
    

# List
#   1. Ordered
#   2. changable
#   3. Indexed 
#   4. written[]

# data = [10, 20, 30, 40, 50]  # int array
# data2 = ["apple", "orange"]  # str array
# # decimal, bolean arrays

# # if string present that is string array
# data5 = [10, 'apple', 'a', True] #String array

# Accessing data

data1 = ["Suzuki", "Toyota", "Honda", "Tata", "Manindra"]

# print(data1)
# print(data1[1])
# print(data1[3])
# # range in array
# print(data1[:3])
# print(data1[:])
# print(data1[::2])

# print(data1[-1])
# print(data1[-4, -2])

# # Array items loop
# for j in data1:
#     print(j)
# -------------------------
# print(len(data1))
data1.append("Hundai")

# if ele in data1: # Case Sensitive
#     print("Availiable")

data1.remove("Honda")
data1.pop() # remove last
data1.pop(1) #remove index
# del data1[3] #remove index

data1.clear() #clear array

# data1.append('red')
# data1.append('blue')
# data1.append('green')

# print(data1)

# ------------------------



data1 = ["Suzuki", "Toyota", "Honda"]
data2 = ["BMW", "Benz", "Standard"]

# data3 = data1 + data2
# print(data3)
# print(len(data3))

# data1.extend(data2) #changes data1 value
# print(data1)

# for x in data2: 
#     data1.append(x)

# print(data1)

# data2 = data1.copy()
# data3 = data1

# data1.clear()
# data1.append("Apple")
# data1.append("Orange")
# print(data2) #old data1
# print(data3) #new data1

# data4 = list(data1) #same like .copy

# print(data4)

# Tuple
# Collection 
# Ordered
# Unchangeable
# indexed 
# written with ()

data = ("red", "Green", "Blue", "Yellow", "Orange")

# print(data)

# print(data[2])
# print(data[4])

# print(data[2:])
# print(data[:2])
# print(data[::])
# print(data[::2])

# print(data[-2])
# print(data[-4:-2])
# -----------------------------
# data.pop() --> modification makes error

#accessing not makes errro
#concat works
#len works
#in works

# --------------------
# data1 = list(data) 
# data1.pop()
# data = tuple(data1) 
# -----------------------

# print("Blue" in data)
# -------------------------------------------
# Set
# set is a collection
# unordered
# changeble
# unindexed

# data = {"Red", "Green", "Blue", "Yellow", "Orange"}

# # print(data[0])

# for x in data:
#     print(x)

# ele = "Red"

# if ele in data:
#     print("Color Availiable")
# else:
#     print("It's not Availiable")

# print(len(data))
# data.add("Black")
# data.remove("Blue")
# #remove or skip
# data.discard("Yellow")

# data.pop() #first item removed

# data.clear()

# data2 = {"Black", "Cyan", "Brown", "Yellow", "White"}

# data3 = data.union(data2)
# print(data3)

# print(data.update(data2)) #set won't allow duplicates

# del data1
#If I print it will show error

# -------------------------------------------

# Dict : Dictionary
# An element is a colection of key and value, separated by:

# Collection
# Ordered

# to access the element, use the key, not the indext no

data = {
    "Brand" : "Suzuki",
    "Name" : "Ertiga",
    "Color" : "White",
    "Version" : "ZXI",
    "Year" : "2020",
}

# print(len(data))
# print(data["Brand"])

# for x in data: #print key only
#     print(x)

# for y in data.items(): #dict to tuple
#     print(y)

# for z in data.values(): #print only values
#     print(z)

# for m,n in data.items(): #print key, value
#     print(m, n)

# key = 'Brand'
# #availiablity check with key
# if (key in data):
#     print("Availiable")
# else:
#     print("not Availiable")
#   #we can't check availiablity of valuey

# #existing key replace new key add item

# data["color"] = "Silver"
# data["Air-Bag"] = "Dual"

# print(len(data))

# # remove with key
# data.pop("color")
# data.popitem()
# data.clear()
# del data
# print(len(data))
# ---------------------------------------

# function

# User-Defined Fucntions
# Pre-Defined Fucntions
    # String 
    # Math
    # Date


# void get()
# {
#     code
# }

# def get([parameter-list]): - callie
#     code

# fucntion-name([arguments]) - caller

# def display():
#     print("Hello")

# display()

# def add ():
#     n1 = input("Enter first number")
#     n2 = input("Enter second number")
#     r1 = n1 + n2
#     print(r1)

# def sub ():
#     n1 = input("Enter first number")
#     n2 = input("Enter second number")
#     r1 = n1 - n2
#     print(r1)

# def mul ():
#     n1 = input("Enter first number")
#     n2 = input("Enter second number")
#     r1 = n1 * n2
#     print(r1)

# def div ():
#     n1 = input("Enter first number")
#     n2 = input("Enter second number")
#     r1 = n1 / n2
#     print(r1)

# ch = int(input("Enter your choice \n1.Add \n2.Sub \n3.Mul \n4.Div \n"))
# if ch == 1:
#     add()
# elif ch == 2:
#     sub()
# elif ch == 3:
#     mul()
# else:
#     div()


# def mulTab(t, n):
    
#     for x in range (1, n+1):
#         m = t * x
#         print(x, 'x', t , '=' , m)

# t = int(input("Enter Which Table"))
# n = int(input("Enter number of times"))

# mulTab(t, n)

# def mulTab(p, q, r):
#     if p>q and p>r:
#         return p
#     elif q > r and q > p:
#         return q
#     else:
#         return r

# n1 = int(input("Enter first number"))
# n2 = int(input("Enter second number"))
# n3 = int(input("Enter third number"))

# print("Biggest no: ", mulTab(n1, n2, n3))

# def dtb(d,  m, y):
#     print(d, '/' , m, '/', y)

# dtb("07", "05", "2000")
# dtb("06", "06", "2003")
# dtb("12", "09", "2020")

# def getData(d1, d2, d3):
#     print(d1, d2, d3)

# getData(1, 20, 30)
# getData(11.11, 22.22, 33.33)
# getData("Red", "Green", "Blue")
# getData("True", False, True) 

# String Functions
# string is a strequence of charectors

# 1.len() --> count total including spaces
str = 'information technology'
l = len(str)
# print(l)

# for i in range(l):
#     print(str[i])

# for j in range(l-1, -1, -1):
#     print(str[j])

# for k in range(0,l,2):
#     print(str[k])

# c = input('Enter the char')

# cou = 0

# for i in range(l):
#     if str[i] ==  c:
#         cou = cou + 1

# print("Counts: ", cou)

# str = 'information technology'
# cou = 0
# v = ['a', 'e','i', 'o', 'u']

# for i in range(len(str)):
#     c = str[i]
#     if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
#       cou = cou + 1

# print("Counts:", cou)

# str = 'malayalam' #palindrome

# ans = True
# for i in range(len(str)):
#     if str[i] != str[len(str) -1]:
#         ans = False

# l = len(str)
# t = 0

# for i in range(l):
#     fc = str[i]
#     lc = str[l-1]
#     if fc == lc:
#         t=0
#         l=l-1
#     else:
#         t = 1
#         break

# if t == 0:
#     print("String is Palindrome")
# else: 
#     print("String is Not Palindrome")


# 2. Upper()
# 3. Lower()
# 4. Tittle()
# 5. swapcase()
# 6. Capitalize()

str1 = 'Apple'
str2 = 'BannAna'

# print(str1.upper())
# print(str2.upper())

# print(str1.lower())
# print(str2.lower())

# 4. startswith()
# 5. endswith()

# print(str1.startswith("Ap"))
# print(str2.endswith('le'))

# 6. title()

# str1 = 'cOMpaNy PrOFile'
# print(str1.title())

# 7.strip()
# str1 = '   Apple   '

# print(len(str1))

# str2 = str2.strip()

# print(len(str2))

# 8. isupper(), isLower()
str1 = 'APPLE'
str2 = 'apple@123' 
# print(str2.lower()) # still true

# print(str1.isupper())

#9. istitle()

str = "inFOrmation teCHNOLogy"

# if str.istitle() == True:
#     print(str)
# else:
#     print(str.title())

# isalnum()  --> if it has spacial char show false

str1 = "ABC123"
str2 = '123'
str3 = 'ab@12'

# print(str1.isalnum())
# print(str2.isalnum())
# print(str3.isalnum())

# isspace()
str1 = ' '
str2 = '  App' #False
# print(str1.isspace())
# print(str2.isspace())

#is digit() or isnumeric() --> check only a number
# print(str1.isdigit())
 
# str2 = '12345'
# print(str2.isnumeric())

#isapha()

# str1 = 'ABCD'
# str2 = 'ABC@' #False
# print(str1.isalpha())
# print(str2.isalpha())

# 15.find() or index()
# str = "Apple is red in color, strawberry also red in color"

# print(str.find('red'))
# print(str.index('red'))

# # 16.capitalize() --> sentance first letter

# str = 'appLe IS red in CoLoR'
# print(str.capitalize())

# # 17.format()
# name = 'Arun'
# age = 12
# grade = 'VII'

# My name is Arun, Age is 12 and studying in Grade VII
#My name is Arun, studying in Grade Vii and age is 12

# op1 = "My name is" + name + ", Age is" + str(age) + "and studying in Grade " + grade
# op2 = "My name is" + ", studying in Grade" + "Vii" + "and age is 12"
# op3 = "My name is {}, grade is {} and styding in grade {}".format(name, age, grade)
# print(op2)
# print(op3)
# op4 = "My name is {} studying in Grade {} and age is {}".format(name, grade, age)
# print(op4)

# 19.int()
# float()
# str()

# a = 5
# b = 5 
# c = a+b 
# print(c)

# d = "5"
# e = 5
# f = d + Str(e)
# print(f)

# g = "5"
# h = 5
# i = int(g) + h
# print(i)


# # replace()
# str = "Apple is red in color, chilli also red in color"

# print(str.replace("red", "green"))

#split() --> convert string to list
# str = "Apple is red in color"
# str1 = str.split()
# print(str1)

# MATH FUNCTIONS
# 1.abs

# n1 = 10
# n2 = 20

# res = n1 - n2
# print(res)
# print(abs(res))

# min , max
# print(max(10,10,90,12))
# print(min(10,10,90,12))

# 4.pow()
# print(pow(5,2))
# print(pow(3,3))

# 5.sqrt
# import math
# print(math.sqrt(9))

# 6. ceil(), 7. floor()
# print(math.ceil(12.001))
# print(math.ceil(-12.001))
# print(math.floor(12.001))
# print(math.floor(-12.001))

# --------------------------------------
# Date()
# now()
# import datetime
# crd = datetime.datetime.now()
# print(crd)
# print(crd.day)
# print(crd.month)
# print(crd.year)

# dtb = datetime.datetime(2000, 5, 7)
# print(dtb)
# print("Date of birth: ")
# ---------------------------------------

# directive   Description                   Example
# %a          Weekday, short version        Wed
# %A          Weekday, full version         Wednesday
# %w          Weekday as a number           3
#             0-6, 0 is Sunday              31
# %d          Day of month 01-31            Dec 
# %b          Month name, short version     December
# %B          Month name, full version      12
# %m          Month as a number 01-12       18
# %y          Year, short version,          2018
#             without century               
# %H          Hour 00-23                    17
# %I          Hour 00-12                    05

# print(dtb.strftime("%a"))
# print(dtb.strftime("%A"))
# print(dtb.strftime("%w"))
# print(dtb.strftime("%d"))
# print(dtb.strftime('%b'))
# print(dtb.strftime('%m'))
# print(dtb.strftime('%y'))
# print(dtb.strftime('%H'))
# print(dtb.strftime('%I'))


