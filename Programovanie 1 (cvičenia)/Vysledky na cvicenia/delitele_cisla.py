#Program na vypis delitelov cisla
def delitele_cisla(x):
    delitel=()
    for i in range(1,x+1):
        if x%i ==0:
            delitel=delitel+(i,)
    return delitel

xx=int(input('Zadajte cislo '))
p=delitele_cisla(xx)
print(p)
        
