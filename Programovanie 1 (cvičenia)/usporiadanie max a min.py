#program na najdenie minima a maxima cisla
a=int (input('Zadajte cislo: '))
b=int (input('Zadajte cislo: '))
c=int (input('Zadajte cislo: '))
d=int (input('Zadajte cislo: '))
max=a
if b>max:
    max=b
if c>max:
    max=c
if d>max:
    max=d
print ('Najvecsie cislo je: ',max)

min=a
if b<min:
    min=b
if c<min:
    min=c
if d<min:
    min=d
print ('Najmensie cislo je: ',min)
