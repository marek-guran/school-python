#zistenie ci ide o rovnostranny, rovno ramenny alebo pravouhly trojuholnik
a=int (input('Zadajte stranu a: '))
b=int (input('Zadajte stranu b: '))
c=int (input('Zadajte stranu c: '))
if (a+b>c) and (a+c>b) and (b+c>a):
    print ('Strany tvoria trojuholnik')
    if  (c*c==a*a+b*b) or (a*a==c*c+b*b) or (b*b==a*a+c*c):
        print('Trojuholnik je pravouhly')
    if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        print('Trojuholnik je rovnoramenny')
    if (a==b==c):
        print('Trojuholnik je rovnostranny')
else:
    print('Strany netvoria trojuholnik')
