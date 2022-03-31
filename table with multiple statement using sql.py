import sqlite3
conn = sqlite3.connect('aswinraj.db')
print ("Opened database successfully");

import sqlite3

conn = sqlite3.connect('aswinraj.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE COMPANY
         (ROLL INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         SUBJECT        CHAR(50),
         MARKS         REAL);''')
print ("Table created successfully");

import sqlite3

conn = sqlite3.connect('aswinraj.db')
print ("Opened database successfully");

conn.execute("INSERT INTO COMPANY (ROLL,NAME,SUBJECT,MARKS) \
      VALUES (101, 'MUTHURAJ', 'MATHS', 175 )");

conn.execute("INSERT INTO COMPANY (ROLL,NAME,SUBJECT,MARKS)) \
      VALUES (201, 'JOY', 'SCIENCE', 125 )");

conn.execute("INSERT INTO COMPANY (ROLL,NAME,SUBJECT,MARKS)) \
      VALUES (301, 'PRAKASHRAJ', ECONOMICS , 150 )");

import sqlite3

conn = sqlite3.connect('aswinraj.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ROLL = ", row[0])
   print ("NAME = ", row[1])
   print ("SUBJECT = ", row[2])
   print ("MARKS = ", row[3], "\n")

print ("Operation done successfully");
conn.close()