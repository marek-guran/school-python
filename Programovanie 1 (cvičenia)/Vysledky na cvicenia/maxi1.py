#Program na zistenie maxima z cisel zadanych z klavesnice
a=int(input('Zadajte cislo '))
maxi=a
p=0
while (a!=0):
    if a>maxi:
        maxi=a
        p=1
    elif a==maxi:
        p+=1
    a=int(input('Zadajte cislo '))
