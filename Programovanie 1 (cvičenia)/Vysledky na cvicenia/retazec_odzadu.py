#Program na vypis retazca odzadu
ret=input('Zadaj retazec')
for i in range(-1,-len(ret)-1,-1):
    print(i,ret[i])
