import sqlite3

#Just run this below code which creates the employee.db file at the current directory
conn = sqlite3.connect('employee.db')

c = conn.cursor()

#https://www.sqlite.org/datatype3.html
c.execute("""CREATE TABLE employees(
          first text,
          last text,
          pay integer
)""")

conn.commit()

#Run this program once and if you do run this program again the you get the error
#    c.execute("""CREATE TABLE employees(
#sqlite3.OperationalError: table employees already exists
conn.close()