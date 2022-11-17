#Program na evidovanie SP v slalome
def pridaj_pretekara():
      pretekar=input('Zadajte meno pretekara ')
      if pretekar in slalom.keys():
            print('Pretekar je uz zaevidovany!')
      else:
            casy=[];
            cas1=float(input('Cas z 1.kola '))
            casy.append(cas1)
            cas2=float(input('Cas z 2.kola '))
            casy.append(cas2)
            casy.append(cas1+cas2)
            slalom[pretekar]=casy
            
def oprav_pretekara():
      pretekar=input('Zadajte meno pretekara ')
      if pretekar in lalom.keys():
            pom=int(input('Zadajte 1. alebo 2.kolo (1,2)'))
            if pom==1:
                  cas1=float(input('Zadajte cas 1.kola '))
                  slalom[prekekar][1]=cas1
            elif pom==2:
                  cas2=float(input('Zadajte cas 2.kola '))
                  slalom[pretekar][2]=cas2
      else:
            print('Pretekar nie je v databaze!')

def zmaz_pretekara():
      pretekar=input('Zadajte meno pretekara ')
      if pretekar in slalom.keys():
            del slalom[pretekar]
      else:
            print('Pretekar nie je v databaze!')
      
      
def vypis_tabulky(device):
      if len(slalom)==0:
            print('Slalom je prazdny ')
      else:
            if device==0:     #vypis na obrazovku
                  f=None
            else:
                  nazov=input('Zadajte nazov suboru ')
                  f=open(nazov,'w')
                  
            print('{:20}{:>7}{:>7}{:>8}'.format('Vysledkova listina','1.kolo','2.kolo','Celkom',file=f))
            print('='*40,file=f)
            for pretekar,casy in sorted(slalom.items(), key=lambda podla: podla[1]):
                body=0
                print('{:<20}'.format(pretekar),end=' ',file=f)
                for i in range(len(casy)):
                    print('{:>5.3f}'.format(casy[i]),end=' ',file=f)
                print()
                  

      

#=================HLAVNY PROGRAM============
slalom={}
volba=0
while True:
      print()
      print('Vyber polozku menu: ')
      print('Pridanie pretekara............1')
      print('Uprava vysledkov pretekara....2')
      print('Zmazanie pretekara............3')
      print('Vypis tabulky.................4')
      print('Zapis do suboru...............5')
      print('Koniec programu...............0')
      volba=int(input())
      if volba==1:
            pridaj_pretekara()
      elif volba==2:
            oprav_pretekara()
      elif volba==3:
            zmaz_pretekara()
      elif volba==4:
            vypis_tabulky(0)
      elif volba==5:
            vypis_tabulky(1)
      else:
            print('Koniec programu...')
            break
      
