#Program na prevod binarneho cisla na dekadicke
def dec(s):
    
    k = len(s)-1
    cislo = 0

    for i in range(len(s)):
        cislo+=*(2**k)
        k-=1

    print('cislo v dekadickej sustave je',cislo)
    return cislo


