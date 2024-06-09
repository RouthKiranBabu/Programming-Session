import sqlite3
from empmodule import Employee

#Using memory needs to create the table again and again
conn = sqlite3.connect(':memory:')

c = conn.cursor()

#Need to create the table again and again for memory
c.execute("""CREATE TABLE employees(
          first text,
          last text,
          pay integer
)""")

c = conn.cursor()

emp1 = Employee("Routh", "Kiran", 12000)
emp2 = Employee("rout", "kiran", 2400)

c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp1.first, emp1.last, emp1.pay))
conn.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp2.first, 'last': emp2.last, 'pay': emp2.pay})
conn.commit()

#Different ways to get the data from database
c.execute("SELECT * FROM employees WHERE last = ?", ("Kiran", ))
print(c.fetchall())
c.execute("SELECT * FROM employees WHERE last = :last", {'last': 'kiran'})
print(c.fetchall())
#Output
#[('Routh', 'Kiran', 12000)]
#[('rout', 'kiran', 2400)]

conn.commit()
conn.close()