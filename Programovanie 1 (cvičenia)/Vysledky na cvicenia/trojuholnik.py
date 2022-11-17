#Program na zistenie trojuholnika

a=int(input('zadajte stranu trojuholnika '))
b=int(input('zadajte stranu trojuholnika '))
c=int(input('zadajte stranu trojuholnika '))

if  not((a+b>c) and (b+c>a) and (a+c>b)):
    print('Strany netvoria trojuholnik!')
else:    
    print('strany tvoria trojuholnik')
    if (a**2 + b**2 == c**2) or (c**2 + b**2 == a**2) or (a**2 + c**2 == b**2):
        print('trojuholnik je pravouhly')

    if (a==b!=c) or (b==c!=a) or (c==a!=b):
        print ( 'trojuholnik je rovnorameny')
    if (a==b==c):
        print ( 'trojuholnik je rovnostrany')
    
    
