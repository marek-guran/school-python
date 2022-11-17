#program zisti prve 3 najvacsie cisla

prve = 0
druhe = 0
tretie = 0

for i in range(10):
    x = int(input('Zadajte cislo'))
    if abs(prve)<abs(x) :
        prve = x
    elif abs(x)>abs(tretie) and abs(x)<abs(prve) and abs(x)> abs(druhe):
        druhe = x
    elif abs(x)<abs(prve) and abs(x)<abs(druhe) and abs(x) > abs(tretie):
        tretie = x
print('Prve: ',prve,'Druhe: ',druhe,'Tretie: ',tretie)

    
        
    
    
