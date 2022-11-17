#Cvicenie, priklad 1, Marek Guráň
print('Pri zadávaní súboru, treba dať aj končiace .txt')
nazov=input("zadajte nazov a cestu k suboru:")
s=open(nazov,"r")
r=s.read()
print(r)
s.close()
