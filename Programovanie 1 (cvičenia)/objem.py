#Vypocet objemu v litroch
r=float (input ('Zadajte polomer podstavy valca v cm'))
w=float (input ('Zadajte vysku valca v cm'))
v=22/7*r*r*w #Objem v cm3
v=v/1000
print ('Objem je',v,'litrov')
