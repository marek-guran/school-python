#FUNKCIA na zistenie, ci je matica symetricka podla hlavnej diagonaly
mat=[[1,2,1,2],[1,2,1,2],[4,5,4,5],[4,5,4,5]]
def matica_symetricka(mat):
    vysl=True
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]!=mat[j][i]:
                vysl=False
    return vysl            
