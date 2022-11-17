#program na najdenie NSD
def nsd(a,b):
    while(a>0):
        if a>=b:
            a=a%b
        else:
            pom=a
            a=b
            b=pom
            a=a%b
    return b

x=int(input('Zadajte prve cislo '))
y=int(input('Zadajte druhe cislo '))
z=nsd(x,y)
print('NSD je ',z)
