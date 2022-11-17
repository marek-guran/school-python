#Program na trojrozmerne pole
def vytvor_kocku():
    n1=int(input('Zadajte 1.rozmer pola '))
    n2=int(input('Zadajte 2.rozmer pola '))
    n3=int(input('Zadajte 3.rozmer pola '))
    kocka=[]
    for i in range(n1):
        matica=[]
        for j in range(n2):
            x=input('Riadok '+str(i)+' pola ')
            p=x.split()
            vektor=[]
            for k in range(n3):
                vektor.append(int(p[k]))
            matica.append(vektor)
        kocka.append(matica)    
    return kocka

def vypis_kocku(kocka):
    print('Vypis kocky:')
    for i in range(len(kocka)):
        for j in range(len(kocka[i])):
            for k in range(len(kocka[i][j])):
                print(kocka[i][j][k],end=' ')
            print()

#----------------------HLAVNY PROGRAM----------
k=[]
k=vytvor_kocku()
vypis_kocku(k)
        
