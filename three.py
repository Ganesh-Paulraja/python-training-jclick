# print('hello')
#File handling
# open(fine-name.ext, mode)

# Mode 
# 1.'r' - Read
# 2. 'w' - write - Create the file. overwrite
# 3. 'a' - Apepend - Create the file, appending the content with the existing one
# 4. 'x' - create - creating the file, error, if the file already exists

# Functions
# write() -- to write the content to that file
# read() --> read the existing file
# read(n) --> specified number of charectors
# readline() --> read line by line 


# str = "Hello"

# # f = open('data1.txt', 'w')
# f = open('data1.txt', 'a')
# f.write(str)
# f.close() # --> recommended but not neccessary
# ---------------------------------------

# f = open('data1.txt', 'r')

# print(f.read())

# f.close
# -------------------------------------------

# d1 = input('Enter name')
# d2 = input("Enter father's name")
# d3 = input("Enter age")
# d4 = input("Enter address")
# d5 = input("Enter mobile number")
# d6 = input("Enter mail-id")

# data ="\nPERSON DATA" + "\nName: " + d1 + "\nFather's Name: " + d2 + "\nAge: " + d3 +"\nAddress: " + d4 + "\nMobile No: " + d5 + "\nEmail-id: " + d6

# f= open("personal.txt", "a")
# f.write(data)

# f.close()

# ----------------------------------------
# choice = int(input("Press 1 for read and 2 for write: "))

# cont = 'y'

# while cont == 'y': 
#     if choice == 1:
#         f = open("mark.txt", "r")
#         f1 = f.read()
#         print(f1)
#     else:
#         m1 = int(input("Enter marks 1: "))
#         m2 = int(input("Enter marks 2: "))
#         m3 = int(input("Enter marks 3: "))
#         m4 = int(input("Enter marks 4: "))
#         m5 = int(input("Enter marks 5: "))

#         tot = m1 + m2 + m3 + m4 + m5
#         avg = tot / 5

#         if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
#             res = "Pass"
#         else:
#             res = "Fail"

#         if avg >= 60 and res == "Pass":
#             cla = "First"
#         elif avg >= 50 and avg < 60 and res == "Pass":
#             cla = "Second"
#         elif avg >= 35 and avg < 50 and res == "Pass":
#             cla = "Third"
#         else:
#             cla = "No class"

#         report = (
#             "Marks Report\n"
#             f"Tamil: {m1}\n"
#             f"English: {m2}\n"
#             f"Math: {m3}\n"
#             f"Science: {m4}\n"
#             f"Social: {m5}\n"
#             f"Result: {res}\n"
#             f"Class: {cla}\n"
#         )

#         f= open("mark.txt", "a")
#         f.write(report + "\n")

#     cont = input("do you want to enter another student data")
        

    
# f = open("house.txt", "r")
# n = input("Enter the no of chars to read")
# print(f.read(n))
# f.close()

# f = open("mark.txt", "r")

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f.close()

# f = open("mark.txt", "r")

# for i in f:
#     print(i)

# # f.close()

# import os

# str = 'Information Technology'

# f = open("data2.txt", "x") # only creat no more changes
# f.write(str) # it will cause error 

# import os

# fna = input('Entter the file name to delete')

# os.remove(fna)

# print("File deleted")

# import os

# fna = input("Enter the file name to check")

# if os.path.existsd(fna)== True:
#     print("File Availiable")
# else:
#     print("File does not exists")

# import os

# os.rmdir("files")

# Exception Handling
# Is an abnorman condition, it arises if the execution not successfully completed

# to get the max number of result
# to prevent automatic termination of the program

# mistakes in programming
# 1. Syntax Error
    # Error in program statements
# 2. Logical Error
    # Mistakes by the user logic
    # print(10/0)

# try:
#       monitoring part
# excdpt: 
#       exceptional handling part
# else:
#       exceptional handling part


# n1 = 10
# n2 = 5
# n3 = 0

# try:
#     r1 = n1/n2
#     r2 = n2/n3
#     print(r1)
#     print(r2)
# except:
#     print("Exception Handled")
# else:  #(optional execute after except false)
#     print('No Exception Found')


# n = 10

# for x in range(-5, 5):
#     try:
#         r = n/x
#         print(r)
#     except:
#         print('Infinity')

# json
# loads()
# dumps()

# import json

# data = '{"RNo": 1, "Name": "Arun","Age": 12, "Place": "Nagercoil"}'

# print(data)
# print(len(data))
# print(data[3])
# data1 = json.loads(data)
# print(data1)
# print(data1["Name"])

# --------------------------------------
# import json
# data = '{"RNo": 1, "Name": "Arun","Age": 12, "Place": "Nagercoil"}'
# print(data)
# print(len(data))

# data1 = json.dumps(data)
# print(data1)
# print(len(data1))
# -------------------------------------------

# import json

# n1 = 10
# n2 = 20
# n3 = n1 + n2
# print(n3)

# n4 = json.dumps(n1) + json.dumps(n2)
# print(n4)

# ------------------------------------------
# typecasting

# import json
# print(json.dumps(10))
# print(json.dumps(22.22))
# print(json.dumps('Hello'))
# print(json.dumps(['Apple', 'Orange', 'Banana']))
# print(json.dumps([True, False, False]))
# print(json.dumps([None]))

# -------------------------------------------
# import json
# data = '{"RNo": 1, "Name": "Arun","Age": 12, "Place": "Nagercoil"}'
# print(data)
# print(json.dumps(data, indent=5))
# print(json.dumps(data, indent=10, separators=(".", "=")))
# -------------------------------------------

# DBMS
# Server
# compute server --> data calculation
# data server --> storing data
# web server --> video audio
# print server --> private print sharing

# DBMS

# include heading all this --> 1 table
# SINO    NAME    AGE    MAIL (field)
# 1       ARUN     12    arun@gmail.com --> 1 record
# 2.      Kannan   21    kannan123

#SINO MARKS     RESULT
# 1.    490       PASS
# 2.    230       FAIL

# Feild -- is a collection of chars or bytearray

# Record -- is a collection of fields

# Table -- is Collection of records

# DataBase -- is a colletion of intter-related tables

# DBMS -- WORKING WITH MORE THEN ONE DATABASES

# SQL -- Structured Query Language

# 1. Createing DB
#         > create database <database-name>

# 2. Creating Table 
#         > create table <table-name> (col-name1 type, col-name2 type,.....)

# 3. Inserting Records
        #   > insert into <table-name> values(data1, data2, ....)

#4. Viewing Records
      #  > select */col-name(s) from <table-name> [where <condition>]

#5. Updating Records
     # > update <table-name> set col-name=data, col-name=data,....[where <condition>]

#6. Deleteing Records

    # delete from <table-name(optional)> [where <condition>]

# Dropping Table
    #drop table <table-name>

# Dropping DB
    #Drop database <database-name>

# Functions

# max()
# min()
# sum()
# avg()
# count()
# ceiling()
# floor()
# pow()
# sqrt()
# abs()


