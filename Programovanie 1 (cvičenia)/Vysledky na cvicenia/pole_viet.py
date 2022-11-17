#program na zistenie počtu slov vo vete
p=input("zadajte dlhý reťazec")
r=p.split()
poc=0
for i in range(len(r)):
    x=r[i]
    if(x[0]<="Z" and x[0]>="A"):
        poc=poc+1
print("počet slov v reťazci je: ",(len(r)))
print("počet slov začínajucich veľkým písmenom je: ",poc)
        
