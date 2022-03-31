import sqlite3

conn = sqlite3.connect('testaswinraj.db')

print ("Opened database successfully");

#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('testaswinraj.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE COMPANY
         (ROLL INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         SUBJECT        CHAR(50),
         MARKS         REAL);''')
print ("Table created successfully");

conn.close()

#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('testaswinraj.db')
print ("Opened database successfully");

conn.execute("INSERT INTO COMPANY (ROLL,NAME,AGE,SUBJECT,MARKS) \
      VALUES (101, 'PRAKASHRAJ', 38, 'SCIENCE', 75 )");

conn.execute("INSERT INTO COMPANY (ROLL,NAME,AGE,SUBJECT,MARKS) \
      VALUES (202, 'MUTHURAJ', 22, 'MATHS', 95 )");

conn.execute("INSERT INTO COMPANY (ROLL,NAME,AGE,SUBJECT,MARKS) \
      VALUES (303, 'SMITH', 21, 'ECONOMICS', 85 )");

conn.execute("INSERT INTO COMPANY (ROLL,NAME,AGE,SUBJECT,MARKS) \
      VALUES (404, 'JOY', 32, 'SOCIAL SCIENCE', 65 )");

conn.commit()
print ("Records created successfully");
conn.close()



import sqlite3

conn = sqlite3.connect('testaswinraj.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT roll, name, age, subject,marks from COMPANY")
for row in cursor:
   print ("ROLL = ", row[0])
   print ("NAME = ", row[1])
   print ("AGE = ", row[2])
   print ("SUBJECT = ", row[3])
   print ("MARKS = ", row[4], "\n")

print ("Operation done successfully");
conn.close()