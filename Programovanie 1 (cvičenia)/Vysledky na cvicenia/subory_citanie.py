#Program na pracu so suborom
t=open('subor1.txt','r')
for i in range(5):
    riadok=t.readline()
    print(riadok)
t.close()    
