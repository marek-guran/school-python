#program na zistenie poctu cifier
def pocetcifier (x):
    c=0
    while (x>0):
        x=x//10
        c+=1
    return c
