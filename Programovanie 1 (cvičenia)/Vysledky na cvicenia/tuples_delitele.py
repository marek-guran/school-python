#Program na vypis delitelov cisla
x=int(input('Zadaj cislo'))
delitel=()
for i in range(1,x+1):
    if x % i == 0:
        delitel = delitel + (i,)
print('Delitele cisla ',x, ' su ', delitel)        
    
