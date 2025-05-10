# db: Library

# Table -1- BookMaster

# bcd  int  -- book code
# bna  vc -- 
# au1  vc
# au2  vc
# pub  vc
# puc  vc
# edn  vc -- edition name
# yed  int
# prc  float
# noc  int  --copy

# Table - 2 - MemberMaster

# mcd  int --
# mna  vc
# ad1  vc
# ad2  vc
# mob  vc
# mid  vc
# occ vc
# idp  vc
# ipn  vc
# ncr  int

# Table - 3- BookIssues
# change nu buook, nu card

# bcd
# bna
# pub
# prc
# mcd
# mna
# mob
# mid
# idp
# isd 
# rmk
# sta 
import mysql.connector

print('WELCOME TO LIBRARY')

mydb = mysql.connector.connect(host = "localhost", username = "root", password="805661@figma", database = "librarydb")
mycursor = mydb.cursor()
# sql = """
# CREATE TABLE book_data (
#   bookcode INT(10),
#   bookname VARCHAR(40),
#   auther1 VARCHAR(40),
#   auther2 VARCHAR(40),
#   publication VARCHAR(40),
#   publisher VARCHAR(40),
#   edition VARCHAR(40),
#   year_of_edition VARCHAR(10),
#   price FLOAT(10),
#   number_of_copy INT(10)
# )
# """


# sql = """
# CREATE TABLE member_data (
#   member_code INT(10),
#   name VARCHAR(40),
#   address1 VARCHAR(40),
#   address2 VARCHAR(40),
#   mobile VARCHAR(40),
#   emailId VARCHAR(40),
#   occupation VARCHAR(40),
#   id_proof VARCHAR(40),
#   id_proof_number VARCHAR(40),
#   number_of_cards INT(10)
# )
# """

# sql = """
# CREATE TABLE checkout_data (
#   bookcode INT(10),
#   bookname VARCHAR(40),
#   publication VARCHAR(40),
#   price FLOAT(10),
#   member_code INT(10),
#   name VARCHAR(40),
#   mobile VARCHAR(40),
#   emailId VARCHAR(40),
#   id_proof_number VARCHAR(40),
#   issued_datte VARCHAR(20),
#   remark VARCHAR(20),
#   statement VARCHAR(20)
# )
# """

# mycursor.execute(sql)
# mydb.commit()
# print('created successfully.')

over = True

while over:
    userOption = int(input('Enter (number) \n 1. Enter New Book \n 2. Join As New Member \n 3. Checkout Book \n 4. Return Book \n 5. Check All Book \n 6. Stop  \n : '))

    if userOption == 1:
        bookcode = int(input('Enter book code (number): '))
        bookname = input('Book name: ')
        auther1 = input('Author name: ')
        auther2 = input('Sub-author name: ')
        publication = input('Publication name: ')
        publisher = input('Publisher name: ')
        edition = input('Edition: ')
        year_of_edition = int(input('Year of edition (number): '))
        price = float(input('Enter price of book (number): '))
        number_of_copy = int(input('Enter number of copies (number): '))

        val = (bookcode, bookname, auther1, auther2, publication, publisher, edition, year_of_edition, price, number_of_copy)
        sql = "insert into book_data values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, val)
        mydb.commit()
        print('book added successfully')

    elif userOption == 2:
        member_code = int(input('Enter member code (number): '))
        name = input('Enter member name: ')
        address1 = input('Enter address line 1: ')
        address2 = input('Enter address line 2: ')
        mobile = input('Enter mobile number: ')
        mailId = input('Enter email ID: ')
        occupation = input('Enter occupation: ')
        id_proof = input('Enter ID proof name: ')
        id_proof_number = input('Enter ID proof number: ')
        number_of_cards = int(input('Enter number of cards: '))
        val = (member_code, name, address1, address2, mobile, mailId, occupation, id_proof, id_proof_number, number_of_cards)
        sql = "insert into member_data values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, val)
        mydb.commit()
        print('member added successfully')

    elif userOption == 3:
        from datetime import date
        book_code = int(input('Enter book code (number): '))
        member_code = int(input('Enter your member code (number): '))
        sql = "select * from book_data where bookcode = %s"
        val = (book_code,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        mydb.commit()
        book_name = result[0][1]
        print('book name', book_name)
        publication = result[0][4]
        price = result[0][8]
        book_count = result[0][9]

        sqlTwo = "select * from member_data where member_code = %s"
        valTwo = (member_code,)
        mycursor.execute(sqlTwo, valTwo)
        resultTwo = mycursor.fetchall()
        member_name = resultTwo[0][1]
        mobile = resultTwo[0][4]
        mailId = resultTwo[0][5]
        id_proof = resultTwo[0][4]
        today = date.today()
        issued_date = today.strftime("%d-%b-%Y")
        remark = input('Enter book return date: ')
        staement = 'True'
        number_of_cards = resultTwo[0][9]

        if book_count == 0:
            print('no book left')
            break

        if number_of_cards == 0:
           print('no card lef')
           break


        totalVal = (book_code, book_name, publication, price, member_code, member_name, mobile, mailId, id_proof, issued_date, remark, staement)
        print(totalVal)
        totalsql = "insert into checkout_data values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        bookupdate_sql = "UPDATE book_data SET number_of_copy = number_of_copy - 1 WHERE bookcode = %s"
        member_update_sql = "UPDATE member_data SET number_of_cards = number_of_cards - 1 WHERE member_code = %s"
        mycursor.execute(bookupdate_sql, val)
        mycursor.execute(member_update_sql, valTwo)
        mycursor.execute(totalsql, totalVal)
        mydb.commit()
        print('book taken successfully')

    elif userOption == 4:
        book_code = int(input('Enter book code (number): '))
        member_code = int(input('Enter your member code (number): '))
        check_sql = """SELECT * FROM checkout_data WHERE bookcode = %s AND member_code = %s AND statement = 'True'"""
        mycursor.execute(check_sql, (book_code, member_code))
        record = mycursor.fetchall()
        if record:
            val = (book_code,)
            valTwo = (member_code,)
            update_checkout_sql = """UPDATE checkout_data SET statement = 'False' WHERE bookcode = %s AND member_code = %s"""
            mycursor.execute(update_checkout_sql, (book_code, member_code))
            bookupdate_sql = "UPDATE book_data SET number_of_copy = number_of_copy + 1 WHERE bookcode = %s"
            member_update_sql = "UPDATE member_data SET number_of_cards = number_of_cards + 1 WHERE member_code = %s"
            mycursor.execute(bookupdate_sql, val)
            mycursor.execute(member_update_sql, valTwo)
            mydb.commit()
            print('book submited successfully')
        else:
            print('wronk user and book')

    elif userOption == 5:
        sql = "SELECT bookcode, bookname FROM book_data"
        mycursor.execute(sql)
        books = mycursor.fetchall()
        print(books)
        for book in books:
            print(book[0], ' ', book[1])
    elif userOption == 6:
        over = False
