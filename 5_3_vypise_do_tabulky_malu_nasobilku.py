# Vytvorte program, ktorý vypíše do tabuľky malú násobilku.

x=0
def nasobilka (x):
    for i in range(1,11,1):
        print('{:2}{:3}{:4}{:4}{:4}{:4}{:4}{:4}{:4}{:5}'.format(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10))
    return (x)           #alebo stačí dať opačné lomitko t \t čo znamená tabulátor
nasobilka (x)

