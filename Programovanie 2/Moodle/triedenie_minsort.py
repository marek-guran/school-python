#Program na triedenie - Minsort
def min_sort(b):
    for i in range(len(b)-1):
        minimum=i
        for j in range(i+1,len(b)):
            if b[minimum]>b[j]:
                minimum=j
        b[i],b[minimum]=b[minimum],b[i]
    return b    

#-------------Hlavny program-----------------
a=[]
n=int(input('Zadaj rozmer pola '))
for i in range(n):
    x=int(input('Prvok['+str(i)+']'))
    a.append(x)
c=min_sort(a)
print()
print('Utriedene pole: ')
for i in range(n):
    print(c[i],end=',')
