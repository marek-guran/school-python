#Program na nacitanie vyskytu znakov A,B,C v subore
f=open('subor1.txt','r')
riadok=f.read()
pa=pb=pc=0
riadok=riadok.upper()
print(riadok)
for i in range(0,len(riadok)-1):
    if riadok[i]=='A':
        pa=pa+1
    if riadok[i]=='B':
        pb=pb+1
    if riadok[i]=='C':
        pc=pc+1
print('Pocet a je ',pa, 'pocet b je ',pb,' pocet c je ',pc)
f.close()
        
