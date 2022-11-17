#Vypocet BMI, Marek Guráň
kg=int(input('Zadajte vašu váhu(kg):'))
v=float(input('Zadajte vašu výšku(m):'))
BMI=kg/(v)**2
if BMI<18.5:
    print('Máte podváhu')
elif 18.5<BMI<25:
    print('Normálna hmotnosť')
elif 25<BMI<30:
    print('Máte nadváhu')
elif BMI>30:
    print('Máte nadváhu')
