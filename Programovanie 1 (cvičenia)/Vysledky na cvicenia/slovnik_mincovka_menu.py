HODNOTY_MENY = (5000,1000,500,200,100,50,20,10,5,2,1)
def novy_zamestnanec():
    meno=input('Zadajte  meno zamestnanca ')
    if meno in zamestnanci.keys():
        print('Zamestnanec s takymto menom uz existuje! ')
    else:
        suma=int(input('Zadajte vyplatu zamestnanca '))
    zamestnanci[meno]=suma
    
def mincovka_jeden(suma):
    for hodnota in HODNOTY_MENY:
        pocet = suma//hodnota
        if pocet > 0:
            SH[hodnota] += pocet
            print("{:5d} € .... {:2d}".format(hodnota, pocet))
        suma = suma%hodnota

def mincovka_vsetci():
    for i in range(len(HODNOTY_MENY)):
        SH[HODNOTY_MENY[i]]=0
    for meno in zamestnanci:
        print("{:7s} {:5d} €".format(meno,zamestnanci[meno]))
        mincovka_jeden(zamestnanci[meno])
        print(15*"=")
    print("MINCOVKA-SUMÁR:")
    for hodnota in HODNOTY_MENY:
        print("{:5d} € .... {:2d}".format(hodnota, SH[hodnota]))

def zapis_subor():
    nazov=input('Zadajte nazov suboru ')
    f=open(nazov,'w')
    for meno in zamestnanci:
        print("{:7s} {:5d} €".format(meno,zamestnanci[meno]),file=f)
        mincovka_jeden(zamestnanci[meno])
    print(15*"=",file=f)
    print("MINCOVKA-SUMÁR:",file=f)
    for hodnota in HODNOTY_MENY:
        print("{:5d} € .... {:2d}".format(hodnota, SH[hodnota],file=f))
    f.close()

# ================== HLAVNÝ PROGRAM ===================

zamestnanci = {}
SH={}
for i in range(len(HODNOTY_MENY)):
    SH[HODNOTY_MENY[i]]=0
while 1==1:
    print()
    print('Vyber polozku z menu ')
    print('Novy zamestnanec........1')
    print('Vypis mincovky..........2')
    print('Zapis do suboru.........3')
    volba=int(input())
    if volba==1:
        novy_zamestnanec()
    elif volba==2:
        mincovka_vsetci()
    elif volba==3:
        zapis_subor()
    else:
        print('Koniec programu...')
        break
