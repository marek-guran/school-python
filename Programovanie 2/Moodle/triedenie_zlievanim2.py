#Program na nacitanie 2 poli, utriedenie zostupne pomocou minsort a zostupne pomocou insertsort
#nakoniec zliatie zostupne do jedneho utriedeneho pola
def nacitanie(p):
    n=int(input('Zadajte pocet prvkov pola: '))
    for i in range(n):
        x=int(input('Prvok['+str(i)+']'))
        p.append(x)

#Funkcia na utriedenie pola metodou triedenia minsort
def minsort(p):
    for i in range(len(p)-1):
        minimum=i
        for j in range(i+1,len(p)):
            if p[j]>p[minimum]:
                minimum=j
        if i!=minimum :
            p[i],p[minimum]=p[minimum],p[i]
    return p       

#Funkcia na utriedenie pola metodou triedenia insertsort
def insertsort(p):
    for i in range (1,len(p)):
        x=p[i]
        j=i-1
        while j>=0 and p[j]<x:
            p[j+1]=p[j]
            j=j-1
        p[j+1]=x    
    return p            

#Funkcia na zliatie pola pomocou metody mergesort
def zlievanie(c,d):
    e=[]
    i=j=k=0
    while (i<len(c)) and (j<len(d)):
        if c[i]>d[j]:
            e.insert(k,c[i])
            k+=1
            i+=1
        else:
            e.insert(k,d[j])
            k+=1
            j+=1
    while (i<len(c)):
        e.insert(k,c[i])
        k+=1
        i+=1
    while (j<len(d)):
        e.insert(k,d[j])
        k+=1
        j+=1
    return e    
            
# Hlavny program
a=[]
b=[]
c=[]
nacitanie(a)
nacitanie(b)
a=minsort(a)
print('Utriedene 1.pole: ')
print(*a)
b=insertsort(b)
print('Utriedene 2.pole: ')
print(*b)
c=zlievanie(a,b)
print('Utriedene pole zlievanim: ')
for i in range(len(c)):
    print(c[i],end=' ')
print()    
