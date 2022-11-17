#Program na zistenie najmensieho cisla z 3 hodnot, Marek Guráň
print ('Do nasledujucich riadkov zapiste cele cisla pre zistenie najmensieho z nich')
a=int (input('Zadajte cele cislo:'))
b=int (input('Zadajte cele cislo:'))
c=int (input('Zadajte cele cislo:'))
min=a
if b<min:
    min=b
if c<min:
    min=c
print ('Najmensie cislo je: ',min)
