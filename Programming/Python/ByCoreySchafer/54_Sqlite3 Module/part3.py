import sqlite3

#Just run this below code which creates the employee.db file at the current directory
conn = sqlite3.connect('employee.db')

c = conn.cursor()

#Comment the below no need to twice the table need to adding data to the database
#c.execute("""CREATE TABLE employees(
#          first text,
#          last text,
#          pay integer
#)""")

#Run the below code to insert the data into database for one time so commented
#c.execute("INSERT INTO employees VALUES ('Rout', 'Kiran', 5000)")

#After inserting the values from above which is commented out
c.execute("SELECT * FROM employees WHERE last = 'Kiran'")

#For one
print(c.fetchone())
#Output
#('Routh', 'Kiran', 50000)

#For many
print(c.fetchmany())
#Output
#[('Routh', 'Kiran', 50000)]

#For 5
#c.fetchmany(5)

conn.commit()
conn.close()