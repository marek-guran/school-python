#Program na zapis 100 nahodnych cisel do suboru a na koniec este dopise 20 cisel
import random
f=open('subor3.txt','w')
for i in range(100):
    print(random.randint(1,100),end=' ',file=f)
f.close()    
f=open('subor3.txt','a')
f.write('\nZapis novych 20 cisel z intervalu <1..50>\n')
for i in range(20):
    print(random.randint(1,50),end=' ', file=f)
f.close()    
