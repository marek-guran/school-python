#program na scitavanie nenulovzch hodnot do 1000, Marek Guráň

v=int(input('Vlozte cislo:'))
for i in range (1000):
    if v==0:
        break
    v=v+1
    if v>1000:
        break
    print(v)
