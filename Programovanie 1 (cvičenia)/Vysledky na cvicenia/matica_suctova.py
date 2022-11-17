#matica suctovych stlpcov

def zadanie_matice ():
    n=int(input(" Zadajte rozmer matice "))
    mat=[]
    for i in range(n):
        p=[]
        hlaska= " Zadajte" +str(i+1)+ "riadok "
        a=input(hlaska)
        p=a.split()
        temp=[]
        for k in range (len (p)):
            temp.append(int(p[k]))
        mat.append (temp)
    return mat

def vypis_matice(mat):
    print("Výpis matice")
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end=' ')
        print()

def sucet_stlpcov(mat):
    v=[]
    for j in range(len(mat)):
        pom=0
        for i in range(len(mat)):
            pom+=mat[i][j]
        v.append(pom)
    return v

def vymena(mat):
    maxi=mat[0][0]
    mini=mat[0][0]
    imini=0
    jmini=0
    imaxi=0
    jmaxi=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(maxi<mat[i][j]):
                maxi=mat[i][j]
                imaxi=i
                jmaxi=j
            if(mini>mat[i][j]):
                mini=mat[i][j]
                imini=i
                jmini=j
    mat[imini][jmini],mat[imaxi][jmaxi]=mat[imaxi][jmaxi],mat[imini][jmini]

def trans_matica(mat):
    mat2=[]
    for i in range(len(mat)):
        temp=[]
        for j in range(len(mat)):
            if(i==0 or i==len(mat)-1 or j==0 or j==len(mat)-1):
                temp.append(mat[i][j])
            else:
                temp.append(0)
                
        mat2.append(temp)
    return mat2
             
#hlavny program---------
m = []
m = zadanie_matice()
vypis_matice(m)
w=[]
w=sucet_stlpcov (m)
vymena(m)
print(w)
vypis_matice(m)
m2=[]
m2=trans_matica(m)
vypis_matice(m2)





        

            
    
        
        
            
