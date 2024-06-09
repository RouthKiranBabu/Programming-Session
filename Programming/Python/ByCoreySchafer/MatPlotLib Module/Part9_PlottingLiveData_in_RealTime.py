import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')
'''
x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 3, 2, 3, 5]
plt.plot(x_vals, y_vals)
# index = count()
# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0, 5))
plt.tight_layout()
plt.show()
# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']'''
'''
x_vals = []
y_vals = []
index = count()
def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    plt.plot(x_vals, y_vals)
#ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
ani = FuncAnimation(plt.gcf(), animate, interval = 1000, cache_frame_data=False)
plt.tight_layout()
plt.show()'''
'''
x_vals = []
y_vals = []
index = count()
def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_vals, y_vals)
ani = FuncAnimation(plt.gcf(), animate, interval = 1000, cache_frame_data=False)
plt.tight_layout()
plt.show()'''
'''
import csv
import random
import time
x_value = 0
total_1 = 1000
total_2 = 1000
fieldnames = ["x_value", "total_1", "total_2"]
with open('Part9data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }
        csv_writer.writerow(info)
        print(x_value, total_1, total_2)
        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)
    time.sleep(1)'''
#Run the file 'Part9_RunAtCommandAndthenrunPlottingLiveData.py' and then run the below
#section
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
x_vals = []
y_vals = []
index = count()
def animate(i):
    data = pd.read_csv('Part9datagen.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    plt.cla()
    plt.plot(x, y1, label = 'Channel 1')
    plt.plot(x, y2, label = 'Channel 2')
    plt.legend(loc = 'upper left')
    plt.tight_layout()
ani = FuncAnimation(plt.gcf(), animate, interval = 1000, cache_frame_data=False)
plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']