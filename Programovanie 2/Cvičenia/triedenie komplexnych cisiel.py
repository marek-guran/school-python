#Komplexné čísla - triedenie podľa absolútnej hodnoty
def minsort(b):
    for i in range (len(b)-1):
        minimum = i
        for j in range (i+1, len(b)):
            if b[minimum][2]>b[j][2]:
                minimum=j
        b[i],b[minimum]=b[minimum],b[i]
    return b
