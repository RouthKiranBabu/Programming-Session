import sqlite3
from empmodule import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees(
          first text,
          last text,
          pay integer
)""")

#Function for inserting emp into the table
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
 
#Get names if the lastname matches
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""", {"first": emp.first, "last": emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last}) 

c = conn.cursor()

emp1 = Employee("Routh", "Kiran", 12000)
emp2 = Employee("rout", "Kiran", 2400)
emp3 = Employee("R", "iran", 2400)

#Using inserting function
insert_emp(emp1)
insert_emp(emp2)
insert_emp(emp3)

#Function to find row in terms of name
emps = get_emps_by_name("Kiran")
print(emps)
#Output
#[('Routh', 'Kiran', 12000), ('rout', 'Kiran', 2400)]

#Updating the pay
update_pay(emp1, 32000)

#Removing the pay
remove_emp(emp2)

emps = get_emps_by_name("Kiran")
print(emps)
#Output
#[('Routh', 'Kiran', 32000)]

conn.commit()
conn.close()