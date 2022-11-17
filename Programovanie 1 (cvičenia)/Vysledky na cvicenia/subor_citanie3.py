#Program na precitanie riadkov suboru cez for a suborovu premennu
f=open('subor1.txt','r')
for riadok in f:
    print(repr(riadok))
f.close()    
