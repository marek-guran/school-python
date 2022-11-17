#Garage
a=float(input('Zadajte rozmer podlahy '))
b=float(input('Zadajte 2 rozmer podlahy '))
c=float(input('Zadajte vysku garaze '))
u=(a*a+b*b)**0.5
print('Uhlopriecky maju velkost: ',u)
ob=1.0*1.5*1.8
og=a*b*c
p=og//ob
print('Do garaze sa vojde ',p,' celych balikov')
