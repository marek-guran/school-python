#zistenie kolko je pravouhlych,rovnostrannych a rovnorammenych trojuholnikov
s=input('Zadajte 3 cisla:')
p=s.find(' ')
a=int(s[:p])
s=s[p+1:]
p=s.find(' ')
b=int(s[:p])
s=s[p+1:]
c=int(s)
pr=ps=pp=0

while not (a==0 and b==0 and c==0):
    if a+b>c and b+c>a and c+a>b:
        if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
            pp=pp+1
        if a==b==c:
            ps=ps+1
        if a==b and a!=c or (a==c and b!=c) or (b==c and a!=c):
            pp=pp+1
    s=input('Zadajte 3 cisla:')

    s=input('Zadajte 3 cisla:')
    p=s.find(' ')
    a=int(s[:p])
    s=s[p+1:]
    p=s.find(' ')
    b=int(s[:p])
    s=s[p+1:]
    c=int(s)

print('Pocet rovnoramennych je:',pr)
print('Pocet rovnostrannych je:',ps)
print('Pocet pravouhlych je:',pp)
