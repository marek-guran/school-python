#Napíšte program,
#ktorý ztextového súboru obsahujúceho celé čísla vytvorí
#osobitné pole párnych čísel, nepárnych čísel.
#Všetky čísla ktoré sa poliach viac krát opakujú budú vymazané.
a='Ruza konecne zvitazi v europskej lige'
print(a.split())
p=a.split()
print(len(p))

for i in range (len(p)):
    x=p[i]
    if 'z'<=x[0]<='z':
        print(x[i])
