import pandas as pd
from matplotlib import pyplot as plt

'''
#plt.style.use('seaborn')#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
plt.style.use('fivethirtyeight')
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
#plt.scatter(x, y)
#plt.scatter(x, y, s = 100, c = 'green', marker = 'X')#https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle
#plt.scatter(x, y, s = 100, c = 'green', edgecolor = 'black', linewidth = 2, alpha = 0.5)
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
#plt.scatter(x, y, s = 100, c = colors, edgecolor = 'black', linewidth = 2, alpha = 0.5)
plt.scatter(x, y, s = 100, c = colors, cmap = 'Greens', edgecolor = 'black', linewidth = 2, alpha = 0.5)
cbar = plt.colorbar()
cbar.set_label('Satisfaction')
plt.tight_layout()
plt.show()'''
'''
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
plt.scatter(x, y, s = sizes, c = colors, cmap = 'Greens', edgecolor = 'black', linewidth = 2, alpha = 0.5)
cbar = plt.colorbar()
cbar.set_label('Satisfaction')
plt.tight_layout()
plt.show()'''
'''
data = pd.read_csv('Part7data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
plt.scatter(view_count, likes, edgecolor = 'black', linewidth = 2, alpha = 0.5)
plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.tight_layout()
plt.show()'''

data = pd.read_csv('Part7data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
plt.scatter(view_count, likes, c = ratio, cmap = 'summer', edgecolor = 'black', linewidth = 2, alpha = 0.5)
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')
plt.xscale('log')
plt.yscale('log')
plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.tight_layout()
plt.show()