#Program na funkcie, ktora precita 3 dvojice cisel a pomocou funkcie ich vymeni
def vymena(x,y):
    c=x
    x=y
    y=c
    return x,',',y
a=b=1    
while (a!=0 and b!=0):
    a=int(input('Zadaj 1.cislo '))
    b=int(input('Zadaj 2.cislo '))
    if (a!=0 and b!=0):
        print('Vymenene cisla su: ',vymena(a,b))
        
