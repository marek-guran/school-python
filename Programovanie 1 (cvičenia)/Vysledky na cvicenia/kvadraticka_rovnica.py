#PROGRAM na vypocet korenov kvadratickej rovnice
a=int(input('Zadaj prvy koeficient '))
b=int(input('Zadaj druhy koeficient '))
c=int(input('Zadaj treti koeficient '))
d=b*b-4*a*c
if d<0:
    print('Rovnica nema korene ')
elif d==0:
    print('Rovnica ma jeden koren ',-b/(2*a))
else:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
    print('Rovnica ma korene ',x1,',',x2)
