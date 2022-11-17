#stvorec vykresleny hviezdami, Marek Guráň
side = int(input("Zadajte stranu a: "))

print("Štvorec vykreslený v hviezdičkách:") 

for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()
