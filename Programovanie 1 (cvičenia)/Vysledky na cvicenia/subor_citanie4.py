#Program na precitanie naray vsetkych riadokov do jednej premennej
f=open('subor1.txt','r')
riadok =f.read()
print(repr(riadok))
f.close() 
