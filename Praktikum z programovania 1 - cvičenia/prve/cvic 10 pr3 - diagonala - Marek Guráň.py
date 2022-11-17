#Cvicenie 10, priklad 3, Marek Guráň
mat=[]
def zadanie_matice (mat):
    n=int(input("Zadajte rozmer matice: "))
    mat=[]
    for i in range(n):
        p=[]
        hlaska= "Zadajte " +str(i+1)+ " riadok: "
        a=input(hlaska)
        p=a.split()
        temp=[]
        for k in range (len (p)):
            temp.append(int(p[k]))
        mat.append (temp)
    return mat

def vypis_diagonaly(mat):
    print("Výpis diagonály")
    for i in range(len(mat)):
        print(mat[i][i], end=' ')
    print()
    return mat

mat=zadanie_matice(mat)
#zadanie_matice(mat)
vypis_diagonaly(mat)
