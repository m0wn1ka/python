import sqlite3
conn = sqlite3.connect('test.db')

print("conncectiondonne")

conn.execute('''CREATE TABLE  if not exists COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("table compan ycreated")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
print("insertion done")
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
print("Cursorr is ")
for i in cursor:
	print(i)
conn.close()
print("connection closed")
