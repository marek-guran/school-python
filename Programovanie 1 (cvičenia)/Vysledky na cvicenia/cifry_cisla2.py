#PROGRAM na prevod dvojkoveho cisla na dekadicke
x=int(input('Zadajte dvojkove cislo '))
y=0
for i in range(len(str(x))):
    z=x%2
    y=y+2**i*z
    x=x//10
print(y)               
               
