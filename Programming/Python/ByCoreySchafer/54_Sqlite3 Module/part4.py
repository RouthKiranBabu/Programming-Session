import sqlite3
from empmodule import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

emp1 = Employee("Routh", "Kiran", 12000)
emp2 = Employee("rout", "kiran", 2400)

#For inserting values in different form 
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp1.first, emp1.last, emp1.pay))
conn.commit()

#After adding values using execute as just above and below we can above and below code and search the value as per last
#For inserting values in different form 
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp2.first, 'last': emp2.last, 'pay': emp2.pay})
conn.commit()

#To search values
c.execute("SELECT * FROM employees WHERE last = 'kiran'")

#To print one value of table
print(c.fetchone())
#Output
#('Routh', 'Kiran', 50000)

#To print all the values present in the table
print(c.fetchall())
#Output
#[('Routh', 'Kiran', 50000), ('Rout', 'Kiran', 50000), ('Rout', 'Kiran', 5000), ('Rout', 'Kiran', 5000), ('Rout', 'Kiran', 5000), ('Rout', 'Kiran', 5000)]

conn.commit()
conn.close()