#Program ktory precita vstupny subor a zisti z neho minimum a maximum.

max=-10000000
min=999999999
f=open('subor_cisel.txt','r')
for ret in f:
    while (len(ret)>0) and (ret.count(' ')>0):
        ix = 0
        while (ix < len(ret)) and (ret[ix] != ' '):
            ix += 1
        cislo=int(ret[:ix])
        print(cislo)
        if cislo>max:
            max=cislo
        if cislo<min:
            min=cislo
        ret2=ret[ix+1:]
        ret=ret2
    if (len(ret)>0):
        cislo=int(ret[:len(ret)])
        print(cislo)
        if cislo>max:
            max=cislo
        if cislo<min:
            min=cislo
print('Minimum je ',min,' a maximum je ',max)            
f.close()
