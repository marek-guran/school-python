pt=0
pr=0
ps=0
pp=0
a=int(input('Zadajte cislo: '))
b=int(input('Zadajte cislo: '))
c=int(input('Zadajte cislo: '))
while (a!=0) and (b!=0) and (c!=0):
    if a+b>c and a+c>b and b+c>a:
        pt+=1
        if (a==b) and (a==c):
            ps+=1
        if (a==b and a!=c) or (a==c!=b) or (b==c!=a):
            pr+=1
        if (a**2 + b**2 == c**2) or (b**2+c**2==a**2) or (c**2+a**2==b**2):
            pp+=1
    a=int(input('Zadajte cislo: '))
    b=int(input('Zadajte cislo: '))
    c=int(input('Zadajte cislo: '))
    
print("v postupnosti je: ",pt," trojuholnikov ",ps," rovnostrannych",pp,"pravouhlych")            
            
        
