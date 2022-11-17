slovnikSA = {
    "začať" :"begin",
    "ak" :"if",
    "koniec" :"end",
    "pokiaľ" :"while",
    "pre" :"for",
    "opakovať" :"repeat",
    "dostať" :"get",
    "vrátiť" :"return",
    "nastaviť" :"set" }
def main():
    while True:
        print()
        print("Preklad slovensko -> anglický .......... 0")
        print("Preklad anglicko -> slovenský .......... +")
        print("Koniec ................................. Enter")
        odpoved = input("Tvoja voľba: ")
        if odpoved == "":
            break
        if odpoved == "0":
            sl_slovo = input("Preložiť slovenské slovo: ")
            if sl_slovo in slovnikSA:
                print(sl_slovo, " - ", slovnikSA[sl_slovo])
            else:
                print(sl_slovo, " - ?")
                an_slovo = input("Preklad: ")
                slovnikSA[sl_slovo] = an_slovo
        elif odpoved == "+":
            hladat = input("Preložiť anglické slovo: ")
            naslo_sa = False
            for sl_slovo, an_slovo in slovnikSA.items():
                if an_slovo == hladat:
                    print(an_slovo, " - ", sl_slovo)
                    naslo_sa = True
                    break
            if not naslo_sa:
                print(hladat, " - ?")
                sl_slovo = input("Preklad: ")
                slovnikSA[sl_slovo] = hladat
        else:
            print("Stlačený zlý kláves!")
main()
