#Program na podmienky podla veku
vek=int(input('Zdajte vek osoby '))
if vek<6 :
    print('Vstupenka zadarmo! ')
elif vek>5 and vek<15 :
        print('Vstupenka za 6 eur')
elif vek>15 and vek<61 :
            print('Vstupenka za 8 eur')
else:
            print('Vstupenka za 7 eur')
            
