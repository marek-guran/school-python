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

def ulozit():
    subor=input('Ako sa bude volať súbor?...')
    f=open(subor, "w+")
def nacitat_subor():
    subor=input('Zadajte názov súboru:')
    f=open(subor,"r")
    print(subor)
def zatvorit():
    f.close(subor)
    print('Súbor bol zatvorený')

volba=0
a=[]
b=[]
c=[]
while True:
    print('=============================================')
    print('=            Program na triedenie           =')
    print('=============================================')
    print('= Pre načítanie 2 polí stlačte............1 =')
    print('= Pre minsort stlačte.....................2 =')
    print('= Pre insert sort stlačte.................3 =')
    print('= Pre zlievanie(mergesort) stlačte........4 =')
    print('= Ak chcete uložiť, stlačte...............5 =')
    print('= Ak chcete načítať zo súboru, stlačte....6 =')
    print('= Ak chcete zatvoriť súbor, stlačte.......7 =')
    print('= Pre ukončenie programu stlačte..........0 =')
    print('=============================================')
    volba=int(input('Vaša voľba: '))
    if volba == 1:
        nacitanie(a)
        nacitanie(b)
    elif volba == 2:
        a=minsort(a)
        print('Utriedene 1.pole: ')
        print(*a)
        
        b=minsort(b)
        print('Utriedene 2.pole: ')
        print(*b)
    elif volba == 3:
        a=insertsort(a)
        print('Utriedené 2.pole: ')
        print(*a)
        
        b=insertsort(b)
        print('Utriedené 2.pole: ')
        print(*b)
    elif volba == 4:
        c=zlievanie(a,b)
        print('Utriedené pole zlievaním: ')
        for i in range(len(c)):
            print(c[i],end=' ')
        print()    
    elif volba == 5:
        ulozit()
    elif volba == 6:
        nacitat_subor()
    elif volba == 7:
        zatvorit()
    elif volba == 0:
        print('Program bol úspešne ukončený!')
        break
    else:
        print('Zadaný príkaz sa nenašiel, pre bližšie informácie: Chyba 404')
        
