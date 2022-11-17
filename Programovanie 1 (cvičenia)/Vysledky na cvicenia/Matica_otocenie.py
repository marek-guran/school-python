#Program na pracu s maticami - otocenie o 90st, vypis vedlajsej diagonaly
def matica_nacitaj():
    mat=[]
    rozmer=int(input('Zadaj rozmer matice '))
    for i in range(rozmer):
        hlaska='Zadajte '+str(i)+'.riadok '
        ret=input(hlaska)
        ret=ret.strip()
        pom=[]
        pom=ret.split()
        for j in range(rozmer):
            pom[i]=int(pom[i])
        mat.append(pom)    
    return mat

def matica_vypis(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print('{:>4}'.format(mat[i][j]), end=' ')
        print()    
    return None

def matica_otoc(mat):
    z=[]
    N=len(mat)-1
    for i in range(0,len(mat)):
        pom=[]
        for j in range(0,len(mat)):
            pom.append(mat[j][N-i])
        z.append(pom)
    return z   

def matica_zrkadlo(mat):
    z=[]
    N=len(mat)-1
    for i in range (0,len(mat)):
        pom=[];
        for j in range(0,len(mat)):
            pom.append(mat[N-j][N-i])
        z.append(pom)
    return z

#===========HLAVNY PROGRAM======================    
m=[]
mz=[]
m=matica_nacitaj()
print('Vypis matice: ')
matica_vypis(m)
print('Prvky hlavnej diagonaly: ')
for i in range(len(m)):
    print(m[i][i], end=' ')
print()    
print('Prvky vedlajsej diagonaly: ')
for i in range(len(m)):
    print(m[i][len(m)-i-1], end=' ')
mz=matica_otoc(m)
print()
print('Vypis otocenej matice: ')
matica_vypis(mz)
mz=[]
mz=matica_zrkadlo(m)
print()
print('Matica preklopena podla hlavnej osi symetrie: ')
matica_vypis(mz)
