#PROGRAM na tvorbu databazy lovcov
def novy_lovec():
    meno=input('Meno lovca: ')
    if meno in zoznam.keys():
        print('Meno sa uz v zozname vyskytuje')
    trofeje=[]
    x=int(input('Pocet lisok:'))
    trofeje.append(x)
    y=int(input('Pocet zajacov:'))
    trofeje.append(y)
    z=int(input('Pocet kacic:'))
    trofeje.append(z)
    zoznam[meno]=trofeje

def vypis_lovcov():
    for meno,trofeje in sorted(zoznam.items()):
        print("{:10}".format(meno), end=' ' )
        for i in range(len(trofeje)):
            print('{:>3}'.format(trofeje[i]),end='')
        print()        
        
def vypis_trofeji():
    for meno,trofeje in sorted(zoznam.items(), key=lambda podla: podla[1]):
        print("{:10}".format(meno), end=' ' )
        for i in range(len(trofeje)):
            print('{:>3}'.format(trofeje[i]),end='')
        print()        

def zmazanie_lovca():
    if len(zoznam)>0:
        meno=input('Zadaj meno lovca:')
        if meno in zoznam.items():
            del zoznam[meno]
        else:
            print('Chybne zadane meno lovca...')

def zapis_subor():
    nazov=input('Zadajte meno suboru ')
    f=open(nazov,'w')
    for meno,trofeje in sorted(zoznam.items()):
        print("{:10}".format(meno), end=' ',file=f )
        for i in range(len(trofeje)):
            print('{:>3}'.format(trofeje[i]),end='',file=f)
        print(file=f)
        
def lovec_vitaz():
    vitaz=[]
    vitaz_suma=0        
    if len(zoznam)>0:
        for meno,trofeje in zoznam.items():
            pom=0
            for i in range(len(trofeje)):
                pom=pom+trofeje[i]
            if pom>vitaz_suma:
                vitaz_suma=pom
                vitaz=[]
                vitaz.append(meno)
            elif pom==vitaz_suma:
                vitaz.append(meno)
            else:
                pass
        print('Najlepsi lovci: ')    
        for i in range(len(vitaz)):
            print(vitaz[i],' trofeji ',vitaz_suma)
        return vitaz            
#========HLAVNY PROGRAM=========
print()
zoznam={}
vitazy=[]
while True:
    print()
    print('Vyberte polozku z ponuky:')
    print('Novy lovec .................1')
    print('Vypis podla mena............2')
    print('Vypis podla trofeji.........3')
    print('Zmazanie lovca..............4')
    print('Zapis do suboru.............5')
    print('Najlepsi strelec............6')
    print('Koniec programu.............0')
    volba=int(input())
    if volba==1:
        novy_lovec()
    elif volba==2:
        vypis_lovcov()
    elif volba==3:
        vypis_trofeji()
    elif volba==4:
        zmazanie_lovca()
    elif volba==5:
        zapis_subor()
    elif volba==6:
        vitazy=lovec_vitaz()
    else:
        print('Koniec programu .......')
        break
        
    
