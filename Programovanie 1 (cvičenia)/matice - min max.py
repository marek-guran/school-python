#Je zadaná štvorcová matica celých čísel s rozmerom NxN, N<20.
#Vymeňte v nej najväčší prvok s najmenším. Ak je v matici viac prvkov,
#s rovnakou maximálnou hodnotou alebo minimálnou hodnotou použite prvý z nich.
def matica_minmax(a):
    maxi=mini=a[0][0]
    imaxi=jmaxi=imini=jmini=0
    for i in range (len(a)):
        for j in range(len(a[i])):
                        if a[i][j]>maxi:
                            maxi=a[i][j]
                            imaxi=i
                            jmaxi=j
                        if a[i][j]<mini:
                            mini=a[i][j]
                            imini=i
                            jmini=j
    a[imaxi], n[mini][jmini]=n[imini][jmini],n[imaxi][jmaxi]
    for i in range (len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
    return None
