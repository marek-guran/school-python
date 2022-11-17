#PROGRAM na vypocet prevratenych hodnot od 1 po dane n
n=int(input('Zadajte cele cislo '))
x=0
for i in range(n):
    x=x+1/(i+1)
print('Sucet prevratenych hodnot je ',x)    
      
