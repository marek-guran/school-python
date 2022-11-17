#Program na nacitanie postupnosti cisel a zapisanie do pola cisel
ret=input('Zadaj niekolko cisel oddelenych ciarkami')
pole=ret.split(',')
p2=[]
for i in range(len(pole)):
    p2.append(int(pole[i]))
