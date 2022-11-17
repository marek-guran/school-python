#Program na scitanie, odcitanie, nasobenie matic, vypis diagonaly (diskretna matematika)
import numpy
m1=[]
m2=[]
m3=[]
m4=[]
m5=[]

def vypis(a):
    for i in range (len(a)):
        for j in range (len(a[i])):
            print('{:4d}'.format(a[i][j]), end=' ')
        print()

def diagonala():
    print('Vypis diagonaly matice A je: ')
    for i in range(len(m1)):
        print(m1[i][i], end=' ')
    print()
    print('Vypis diagonaly matice B je: ')
    for i in range(len(m2)):
        print(m2[i][i], end=' ')
    print()

def diagonala_c():
    print('Vypis diagonaly matice C je: ')
    for i in range(len(m3)):
        print(m3[i][i], end=' ')
    print()

def nacitaj():
    a=[]
    riadok=int(input('Zadajte pocet riadkov '))
    stlpec=int(input('Zadajte pocet stlpcov '))
    for i in range(riadok):
        pom=[]
        for j in range(stlpec):
            ret='M['+str(i)+','+str(j)+'] '
            x=int(input(ret))
            pom.append(x)
        a.insert(i,pom)    
    return a

def scitanie(m1, m2):
    c=[]
    for i in range (len(m1)):
        temp=[]
        for j in range (len(m1[i])):
            temp.append(m1[i][j]+m2[i][j])
        c.append(temp)
    return c

def odcitanie(m1, m2):
    d=[]
    for i in range (len(m1)):
        temp=[]
        for j in range (len(m1[i])):
            temp.append(m1[i][j]-m2[i][j])
        d.append(temp)
    return d

def sucin(m1,m2):
    c=[]
    for i in range (len(m1)):
        temp=[]
        for j in range (len(m2[0])):
            temp.append(0)
        c.append(temp)
        
    for i in range (len(m1)):
        for j in range (len(m2[0])):
            for k in range (len(m2)):
                c[i][j]=m1[i][k]*m2[k][j]+c[i][j]
    return c



while True:
    print()
    print('Nacitanie matic.........1')
    print('Vypis matic.............2')
    print('Sucet matic.............3')
    print('Odcitanie matic.........4')
    print('Sucin matic.............5')
    print('Diagonala matic A, B....6')
    print('Diagonala matice C......7')
    print('Koniec..................0')
    print()
    volba=int(input('Vasa volba: '))
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
        print('Vysledok suctu 2 matic je:')
        vypis(m3)
    elif volba==4:
        m3=odcitanie(m1,m2)
        print('Vysledok odcitania matic je:')
        vypis(m3)
    elif volba==5:
        m3=sucin(m1,m2)
        print('Vysledok sucinu matic je:')
        vypis(m3)
    elif volba==6:
        m4=diagonala()
    elif volba==7:
        m5=diagonala_c()
    elif volba==0:
        print('Program skoncil')
        break
    else:
        print('Zadali ste zly vstup')
