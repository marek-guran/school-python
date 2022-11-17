#Program na najdenie a vymenenie minima/maxima
def matica_nacitaj():
    riadok=0
    mat=[]
    while riadok>-1:
        riadok=riadok+1
        hlaska='Riadok '+str(riadok)+' '
        ret=input(hlaska)
        p=[]
        p=ret.split(' ')
        if len(p)==1 and p[0]=='0':
            break
        else:
            for i in range(len(p)):
                p[i]=int(p[i])
        mat.append(p)
    return mat

def matica_vypis(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print('{:4}'.format(m[i][j]), end=' ')
        print()
    return None
        
def matica_minmax(m):
    min=m[0][0]
    max=m[0][0]
    imin=jmin=imax=jmax=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>max:
                max=m[i][j]
                imin=i
                jmin=j
            if m[i][j]<min:
                min=m[i][j]
                imin=i
                jmin=j
    m[imin][jmin],m[imax][jmax]=m[imax][jmax],m[imin][jmin]
    return m

#HLAVNY PROGRAM 
a=matica_nacitaj()
print('Originalna matica:')
matica_vypis(a)
b=[]
b=matica_minmax(a)
print('Vymenena matica:')
matica_vypis(b)
        
