#program na vypocet vyrazu
x=int(input('Zadajte hodnotu x: '))
y=int(input('Zadajte hodnotu y: '))
if x==0 or y==0:
    print('Vyraz nema riesenie')
else:
    v=(25-y)/(x*y)
    print('Vyraz ma riesenie ',v)
