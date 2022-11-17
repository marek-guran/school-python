#Program na vypocet suctu cisel
sucet=0
while True:
    retazec=input('Zadaj cislo: ')
    if retazec == '' :
        break
    sucet += int(retazec)
print('Sucet precitanych cisel = ',sucet)    
