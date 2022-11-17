#Zostavte program vytvárajúcu pre danú celočíselnú obdĺžnikovú maticu
#rozmeru MxN vytvorí vektor riadkových súčtov ,
#kde i-ty riadok bude súčet prvkov v i-tom riadku.
def matica_nacitaj():
    mat=[]
    riadok=int(input('Zadajte pocet riadkov '))
    stlpec=int(input('Zadajte pocet stlpcov '))
    for i in range(riadok):
        pom=[]
        for j in range(stlpec):
            ret='M['+str(i)+','+str(j)+'] '
            x=int(input(ret))
            pom.append(x)
        mat.insert(i,pom)    
    return mat

def matica_vypis(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
        print()
    print()    
    return None
def vektor_suctov(mat):
    z=[]
    for i in range(0,len(mat)):
        sum=0
        for j in range(len(mat[i])):
            sum=sum+mat[i][j]
        z.insert(i,sum)
    return z   

    
m=[]
mz=[]
m=matica_nacitaj()
print('Vypis matice ')
matica_vypis(m)
mz=vektor_suctov(m)
print('Vektor suctov:')
for i in range(len(mz)):
    print(mz[i])
    
