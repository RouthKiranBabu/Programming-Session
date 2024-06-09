from collections import namedtuple
Color=namedtuple('Color',['red','green','blue'])
color=Color(55,155,255)
print(color[1])
print(color.red)
print(color._fields)
white=Color(1,2,3)
print(white.red,white.green,white.blue)

