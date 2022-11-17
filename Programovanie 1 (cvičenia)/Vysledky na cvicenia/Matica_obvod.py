#Nacitanie matice, ktora vypise prvky z obvodu a na miesto vnutornych da 0
def matica_vstup():
    mat=[]
    print('Zadavajte prvky matice po riadkoch, koniec=Enter')
    riadok=0
    while 1==1:
        ret=input('Zadajte riadok ')
        if len(ret)==0 and ret=='':
            break
        else:
            riadok+=1
        p=[]
        p=ret.split()
        for i in range(len(p)):
            p[i]=int(p[i])
        mat.append(p)
    return mat

def matica_vypis(m):
    print('Vypis matice:')
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end=' ')
        print()
    print()
    return None

def matica_obvod(m):
    b=[]
    for i in range(len(m)):
        temp=[]
        for j in range(len(m[i])):
            if i==0 or i==len(m)-1 or j==0 or j==len(m[i])-1:
                temp.append(m[i][j])
            else:
                temp.append(0)
        b.append(temp)
    return b
        

a=[]
a=matica_vstup()
matica_vypis(a)
b=matica_obvod(a)
matica_vypis(b)                    
                     
                     
        
