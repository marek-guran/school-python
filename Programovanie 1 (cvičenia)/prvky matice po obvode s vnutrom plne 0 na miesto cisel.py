#Z vytvorenej štvorcovej matice NxN, vypíšte na obrazovku prvky po obvode matice,
#na miesto vnútorných prvkov vypíšte 0.
def matica_vstup():
    mat=[]
    print('Zadávajte prvky po riadkoch, na konci bude samostatná 0')
    riadok=0
    while 1==1:
        ret=input('Zadajte riadok:')
        if len(ret)==1 and ret[0]=='0':
            break
        else:
            p=[]
            p=ret.split(' ')
            for i in range(len(p)):
                p[i]=int(p[i])
            mat.append(p)
    return mat

def matica_vypis(m):
    print('Výpis matice:')
    for i in range (len(m)):
        for j in range(len(m[i])):
            print([i] [j], end=' ')
        print()

def matica_obvod(a):
    b=[]
    for i in range (len(a)):
        temp=[]
        if i==0 or i==len(a[i])-1:
            temp.append(a[i][j])
            for j in range (len(a[i])):
                if i==0 or i==len(m)-1:
                    temp.append(a[i])
                else:
                    if j==0 or j==len(a[i])-1:
                        tmp.append(a[i][j])
                else:
                    tmp.append(0)
            b.append(tmp)
        return b




#main program
m=[]
a=matica_vstup()
matica_vypis(a)
n=matica_obvod(n)
matica_vypis(n)
