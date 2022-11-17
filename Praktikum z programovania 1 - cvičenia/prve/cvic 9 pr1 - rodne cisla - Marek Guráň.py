#cvicenie 9, priklad 1, Marek Guráň
print('Prosím zadajte vaše rodné číslo s vynechaním čísiel za lomítkom')
id1 = input('Vložte vaše rodné číslo:')
print('Prosím zadajte čísla za lomítkom')
id2 = input('Vložte čísla za lomítkom /:')

idn=(id1+str('/')+id2)
print(idn)

kid1=len(id1)
if kid1 is kid1>6 or kid1<6:
    print('Zlý počet čísel v rodnom čísle')

kid2=len(id2)
if kid2 is kid2>4 or kid2<4:
    print('Zlý počet čísel v rodnom čísle za lomítkom')

print('Ak sa jedná o muža, zadajte: muz()')
print('Ak sa jedná o ženu, zadajte: zena()')

def muz():
    rok=idn[:2]
    den=idn[4:6]
    mesiac=idn[2:4]
    print('Váš dátum narodenia je:',den+str('.')+mesiac+str('.19')+rok)

def zena():
    rok=idn[:2]
    den=idn[4:6]
    mesiac=idn[2:4]
    mesiac=str(int(mesiac)-50)
    print('Váš dátum narodenia je:',den+str('.')+mesiac+str('.19')+rok)

