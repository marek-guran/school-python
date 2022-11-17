def matica_vytvor(riadky,stlpce):
    matica=[]
    for i in range(riadky):
        temp=[]
        for j in range(stlpce):
            x=int(input('Zadajte cislo'))
            temp.append(x)
        matica.append(temp)

    print('Vypis matice:')
    for i in range(riadky):
        for j in range(stlpce):
            print(matica[i][j],end=' ')
        print()
    return matica    
        
matica_vytvor(riadky,stlpce)
