''' Array alignment '''

import random

filename = input('Enter your file name ')

f = open(filename, 'r')

"""i=0
while i<10:
    f.write(str(random.randint(0,10)) + '\n')
    i+=1"""

numbers = []

for i in f:
    i = i.strip()
    numbers.append(i)

f.close()       

sum = 0

for i in numbers:
    sum+=(int(i))


avg = round(sum / len(numbers))

count = 0

for i in numbers:
    if int(i) > avg:
        count+=int(i)-avg
    elif int(i) < avg:
        count+=avg-int(i)

print(count)        



