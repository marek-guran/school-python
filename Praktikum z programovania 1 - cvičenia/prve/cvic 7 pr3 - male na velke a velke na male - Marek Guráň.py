#cvicenie 7, priklad 3, Marek Guráň
r=input('Zadajte váš reťazec:')
pv=0
tuple(r)
mr=r.lower()
print(mr)
vr=r.upper()
print(vr)

for i in range(len(r)):
    slovo=r[i]
    if slovo[0]>='A' and slovo[0]<='Z':
        pvm=r.lower()
print(pvm)

for i in range(len(r)):
    slovo=r[i]
    if slovo[0]>='a' and slovo[0]<='z':
        pvv=r.upper()
print(pvv)

str=r
stm=str.find(r.lower())
stm=r.lower()
print(stm)

#nevedel som ako to spraviť, trápil som sa nad tým 2 hodiny
#a nič iné ma nenapadlo ako to spraviť
