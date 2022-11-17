#program na pocetnost pismen a,b,c
nazov=input("zadajte nazov a cestu k suboru ")
s=open(nazov,"r")
r=s.read()
r=r.upper()
print("pocet pismen A je ",r.count("A"))
print("pocet pismen B je ",r.count("B"))
print("pocet pismen C je ",r.count("C"))
s.close()
