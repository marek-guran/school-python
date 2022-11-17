#Program - triedenie Quicksort
def quick_sort(b):
    def quick(z,k):
        if z<k:     #rozdelenie na 2 casti
            index=z
            pivot=b[z]
            for i in range(z+1,k+1):
                if b[i]<pivot:
                    index+=1
                    b[index],b[i]=b[i],b[index]
            b[index],b[z]=b[z],b[index]        
            quick(z,index-1)
            quick(index+1,k)
    quick(0,len(b)-1)

import random
#a=[random.randrange(500) for i in range(50)]
n=int(input('Zadajte pocet prvkov pola '))
a=[]
for i in range(n):
    x=int(input('a['+str(i)+'] '))
    a.append(x)
print('Pole pred utriedenim: ')
print(*a)
quick_sort(a)
print('Pole po utriedeni: ')
print(*a)
