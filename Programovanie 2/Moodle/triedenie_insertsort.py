#Program na triedenie - Insertsort
def insert_sort(b):
    print(*b)
    for i in range(1,len(b)):
        x=b[i]
        j=i-1        #diera v triedeni
        while j>=0 and b[j]>x :
            b[j+1]=b[j]
            j=j-1
        b[j+1]=x
        print(*b[:i+1], '|', *b[i+1:])
    return b

#------------Hlavny program-----------
a=[]
n=int(input('Zadajte rozmer pola: '))
for i in range(n):
    x=int(input('Prvok['+str(i)+']'))
    a.append(x)
c=insert_sort(a)
print()
print('Utriedene pole: ')
print(c)
