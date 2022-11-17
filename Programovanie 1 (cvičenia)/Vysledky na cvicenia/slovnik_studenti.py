#PROGRAM na evidenciu ziakov a znamky za predmety
def novy_student():
    meno=input('Zadajte meno studenta ')
    if meno in zoznam.keys():
        print('Student so zadanym meno uz existuje!')
    else:
        print('Zadajte znamky (ukoncene 0)')
        znamka=-1
        studium=[]
        while znamka!=0:
            znamka=int(input())
            if znamka!=0:
                studium.append(znamka)
        if len(studium)==0:
            studium.append(0)
        zoznam[meno]=studium
            
def zmazanie_studenta():
    if len(zoznam)==0:
        print('Zaoznam je prazdny!')
    else:    
        meno=input('Zadajte meno ')
        if meno in zoznam.keys():
            del zoznam[meno]

def vypis_studentov(device):
    if not len(zoznam)>0:
        print('Zoznam studentov je prazdny!')
    else:
        if device==0:    #vypis na obrazovku
            f=None
        else:           #vypis do suboru
            nazov=input('Zadajte meno suboru ')
            f=open(nazov,'w')
        for meno,studium in zoznam.items():
            sucet=0
            print('{:20s}'.format(meno),end='',file=f)
            for i in range(len(zoznam[meno])):
                print('{:<2d}'.format(zoznam[meno][i]),end='',file=f)
                sucet=sucet+zoznam[meno][i]
            print(' Priemer ','{:<3.2f}'.format(sucet/len(zoznam[meno])),file=f)    
        

#====================HLAVNY PROGRAM=================
zoznam={}
volba=0
while True:
    print()
    print('Novy student............1')
    print('Vypis znamok............2')
    print('Zapis do suboru.........3')
    print('Zmazanie studenta.......4')
    print('Koniec..................0')
    volba=int(input())
    if volba==1:
        novy_student()
    elif volba==2:
        vypis_studentov(0)
    elif volba==3:
        vypis_studentov(1)
    elif volba==4:
        zmazanie_studenta()
    elif volba==0:
        print('Koniec programu!')
        break
