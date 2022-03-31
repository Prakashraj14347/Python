import sqlite3

conn = sqlite3.connect('prakashrajaswin.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         City        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully")


import sqlite3

conn = sqlite3.connect('prakashrajaswin.db')
print("Opened database successfully")


conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,CITY,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,CITY,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,CITY,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,CITY,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
conn.commit()

cursor = conn.execute("SELECT id, name, CITY, salary from COMPANY")
for row in cursor:
    print ("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("CITY = ", row[2])
    print ("SALARY = ", row[3], "\n")
    
   
print ("Operation done successfully")