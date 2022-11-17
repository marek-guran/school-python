#PROGRAM na vytvorenie vektora riadkovych suctov z obdlznikovej matice
def matica_vstup():
    m=[]
    print('Zadajte prvky po riadkoch, koniec=Enter')
    while 1==1:
        ret=input()
        if len(ret)==0 and ret=='':
            break
        temp=[]
        temp=ret.split(' ')
        for i in range(len(temp)):
            temp[i]=int(temp[i])
        m.append(temp)
    return m

def matica_vypis(mat):
    print('Vypis matice:')
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
        print()
    return None

def matica_vektor_suctov(mat):
    v=[]
    for i in range(len(mat)):
        v.insert(i+1,0)
        for j in range(len(mat[i])):
            v[i]=v[i]+mat[i][j]
    return v
        
#MAIN PROGRAM
mat=matica_vstup()
matica_vypis(mat)
vektor=matica_vektor_suctov(mat)
print('Vektor riadkovych suctov:')
for i in range(len(mat)):
    print(vektor[i])
