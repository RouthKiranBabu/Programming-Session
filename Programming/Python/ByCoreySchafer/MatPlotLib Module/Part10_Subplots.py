import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
'''
data = pd.read_csv('Part10data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
plt.plot(ages, py_salaries, label='Python')
plt.plot(ages, js_salaries, label='JavaScript')
plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
plt.legend()
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()'''
'''
data = pd.read_csv('Part10data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
fig, ax = plt.subplots()
ax.plot(ages, py_salaries, label='Python')
ax.plot(ages, js_salaries, label='JavaScript')
ax.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
ax.legend()
ax.set_title('Median Salary (USD) by Age')
ax.set_xlabel('Ages')
ax.set_ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()'''
'''
fig, ax = plt.subplots()
print(ax)'''
'''
fig, ax = plt.subplots(nrows = 2, ncols = 1)
print(ax)'''
'''
fig, ax = plt.subplots(nrows = 2, ncols = 2)
print(ax)'''
'''
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)
print(ax1)
print(ax2)'''
'''
data = pd.read_csv('Part10data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
#ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')
ax2.legend()
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()'''
'''
data = pd.read_csv('Part10data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True)
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')
ax2.legend()
#ax2.set_title('Median Salary (US1D) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()'''

data = pd.read_csv('Part10data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')
ax2.legend()
#ax2.set_title('Median Salary (US1D) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()
fig1.savefig('Part10Fig1.png')
fig2.savefig('Part10Fig2.png')