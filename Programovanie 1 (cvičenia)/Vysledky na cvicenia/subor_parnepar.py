#PROGRAM ktory precita subor cisel a vytvori z neho subor parnych a neparnych cisel.
#opakujuce sa prvky vymaze
f=open(input('Zadajte nazov suboru '),'r')
ret=f.readline()
p=[]
while ret:
    p2=ret.split()
    for i in range(len(p2)):
        p.insert(i,int(p2[i]))
    ret=f.readline()    
f.close()
fp=open(input('Zadajte nazov suboru parnych cisel '),'w')
fn=open(input('Zadajte nazov suboru neparnych cisel '),'w')

i=0
while i<len(p)-1:
    if p.count(p[i])>1:
        p.remove(p[i])
    else:
        i+=1
        
for i in range(len(p)):        
    if p[i] %2 ==0:
        print(p[i],end=' ',file=fp)
    else:
        print(p[i],end=' ',file=fn)
fp.close()
fn.close()
        
