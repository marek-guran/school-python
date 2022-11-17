#program na vypocitanie suctu prevratenych hodnot od 1 do daneho N
n=int(input('Vlozte kladne cislo:'))
v=0
for i in range (n):
    v=v+1/(i+1)
print('Sucet obratenych hodnot je:',v)
