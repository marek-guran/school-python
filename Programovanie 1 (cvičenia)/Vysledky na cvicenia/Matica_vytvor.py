def matica_vytvor():
    matica=[]
    riadky=int(input('Zadaj pocet riadkov ')
    stlpce=int(input('Zadaj pocet stlpcov ')
    
    for i in range(riadky):
        temp = []
        for j in range(stlpce):
            x=int(input('Prvok [',i,',',j,']'))
            temp.append(x)
        matica.append(temp)
    for i in range(riadky):
        for j in range(stlpce):
            print(matica[i][j],end=' ')
        print()    
    return matica


