import sqlite3
from empmodule import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

emp1 = Employee("Routh", "Kiran", 12000)
emp2 = Employee("rout", "kiran", 2400)

#Different ways to get the data from database
c.execute("SELECT * FROM employees WHERE last = ?", ("Kiran", ))
print(c.fetchall())
#Output
#[('Routh', 'Kiran', 50000), ('Routh', 'Kiran', 50000), ('Rout', 'Kiran', 50000), 
# ('Rout', 'Kiran', 5000), ('Rout', 'Kiran', 5000), ('Rout', 'Kiran', 5000), 
# ('Rout', 'Kiran', 5000), ('Rout', 'Kiran', 5000), ('Routh', 'Kiran', 12000), ('Routh', 'Kiran', 12000), ('Routh', 'Kiran', 12000), ('Routh', 'Kiran', 12000), ('Routh', 'Kiran', 12000), ('Routh', 'Kiran', 12000), ('Routh', 'Kiran', 12000)]

c.execute("SELECT * FROM employees WHERE last = :last", {'last': 'kiran'})
print(c.fetchall())
#Output
#[('rout', 'kiran', 12000), ('rout', 'kiran', 12000), ('rout', 'kiran', 12000), 
#('rout', 'kiran', 12000), ('rout', 'kiran', 12000), ('rout', 'kiran', 12000), 
#('rout', 'kiran', 2400)]

conn.commit()
conn.close()