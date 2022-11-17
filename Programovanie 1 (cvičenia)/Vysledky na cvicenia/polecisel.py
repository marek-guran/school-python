#program na najdenie 1,2,3 maxima a 1,2,3 minima
a=input('zadajte cele cisla')
p=a.split()
p2=[]
for i in range( len(p)):
    p2.append(int(p[i]))
p2.sort()
print('prve dva minima su:',p2[0], ' ',p2[1], ' ' ,p2[2])
print('prve dva maxima su:',p2[len(p2)-1], ' ',p2[len(p2)-2], ' ' ,p2[len(p2)-3])
