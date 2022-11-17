#Program na precitanie riadkov suboru cez while
f=open('subor1.txt','r')
riadok=f.readline()
while riadok!='':
    print(riadok)
    riadok=f.readline()
f.close()    
    
