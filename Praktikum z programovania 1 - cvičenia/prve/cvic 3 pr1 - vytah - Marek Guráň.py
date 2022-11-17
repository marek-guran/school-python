#pretazenie vytahu, Marek Guráň

a=int(input('Mnozstvo balikov:'))
b=int(input('Vaha jedneho balika v kg:'))
v=a*b
if v<400:
    print('Vaha neprekrocila nosnost vytahu')
elif v>400:
    print('Pretazenie vytahu, vyberte posledny balik')
