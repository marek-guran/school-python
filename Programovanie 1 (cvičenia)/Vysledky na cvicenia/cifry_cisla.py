#PROGRAM na zistenie poctu cifier
x=int(input('Zadajte cele cislo '))
p=0
while (x>0):
    x=x//10
    p=p+1
print('Cislo obsahuje ',p,' cifier')    
