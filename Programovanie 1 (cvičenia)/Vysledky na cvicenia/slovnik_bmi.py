def bmi(hmotnost, vyska):
    return hmotnost/vyska/vyska

def hodnotenie(bmi):
    if bmi < 18:
        return "podvýživa"
    elif bmi < 22:
        return "v norme"
    else:
        return "nadváha"

def main(databaza):
    print("{:10} {:5} {}".format("Meno", "BMI", "Hodnotenie"))
    for meno, data in databaza.items():
        lok_bmi = bmi(data[0], data[1])
        lok_hodnotenie = hodnotenie(lok_bmi)
        print("{:10} {:5.2f} {}".format(meno, lok_bmi, lok_hodnotenie))

tretiaci = {"Adela":[48,1.68], "Pavol":[92,1.89],"Peter":[74,1.84],
            "Zuzana":[68,1.68]}
main(tretiaci)
