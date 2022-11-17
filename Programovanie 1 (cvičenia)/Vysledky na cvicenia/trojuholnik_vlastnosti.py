#PROGRAM na zistenie ci strany tvoria trocjuholni
a=int(input('Zadaj stranu '))
b=int(input('Zadaj stranu '))
c=int(input('Zadaj stranu '))
if not((a+b>c) and (a+c>b) and (b+c>a)):
    print('Strany netvoria trojuholnik ')
else:
    print('Strany tvoria trojuholnik ')
    if (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b):
        print('Trojuholnik je pravouhly ' )
    if (a==b) and (a==c):
        print('Trojuholnik je rovnostranny ')
    if (a==b) and (a!=c) or (a==c) and (b!=c) or (b==c) and (a!=b):
        print('Trojuholnik je rovnoramenny ')
    
