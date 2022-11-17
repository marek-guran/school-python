#program na vypocet urokov v banke na 10 rokov
v=int(input('Zadajte vklad:'))
vp=v
u=float(input('Zadajte urok:'))
for i in range (10):
    v=v+(u/100)*v
print('Po 10 tich rokoch bude nasetrene:',v)
roky=0
x=int(input('Zadajte vyslednu ciastku:'))
while vp<x:
    roky=roky+1
    vp=vp+(u/100)*vp
print('Pozadovanu ciastku dosiahneme po:',roky,'rokoch')
    
