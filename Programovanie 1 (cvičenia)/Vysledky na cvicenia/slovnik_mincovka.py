HODNOTY_MENY = (5000,1000,500,200,100,50,20,10,5,2,1)
celkovyPocetHodnoty = {hodnota:0 for hodnota in HODNOTY_MENY}

def mincovka_jeden(suma):
    for hodnota in HODNOTY_MENY:
        pocet = suma//hodnota
        if pocet > 0:
            celkovyPocetHodnoty[hodnota] += pocet
            print("{:5d} € .... {:2d}".format(hodnota, pocet))
        suma = suma%hodnota

def mincovka_vsetci():
    for meno in zamestnanci:
        print("{:7s} {:5d} €".format(meno,zamestnanci[meno]))
        mincovka_jeden(zamestnanci[meno])
        print(15*"=")
        print("MINCOVKA-SUMÁR:")
    for hodnota in HODNOTY_MENY:
        print("{:5d} € .... {:2d}".format(hodnota, celkovyPocetHodnoty[hodnota]))
# ================== HLAVNÝ PROGRAM ===================

zamestnanci = {}
while 1==1:
    print()
    print('Vyber polozku z menu ')
    print('Novy zamestnanec........1')
    print('Vypis mincovky..........2')
    volba=int(input())
    if volba==1:
        novy_zamestnanec
mincovka_vsetci()
