#Sú zadané 2 polia znakov. Zistite či majú rovnakú dĺžku.
#Ak sú rovnaké, zistite či sú tvorené rovnakými prvkami.
#Ak nie sú rovnaké, zistite na ktorom prvku sa začínajú odlišovať.
p1=[]
p2=[]
x=input('Zadajte znaky prveho pola:')
p1=list(x)
y=input('Zadajte znaky druheho pola:')
p2=list(y)
if len(p1)!=len(p2):
    print('Polia nemaju rovnaku velkost')
else:
    idx=0
    totozne=True
    for i in range(len(p1)):
        if p1[i]!=p2[i]:
            totozne=False
            idx=i
            break
    if totozne==True:
        print('Polia tvoria rovnake prvky ')
    else:
        print('Polia sa lisia od ',idx,' prvku')
