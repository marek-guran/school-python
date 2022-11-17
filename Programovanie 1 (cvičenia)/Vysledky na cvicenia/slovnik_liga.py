#PROGRAM na evidovanie futbalovej ligy
def pridaj_druzstvo():
    druzstvo=input('Zadajte druzstvo ')
    if druzstvo in liga.keys():
        print('Druzstvo uz v tabulke existuje!')
    else:
        vysledky=[];
        vyhry=int(input('Zadajte vyhry '))
        vysledky.append(vyhry)
        remizy=int(input('Zadajte remizy '))
        vysledky.append(remizy)
        prehry=int(input('Zadajte prehry '))
        vysledky.append(prehry)
        liga[druzstvo]=vysledky
        
def oprav_vysledky():
    druzstvo=input('Zadajte druzstvo ')
    if druzstvo in liga.keys():
        pom=input('Zadajte polozku opravy V/vyhra R/remiza P/prehra' )
        if pom=='V':
            vyhry=int(input('Zadajte vyhry '))
            liga[druzstvo][0]=vyhry
        elif pom=='R':
            remizy=int(input('Zadajte remizy '))
            liga[druzstvo][1]=remizy
        elif pom=='P':
            prehry=int(input('Zadajte prehry '))
            liga[druzstvo][2]=prehry
    else:
        print('Chybne zadane druzstvo alebo druzstvo neexistuje!')
            
def zmaz_druzstvo():
    druzstvo=input('Zadajte druzstvo ')
    if druzstvo in liga.keys():
        del liga[druzstvo]
    else:
        print('Chybne zadane druzstvo alebo druzstvo neexistuje!')

def vypis_tabulky(device):
    if len(liga)==0:
        print('Tabulka je prazdna!')
    else:
        if device==0:     #vypis na obrazovku
            print('{:<19}{:>5}{:>4}{:>4}{:>4}'.format('Tabulka','Body','V','R','P'))
            print('='*40)
            for druzstvo,vysledky in sorted(liga.items(), key=lambda podla: podla[1], reverse=True):
                body=0
                for i in range(len(vysledky)):
                    if i==0:
                        body=body+vysledky[i]*2
                    elif i==1:
                        body=body+vysledky[i]
                    else:
                        pass
                print('{:<20}'.format(druzstvo),end='')
                print('{:>4}'.format(body),end='')
                for i in range(len(vysledky)):
                    print('{:>4}'.format(vysledky[i]),end='')
                print()
        else:           #zapis do suboru
            nazov=input('Zadajte meno suboru ')
            f=open(nazov,'w')
            print('{:<19}{:>5}{:>4}{:>4}{:>4}'.format('Tabulka','Body','V','R','P'),file=f)
            print('='*40,file=f)
            for druzstvo,vysledky in sorted(liga.items(), key=lambda podla: podla[1], reverse=True):
                body=0
                for i in range(len(vysledky)):
                    if i==0:
                        body=body+vysledky[i]*2
                    elif i==1:
                        body=body+vysledky[i]
                    else:
                        pass
                print('{:<20}'.format(druzstvo),end='',file=f)
                print('{:>4}'.format(body),end='',file=f)
                for i in range(len(vysledky)):
                    print('{:>4}'.format(vysledky[i]),end='',file=f)
                print(file=f)    
            f.close()
             
#============ HLAVNY PROGRAM ===============
liga={}
volba=0
while True:
    print()
    print('Vyber polozku z menu: ')
    print('Pridanie druzstva...............1')
    print('Uprava vysledkov druzstva.......2')
    print('Zmazanie druzstva...............3')
    print('Vypis tabulky...................4')
    print('Zapis do suboru.................5')
    print('Koniec programu.................0')
    volba=int(input())
    if volba==1:
        pridaj_druzstvo()
    elif volba==2:
        oprav_vysledky()
    elif volba==3:
        zmaz_druzstvo()
    elif volba==4:
        vypis_tabulky(0)
    elif volba==5:
        vypis_tabulky(1)
    else:
        print('Koniec programu...')
        break
    
