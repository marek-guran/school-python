#Program ShakeSort(b)
def shakesort(b):
    l=0
    r=len(b)
    k=len(b)
    while l<=r:
        for j in range(r-1,0,-1):
            if b[j-1]>b[j]:
                b[j],b[j-1]=b[j-1],b[j]
                k=j
        l=k+1
        for j in range(l,r):
            if b[j-1]>b[j]:
                b[j],b[j-1]=b[j-1],b[j]
                k=j
        r=k-1
    return b

#Hlavny program
a=[]
n=int(input('Zadajte rozmer pola: '))
for i in range(n):
    x=int(input('a['+str(i)+']'))
    a.append(x)
c=shakesort(a)
print('Utriedene pole: ')
print(c)
        
        
