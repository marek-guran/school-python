#Program na pracu s maticami
def matica_nacitaj():
    mat=[]
    rozmer=int(input('Zadaj rozmer matice '))
    for i in range(rozmer):
        pom=[]
        for j in range(rozmer):
            ret='M['+str(i)+','+str(j)+'] '
            x=int(input(ret))
            pom.append(x)
        mat.append(pom)    
    return mat

def matica_vypis(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if not(i==0 or j==0 or i==len(m)-1 or j==len(m)-1):
                print(0, end=' ')
            else:    
                print(mat[i][j], end=' ')
        print()
    print()    
    return None
def matica_zrkadlo(mat):
    z=[]
    for i in range(0,len(mat)):
        pom=[]
        for j in range(len(mat)-1,-1,-1):
            pom.append(mat[i][j])
        z.append(pom)
    return z   

    
m=[]
mz=[]
m=matica_nacitaj()
print('Vypis matice ')
matica_vypis(m)
print('Prvky havnej diagonaly ')
for i in range(len(m)):
    print(m[i][i], end=' ')
print()    
print('Prvky vedlajsej diagonaly ')
for i in range(len(m)):
    print(m[i][len(m)-i-1], end=' ')
mz=matica_zrkadlo(m)
print()
print('Zrkadlovy vypis matice ')
matica_vypis(mz)
