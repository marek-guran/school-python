#Program na scitanie, odcitanie, nasobenie matic
def vypis(a):
    for i in range (len(a)):
        for j in range (len(a[i])):
            print('{:4d}'.format(a[i][j]), end=' ')
        print()

def nacitaj():
    a=[]
    s=input('Zadajte názov súboru:')
    f=open(s, 'r')
    for riadok in f:
        p=riadok.split()
        for i in range (len(p)):
            p[i]=int(p[i])
        a.append(p)
    f.close()
    return a

def scitanie(a,b):
    c=[]
    for i in range (len(a)):
        temp=[]
        for j in range (len(a[i])):
            temp.append(a[i][j]+b[i][j])
        c.append(temp)
    return c

def odcitanie(a,b):
    d=[]
    for i in range (len(a)):
        temp=[]
        for j in range (len(a[i])):
            temp.append(a[i][j]-b[i][j])
        d.append(temp)
    return d

def sucin(a,b):
    c=[]
    for i in range (len(a)):
        temp=[]
        for j in range (len(b[0])):
            temp.append(0)
        c.append(temp)
        
    for i in range (len(a)):
        for j in range (len(b[0])):
            for k in range (len(b)):
                c[i][j]=a[i][k]*b[k][j]+c[i][j]
    return c



#Hlavny program
m1=[]
m2=[]
m3=[]

while True:
    print()
    print('Nacitanie matic...1')
    print('Vypis matic.......2')
    print('Sucet matic.......3')
    print('Odcitanie matic...4')
    print('Sucin matic.......5')
    print('Koniec............0')
    volba=int(input())
    if volba==1:
        m1=nacitaj()
        m2=nacitaj()
    elif volba==2:
        print('Vypis prvej matice:')
        vypis(m1)
        print('Vypis druhej matice:')
        vypis(m2)
    elif volba==3:
        m3=scitanie(m1,m2)
        print('VYsledok suctu 2 matic je:')
        vypis(m3)
    elif volba==4:
        m3=odcitanie(m1,m2)
        print('Vysledok odcitania matic je:')
        vypis(m3)
    elif volba==5:
        m3=sucin(m1,m2)
        print('Vysledok sucinu matic je:')
        vypis(m3)
    else:
        print('Koniec programu')
        break
