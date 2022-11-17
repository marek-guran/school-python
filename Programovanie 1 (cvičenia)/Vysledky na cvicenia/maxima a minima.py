#program na zistenie maxima a minima styroch cisel
a=int(input('zadaj cele cislo '))
b=int(input('zadaj cele cislo '))
c=int(input('zadaj cele cislo' ))
d=int(input('zadaj cele cislo' ))
if (a>=b) and (a>=c) and (a>=d):
    print ('najvacsie cislo je ',a)
elif (c>=b)and(c>=a) and (c>=d):
    print ('najvacsie cislo je ',c)
elif (b>=a) and (b>=c) and (b>=d):
    print ('najvacsie cislo je ',b)
elif (d>=a) and (d>=b) and (d>=c):
    print ('najvacsie cislo je ',d)


