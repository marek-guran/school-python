#zistenie minima a maxima z pola
p=[]
x=input('Zadajte prvy pola oddelene !')
p2=x.split('!')
for i in range (len(p2)):
    p.insert(i,int(p2[i]))
p.sort()
print('3 minima su:', p[0],',',p[1],',',p[2])
p.reverse()
print('3 maxima su:', p[0],',',p[1],',',p[2])
