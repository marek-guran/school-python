#PROGRAM na nacitanie prvkov vektora
p=[]
n=int (input('Zadaj pocet prvkov pola: '))
for i in range (0,n):
    hlaska='Zadaj '+str(i)+'.cislo '
    x=int(input(hlaska))
    p[i:i]=[x]

print('Vypis prvkov pola: ')    
for i in range(n):
    print(p[i], end=' ')
