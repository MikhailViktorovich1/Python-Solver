''' Circular array '''

n = input("Enter n: ")
n = int(n)

m = input("Enter m: ")
m = int(m)

l=[]
ls=[]
lss=[]

for i in range (1, n+1):
    l.append(i)
       
l = l * m

i=0
a=m-1
x=0

while True:
    ls.append(l[i:m])
    lss.append(ls[x][0])

    i+=a
    m+=a
    x+=1
    
    if ls[-1][a] == ls[0][0]:
        break
    
print(lss)



    



    
    



    
    

    




   


