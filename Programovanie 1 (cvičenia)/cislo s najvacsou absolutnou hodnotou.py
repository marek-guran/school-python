#najvacsia absolutna hodnota, zistenie maxima absolutnych hodnot
n=int(input('Zadajte cislo:'))
maxim=0

for i in range (n):
    x=int(input('Zadajte pocet celych cisel:'))
    if abs(x)>maxim:
        maxim=abs(x)
    else:
        pass
print('Cislo s najvacsou absolutnou hodnotou je:',maxim)
