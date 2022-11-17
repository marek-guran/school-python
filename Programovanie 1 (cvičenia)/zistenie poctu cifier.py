#urcenie poctu cifier daneho cisla
print('Funkcia sa spusti: pocet(x)')
x=int(input('Vložte čísla:'))
def pocet(x):
    p=0
    n=0
    for i in range(len(str(x))):
        if x%2>0:
            n=+1
        else:
            p+=1
        x=x//10
    return p,n
