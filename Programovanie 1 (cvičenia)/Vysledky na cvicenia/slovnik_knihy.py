#Program na evidenciu knih cez eshop
def pridanie_knihy():
    nazov=input('Zadajte nazov knihy ')
    if nazov in zoznam.keys():
        print('Kniha uz existuje v zozname!')
    else:
        polozky=[]
        autor=input('Zadajte autora knihy ')
        polozky.append(autor)
        rok=int(input('Zadajte rok vydania '))
        polozky.append(rok)
        cena=float(input('Zadajte cenu knihy '))
        polozky.append(cena)
        zoznam[nazov]=polozky

def vypis_knih(device):
    if device==0:
        f=None
    else:
        subor=input('Zadajte nazov suboru ')
        f=open(subor,'w')
        
    print('{:30}{:15}{:>5}{:>7}'.format('Nazov','Autor','Rok','Cena'),file=f)
    print('='*70,file=f)
    for nazov,polozky in sorted(zoznam.items(), key=lambda podla:podla[1]):
        print('{:30}{:15}{:>5}{:>7.2f}'.format(nazov,polozky[0],polozky[1],polozky[2]),end='',file=f)
        print()
    return 0  

def oprava_knihy():
    nazov=input('Zadajte nazov knihy ')
    volba=input('Vyberte Autora[A] / Rok[R] / Cenu[C]')
    if volba.upper()=='A':
        autor=input('Zadajte opravene meno autora ')
        zoznam[nazov][0]=autor
    elif volba.upper()=='R':
        rok=int(input('Zadajte opraveny rok '))
        zoznam[nazov][1]=rok
    elif volba.upper()=='C':
        cena=float(input('Zadajte opravenu cenu '))
        zoznam[nazov][2]=cena
        
def zmazanie_knihy():
    nazov=input('Zadajte nazov knihy na zmazanie: ')
    if nazov not in zoznam.keys():
        print('Kniha s tymto nazvom neexistuje v databaze!')
    else:
        del zoznam[nazov]
        print('Kniha bola zmazana!')
    return 0

#------------------HLAVNY PROGRAM-------------------
zoznam={}
volba=0
while True:
      print()
      print('Vyber polozku menu: ')
      print('Pridanie knihy..............1')
      print('Uprava autora alebo cenu....2')
      print('Zmazanie knihy..............3')
      print('Vypis zoznamu knih..........4')
      print('Zapis do suboru.............5')
      print('Koniec programu.............0')
      volba=int(input())
      if volba==1:
            pridanie_knihy()
      elif volba==2:
            oprava_knihy()
      elif volba==3:
            zmazanie_knihy()
      elif volba==4:
            vypis_knih(0)
      elif volba==5:
            vypis_knih(1)
      else:
            print('Koniec programu...')
            break
      
