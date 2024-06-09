import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('Part5data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')
#plt.fill_between(ages, py_salaries)
#plt.fill_between(ages, py_salaries, alpha = 0.25)
overall_median = 57287
#plt.fill_between(ages, py_salaries, overall_median, alpha = 0.25)
'''
plt.fill_between(ages, py_salaries, overall_median, 
	where = (py_salaries > overall_median), alpha = 0.25)'''
'''
plt.fill_between(ages, py_salaries, overall_median, 
	where = (py_salaries > overall_median), interpolate = True, alpha = 0.25)
plt.fill_between(ages, py_salaries, overall_median, 
	where = (py_salaries <= overall_median), interpolate = True, alpha = 0.25)'''
'''
plt.fill_between(ages, py_salaries, overall_median, 
	where = (py_salaries > overall_median), interpolate = True, alpha = 0.25)
plt.fill_between(ages, py_salaries, overall_median, 
	where = (py_salaries <= overall_median), interpolate = True, color = 'yellow', alpha = 0.25)'''

plt.fill_between(ages, py_salaries, dev_salaries, 
	where = (py_salaries > dev_salaries), interpolate = True, alpha = 0.25, label = 'Above Avg')
plt.fill_between(ages, py_salaries, dev_salaries, 
	where = (py_salaries <= dev_salaries), interpolate = True, color = 'red', alpha = 0.25, label = 'Below Avg')
plt.legend()
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()