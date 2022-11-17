#FUNKCIA na efektivnejsie zistenie, ci je matica symetricka podla hlavnej diagonaly
def matica_symetricka2(mat):
    for i in range(1,len(mat)):
        for j in range(i):
            if mat[i][j]!=mat[j][i]:
                return False
    return True 
