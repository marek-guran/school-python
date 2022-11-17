#Program na vypocet n-teho faktorialu zo zadaneho cisla n
n=int(input('Zadaj cele cislo'))
sucin=1
for i in range (1,n+1):
    sucin=sucin * i
print('{:3} ! = {:6} '.format(n,sucin))    
