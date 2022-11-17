#Program na nacitanie slov do pola retazcov
ret=input('Zadajte cisla oddelene ciarkou ')
p=ret.split(',')
p2=[]
for i in range(len(p)):
    p2.append(int(p[i]))
    print(p2[i])
    
