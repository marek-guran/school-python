#Program na zistenie maxima z celych cisel
m=int(input('Zadajte 1.cislo'))
for i in range (1,10):
    hlaska='Zadajte '+str(i+1)+'.cislo'
    x=int(input(hlaska))
    if x>m:
        m=x
    else:
        pass
print('Najvacsie cislo je ',m)    
