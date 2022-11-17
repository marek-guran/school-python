#Rozdelenie vyplaty na nominalne bankovky a mince
ntica =  (5000,1000,500,200,100,50,20,10,5,2,1)
slovnik = {}
def vydaj(peniaze):
    suma = peniaze
    s = ()
    for x in ntica:
        p = 0
        p = suma // x
        s = s +(p,)
        if p != 0:
            suma = suma % (x*p)
    return s
def pridaj_cloveka():
    meno = input("Zadajte meno sporiaceho:  ")
    vyplata = int(input("Zadajte vyplatu:   "))
    prepocet = vydaj(vyplata)
    pole = []
    pole.append(vyplata)
    for i in prepocet:
        pole.append(prepocet[i])
    slovnik[meno] = pole
                
def vypis(zariadenie):
    if zariadenie==1:
        nazov=input("zadajte nazov suboru: ")
        f=open(nazov,"w")
    else:
        f=None
    print("vypis pola zamestnancov a ich vyplat")
    for meno,pole in sorted(slovnik.items()):
        print("{:<20}{:>7}{:>2}{:>2}{:>2}{:>2}{:>2}{:>2}{:>2}{:>2}{:>2}{:>2}{:>2}".format(meno,pole[0],pole[1],pole[2],pole[3],pole[4],pole[5],pole[6],pole[7],pole[8],pole[9],pole[10],pole[11],file=f)) 
# ----------------------hlavny program----------------------------

while True:
    print()
    print("Novy zamestnanec..........n")
    print("Vypis zamestnancov........v")
    print("Zapis do suboru...........z")
    print("Koniec....................k")
    m = input("")
    if m == "n":
        pridaj_cloveka ()
    elif m == "v":
        vypis (0)
    elif m == "z":
        vypis (1)
    elif m == "k":
        print("koniec programu")
        break
        
        
    




        
        
        
        

