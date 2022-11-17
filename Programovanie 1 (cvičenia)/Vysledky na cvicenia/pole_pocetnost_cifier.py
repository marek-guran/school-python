#program zisti pocetnost cifier

ret = input('Zadajte dlhe cislo: ')
v = [0]*10
for i in ret:
    v[int(i)]+=1
for i in range(len(v)):
    print(i,' sa nachadza ',v[i],' krat')
