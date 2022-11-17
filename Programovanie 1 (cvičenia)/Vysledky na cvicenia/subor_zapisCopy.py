#Kopirovanie obsahu textoveho suboru do 2.suboru
f=open('subor1.txt','r')
riadok=f.read()
f.close()
f=open('subor11.txt','w')
f.write(riadok)
print('Zapis sa skoncil!')
f.close()
