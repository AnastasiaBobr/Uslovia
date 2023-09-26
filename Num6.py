import math 
x = int(input('x= '))
y = int(input('y= '))
r = int(input('radiys= '))

if math.sqrt(x**2 + y**2) <= r:
    print('prinadlezhit')
else:
    print('ne prinadlezhit')
