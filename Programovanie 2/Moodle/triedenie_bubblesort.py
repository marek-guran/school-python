#Program na triedenie prvkov pola - Bubble sort2
def bubble_sort(b):
    for i in range(1,len(b)):
        for j in range(len(b)-1,i-1,-1):
            print(i,',',j)
            if b[j]<b[j-1]:
                b[j],b[j-1]=b[j-1],b[j]
    return b        

a=[]
n=int(input('Zadajte pocet prvkov: '))
for i in range(n):
        x=int(input('Prvok['+str(i)+']'))
        a.append(x)
c=bubble_sort(a)
print()
print('Utriedene pole:')
print(*c)            
        
