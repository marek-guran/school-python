#program na najdenie minima a maxima v textovom subore
nazov=input("Zadajte nazov a cestu k suboru:")
f = open (nazov,"r")

for red in f :
    mini=99999999999999999999999999999
    maxi=-9999999999999999999999999999
    while(len(red) > 0 and red.count(" ") )> 0:
        poz = red.find(" ")
        cislo = int(red[:poz])
        if(cislo > maxi):
            maxi = cislo
        if(cislo < mini):
            mini = cislo
        pom = red[poz+1:]
        red = pom
    if(len(red) > 0):
        cislo = int(red)
        if(cislo > maxi):
            maxi = cislo
        if(cislo < mini):
            mini = cislo
    print('maxi= ',maxi)
    print('mini= ',mini)
        
