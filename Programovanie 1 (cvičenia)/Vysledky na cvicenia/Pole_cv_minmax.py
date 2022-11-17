#PROGRAM na zistenie 1,2,3 min a 1,2,3 max z cisel
x=input('Zadaj cele cisla ')
p2=x.split()
p=[]
for i in range(len(p2)):
    p.insert(i,int(p2[i]))
p.sort()
if len(p)>2:
    print('Prve 3 maxima: ',p[len(p)-1],',',p[len(p)-2],',',p[len(p)-3])
    print('Prve 3 minima: ',p[0],',',p[1],',',p[2])
