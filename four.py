# DBMS
# Server
# compute server --> data calculation
# data server --> storing data
# web server --> video audio
# print server --> private print sharing

# DBMS --> Procedural languages

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
    # > delete from <table-name> [where <condition>]

#7 Dropping Table
    # > drop table <table-name>

#8 Dropping DB
   # > drop database <database-name>

# Functions
   # max()
   # min()
   # sum()
   # avg()
   # count()
   # ceiling()
   # floor()
   # tabs()
   
   #clauses
   # between 
   # in
   # not in
   # order by
   # group by
   # union
   # intersect

   # Constraints
   # primary key
   # foreign key 
   # null
   # not null 
   # unique 
   # check

# > python -m pip install mysql-connector-pythonf

# import mysql.connector

# mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma", database = "Ganeshdb")
# print("Connection Established")
# # print()

# mycursor = mydb.cursor()
# # sql = "create database ganeshdb"
# sql = "create table personal(eid int, ena varchar(40), grd varchar(2), dep varchar(30), deg varchar(30))"

# mycursor.execute(sql)

# print("DB Created Successfully")

# ---------------------------------------
# import mysql.connector

# mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma", database = "Ganeshdb")

# mycursor = mydb.cursor()

# ch = "y"
# while ch == 'y':
#     d1 = int(input("Enter employee id"))
#     d2 = input("Enter employee name")
#     d3 = input("Enter employee grade")
#     d4 = input("Enter employee department")
#     d5 = input("Enter employee Designation") 
#     val = (d1, d2, d3, d4, d5)
#     sql = "insert into personal values(%s, %s, %s, %s, %s)"
#     mycursor.execute(sql, val)
#     mydb.commit()

#     ch = input("anymore employes to add")


#single quote important
# val = (1, 'Arun', 'A', 'Computer', 'Programmer')
# sql = "insert into personal values(%s, %s, %s, %s, %s)"

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "records inserted")


# ------------------------------------------------------

# import mysql.connector

# mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma", database = "Ganeshdb")

# mycursor = mydb.cursor()
# sql= "select *from personal"
# mycursor.execute(sql)
# resultet = mycursor.fetchall()

# for x in resultet:
#     print(x)

# print(mycursor.rowcount, "records viewed")
# ------------------------------------------------------------

# import mysql.connector

# mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma", database = "Ganeshdb")

# cursor = mydb.cursor()
# # sql= "select *from personal where grd='A'"
# # sql= "select *from personal where bpa>=20000 and bpa<25000"
# # sql= "select *from personal where bpa between 20000 and 25000"
# # sql = "select max(bpa) from personal"
# # sql = "select min(bpa) from personal"
# # sql = "select sum(bpa) from personal"
# # sql = "select avg(bpa) from personal"
# # sql = "select count(*) from personal"
# # sql= "select *from personal where not grd='A'"
# # sql= "select *from personal where grd in ('A')"
# sql= "select *from personal where grd not in ('A')"
# # sql= "select *from personal where grd not in ('A')"
# # sql= "select *from personal where ena like 'A%"
# # sql= "select *from personal where ena like '%l"
# # sql= "select *from personal where ena like '_u%"

# cursor.execute('UPDATE employees SET salary = 50000 WHERE name = "Alice"')
# cursor.execute('UPDATE employees SET salary = 55000 WHERE name = "Bob"')
# cursor.execute('UPDATE employees SET salary = 60000 WHERE name = "Charlie"')
# cursor.execute('UPDATE employees SET salary = 65000 WHERE name = "David"')

# mydb.commit()

# mycursor.execute(sql)
# resultet = mycursor.fetchall()

# print(resultet)

# for x in resultet:
#     print(x)

# print(mycursor.rowcount, "records viewed")

# --------------------------------------------------------------
# import mysql.connector

# mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma")

# cursor = mydb.cursor()
# # --------------------------------------------
# sql = 'create database ganesh2'
# # ------------------------------------------

# sql = "update personal set bpa=bpa+2500 where grd = 'A'"
# sql = "update personal set ena='A.Arun' where eid=1"
# cursor.execute(sql)
# cursor.execute("UPDATE personal SET salary = 50000 WHERE eid = '1'")
# cursor.execute('UPDATE personal SET salary = 55000 WHERE eid = "2"')
# cursor.execute('UPDATE personal SET salary = 60000 WHERE eid = "3"')
# cursor.execute('UPDATE personal SET salary = 65000 WHERE eid = "4"')

# sql = "delete from personal where grd='b'"

# sql = "drop table personal"

# sql = "drop database ganeshdb"
# cursor.execute(sql)


# mydb.commit()

# print("table droped")
# -------------------------------------------------

# import mysql.connector
# mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma", database = "ganeshbanking" )

# mycursor = mydb.cursor()
# sql = "create table newacc(acn int primary key, ana varchar(30) not null, ad1 varchar(30), ad2 varchar(30), act varchar(10), ref varchar(20), opd varchar(12), oam int, trd varchar(12),cbl int)"

# d1 = int(input("Enter Account Number"))
# d2 = input("Enter Account Holder's Name")
# d3 = input("Enter Address Field 1")
# d4 = input("Enter Address Field 2")
# d5 = input("Enter Account Type")
# d6 = input ("Enter Reference")
# d7 = input("Enter Account Opening Date")
# d8 = int(input("Enter Opening Amount"))

# val = (d1, d2, d3, d4, d5, d6, d7, d8, d7, d8)
# sql = "insert into newacc values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# # mycursor.execute(sql)
# mycursor.execute(sql, val)
# mydb.commit()

# print(mycursor.rowcount, 'database created')
# -------------------------------------------------------------

# import mysql.connector
# mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma", database = "ganeshbanking" )

# mycursor = mydb.cursor()
# sql = "create table payin(acn int primary key, pad varchar(12), amp int)"

# d1 = int(input("Enter Account Number"))
# d2 = input("Enter Date of Payment")
# d3 = int(input("Enter Payin Amount"))

# val = (d1, d2, d3)
# sql = "insert into payin values(%s, %s, %s)"

# # mycursor.execute(sql)
# mycursor.execute(sql, val)

# val1 = (d2, d3, d1)
# sql1 = "update newacc set trd=%s, cbl= cbl+ %s where acn = %s"
# mycursor.execute(sql1, val1)

# mydb.commit()

# print(mycursor.rowcount, 'database created')
# -------------------withdraw table--------------------------------------

import mysql.connector
mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma", database = "ganeshbanking" )

mycursor = mydb.cursor()
# sql = "create table withdraw(acn int primary key, wd varchar(12), amw int)"

# mycursor.execute(sql)

d1 = int(input("Enter Account Number"))
d2 = input("Enter Date of withdraw")
d3 = int(input("Enter withdraw Amount"))

val = (d1, d2, d3)
sql = "insert into witdraw values(%s, %s, %s)"
mycursor.execute(sql)

val1 = (d2, d3, d1)
sql1 = "update newacc set trd=%s, cbl= cbl- %s where acn = %s"
mycursor.execute(sql1, val1)

mydb.commit()

# -----------------------------------------------------






