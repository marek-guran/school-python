#PROGRAM na zistenie poctu slov vety a pocet slov s velkymi pismenami
ret=input('Zadajte vety ')
p=ret.split()
pv=0
print('Suvetia obsahuju ',len(p), ' slov')
for i in range(len(p)):
    slovo=p[i]
    if slovo[0]>='A' and slovo[0]<='Z':
        pv+=1
print('Pocet slov s velkymi pismenami je ',pv)        
