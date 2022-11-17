#program na zistenie poctu maxim v ppostupnosti
n=int(input('Zadajte cele cislo:'))
pm=1
if n==0:
    print('Koniec programu')
else:
    maximum=n
    while n!=0:
        n=int(input('Zadajte cele cislo:'))
        if n!=0:
            if maximum==n:
                pm=pm+1
            if maximum<n:
                maximum=n
                pm=1
print('Pocet maxim ',maximum,'je',pm)
