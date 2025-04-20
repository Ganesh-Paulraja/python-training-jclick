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

# > python -m pip install mysql-connector-python

import mysql.connector

mysql.connector.connect(host = "localhost", username = "root", password="805661@figma")