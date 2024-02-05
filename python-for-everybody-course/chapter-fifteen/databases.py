#Relational Databases
'''
* Relational databases model data by storing rows and columns in tables. The powe of the relational database lies in its ability to efficiently retrieve data from those tables and in particular where there are multiple tables 
and the relationships between those tables involved in the query.

#Terminology
* Database - contains many tables
* Relation (or table) - contains tuples and attributes
* Tuple (or row) - a set of fields that generally represents an "object" like a person or a music track
* Attribute (also column or field) - one of possibly many elements of data corresponding to the object represented by the row
'''

#SQL
'''
* Structured Query Language is the language we use to issue commands to the database
    * Create a table
    * Retrieve some data
    * Insert data
    * Delete data
'''

#Web Applications w/ Databases
'''
* Application Developer - Builds the logic for the application, the look and feel of the application - monitors the application for problems
* Database Administrator - Monitors and adjusts the database as the program runs in production
* Often both people participate in the building of the "Data Model"
'''

#Database Model
'''
* A database model or database schema is the structure or format of a database, described in a formal language supported by the database management system. In othe words, a "database model" is the application of a data
model when used in conjunction with a database management system.

#Common Database Systems
* Three major Database Management Systems in wide use
    * Oracle - Large, commercial, enterprise-scale, very very tweakable
    * MySql - Simpler but very fast and scalable - commercial open source
    * SqlServer - Very nice - from Microsoft (also Access)
* Many other smaller projects, free and open source
    *HSQL, SQLite, Postress...
'''

#SQL Commands Examples:
'''
* Single Table SQL:
CREATE TABLE "Users" ("name" TEXT, "email" TEXT)

* SQL: Insert -> The Insert statement inserts a row into a table
INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu')

* SQL: Delete -> Deletes a row in a table based on a selection criteria
DELETE FROM Users WHERE email='ted@umich.edu'

* SQL Update -> Allows the updating of a field with a where clause
UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'

* Retrieving Records: Select -> The select statement retrieves a group of records - you can either retrieve all the records or a subset of the records with a WHERE clause
SELECT * FROM Users
SELECT * FROM Users WHERE email='csev@umich.edu'

* Sorting with ORDER BY -> You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name DESC
'''

#Code example
# import sqlite3

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')

# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (email, count)
#                 VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
#                     (email,))
#     conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()
