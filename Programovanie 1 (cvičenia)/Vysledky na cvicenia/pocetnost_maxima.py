#Program na hladanie pocetnosti maxima
x=int(input('Zadajte cislo '))
m=x
p=1
if (x!=0):
    while (x!=0):
        x=int(input('Zadajte cislo '))
        if x>m:
            m=x
            p=1
        elif x==m:
            p=p+1
    print('Maximum je ',m,' nachadza sa ',p,'.krat')
else:
    print('Postupnost je prazdna!')
