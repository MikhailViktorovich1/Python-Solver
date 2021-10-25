'''Dots and Circles'''

import random
import math

filename1 = input("Enter filename with circle center and circle radius data: ")
filename2 = input("Enter filename with dots' coordinates: ")

f1 = open(filename1,'r')
f2 = open(filename2,'r')


'''f1.write(str(random.uniform(-100.0,100.0)) + " " + str(random.uniform(-100.0,100.0)) +'\n' + str(random.randint(1,100)))


for i in range(5):
    f2.write(str(random.uniform(-100.0,100.0)) + " " + str(random.uniform(-100.0,100.0)) +'\n')
'''

x=y=r=0
circle =[]

for i in f1:
    circle.append(i.split())
    
x=float(circle[0][0])
y=float(circle[0][1])
r=int(circle[1][0])

x1=y1=0
dots = []
index=0

for i in f2:
    dots.append(i.split())
    x1 = float(dots[index][0]) 
    y1 = float(dots[index][1])
    
    index+=1

    if (x1 - x)*(x1 - x) + (y1-y)*(y1-y) == r*r:
        print('0')
    elif (x1 - x)*(x1 - x) + (y1-y)*(y1-y) > r*r:
        print('2')
    else:
        print('1')
    
f1.close()
f2.close()
