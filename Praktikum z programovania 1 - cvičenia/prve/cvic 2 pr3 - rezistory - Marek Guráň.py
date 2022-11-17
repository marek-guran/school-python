#program na zistenie vysledneho odporu 2 rezistorov(seriovo a paralelne),  Marek Guráň
print ('Zadajte hodnoty na zistenie odporu dvoch rezistorov: (v ohmoch)')
R1=int (input('Rezistor jedna:'))
R2=int (input('Rezistor dva:'))
R=R1+R2
print ('Vysledny odpor je:',R, 'ohmov, ktore su zapojene seriovo')
#Paralelne:
R=(R1*R2)/(R1+R2)
print ('Vysledny odpor je:',R, 'ohmov, ktore su zapojene paralelne')
