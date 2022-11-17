#Program na zistenie, cie je dane cislo prvocislo
cislo=int(input('Zadajte cele cislo '))
delitel=2
while delitel< cislo and cislo % delitel !=0 :
    delitel=delitel+1

if delitel==cislo:
    print(cislo, ' je prvocislo')
else:
    print(cislo, ' nie je prvocislo')
