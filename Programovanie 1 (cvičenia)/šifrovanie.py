#šifrovaná správa
nazov=input('Zadajte názov súboru na prečítanie:')
r='Mama ma Emu'
velke=[]
male=[]
posun=int(input('Vložte posun:'))
nazov2=nazov[:pozicia]+'_sifra'+nazov[pozicia+1:]
pozicia=r.find('.')

for i in range (ord('Z')-ord('A')+1):
    velke.append(chr(ord('A')+i))
    
for i in range (ord('z')-ord('a')+1):
    male.append(chr(ord('a')+i))

for i in range (len(r)):
    x=r[i]
    if x in velke:
        if ord(x)+posun>ord('Z'):
            (chr(ord(x)+posun % ord('Z'))+ord('A')-1)
        else:
            x=(ord(x)+posun)

for i in range (len(r)):
    x=r[i]
    if x in male:
        if ord(x)+posun>ord('z'):
            (chr(ord(x)+posun % ord('z'))+ord('a')-1)
        else:
            x=(ord(x)+posun)
def sifra(riadok,posun):
    ret=''
    for i in range (len(riadok)):
        if riadok[i] in velke:
            if (ord(riadok[i])+posun)>ord('Z'):
                x=((ord(riadok[i])+
