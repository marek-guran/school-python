#vypocet kvadratickej rovnice, jej realne korene
a=int (input('Zadaj a: '))
b=int (input('Zadaj b: '))
c=int (input('Zadaj c: '))
if a==0:
        print('Rovnica nema realne korene')
elif b*b<4*a*c:
        print('Rovnica nema realne korene')
elif b*b==4*a*c:
        print('Rovnica ma jeden realny koren', -b/(2*a))
else:
    x1=(-b+(b*b-4*a*c)**0.5)/2*a
    x2=(-b-(b*b-4*a*c)**0.5)/2*a
    print('Rovnica ma korene: ',x1,' ',x2)
