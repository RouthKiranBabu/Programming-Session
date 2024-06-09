from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]     
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
'''
plt.plot(ages_x, py_dev_y, color = '#5a7d9a', linewidth = 3, label = 'Python Devs')
plt.plot(ages_x, js_dev_y, color = '#adad3b', linewidth = 3, label = 'Java Script')
plt.plot(ages_x, dev_y, color = '#444444', linestyle = '--', label = 'All Devs')
plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('newplotxkcd.png')
plt.show()'''
'''
plt.plot(ages_x, js_dev_y, color = '#e5ae38', linewidth = 3, label = 'Java Script')
plt.plot(ages_x, py_dev_y, color = '#008fd5', linestyle = '--', label = 'Python')
plt.bar(ages_x, dev_y, color = '#444444', label = 'All Devs')
plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()'''
'''
plt.bar(ages_x, py_dev_y, color = '#008fd5', linestyle = '--', label = 'Python')
plt.bar(ages_x, js_dev_y, color = '#e5ae38', linewidth = 2, label = 'Java Script')
plt.bar(ages_x, dev_y, color = '#444444', label = 'All Devs')
plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()'''
'''
import numpy as np
x_indexes, width = np.arange(len(ages_x)), 0.25
plt.bar(x_indexes - width, py_dev_y, width = width, color = '#008fd5', label = 'Python')
plt.bar(x_indexes, js_dev_y, width = width, color = '#e5ae38', label = 'Java Script')
plt.bar(x_indexes + width, dev_y, width = width, color = '#444444', label = 'All Devs')
plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.xticks(ticks = x_indexes, labels = ages_x)
plt.grid()
plt.tight_layout()
plt.show()'''
'''
import csv
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	row = next(csv_reader)
	print(row)
	print(row['LanguagesWorkedWith'])
	print(row['LanguagesWorkedWith'].split(';'))'''
'''
from collections import Counter
c = Counter(['Python', 'JavaScript'])
print(c)
c.update(['C++', 'Python'])
print(c)
c.update(['C++', 'Python'])
print(c)'''
'''
import csv
from collections import Counter
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	language_counter = Counter()
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))
print(language_counter)
print('\n', language_counter.most_common(15))'''
'''
import csv
from collections import Counter
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	language_counter = Counter()
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))
languages, popularity = [], []
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])
print(languages)
print(popularity)'''
'''
import csv
from collections import Counter
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	language_counter = Counter()
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))
languages, popularity = [], []
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])
plt.bar(languages, popularity)
plt.xlabel('Programming Languages')
plt.ylabel('People Choosen')
plt.title('Most Popular Languages')
plt.tight_layout()
plt.show()'''
'''
import csv
from collections import Counter
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	language_counter = Counter()
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))
languages, popularity = [], []
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])
plt.barh(languages, popularity)
#plt.ylabel('Programming Languages')
plt.xlabel('People Choosen')
plt.title('Most Popular Languages')
plt.tight_layout()
plt.show()'''
'''
import csv
from collections import Counter
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	language_counter = Counter()
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))
languages, popularity = [], []
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])
languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)
#plt.ylabel('Programming Languages')
plt.xlabel('People Choosen')
plt.title('Most Popular Languages')
plt.tight_layout()
plt.show()'''

import csv, pandas as pd
from collections import Counter
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
language_counter = Counter()
languages, popularity = [], []
for response in lang_responses:
	language_counter.update(response.split(';'))
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])
print(languages)
print(popularity)
languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)
#plt.ylabel('Programming Languages')
plt.xlabel('People Choosen')
plt.title('Most Popular Languages')
plt.tight_layout()
plt.show()
print(languages)
print(popularity)