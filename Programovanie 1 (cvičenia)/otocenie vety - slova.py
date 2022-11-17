#vypisanie slov v opacnom poradi
import random
x=input('Zadajte vetu:')
def otoc(x):
    z=' '
    for i in range(len(x)-1, -1, -1):
        z=z+x[i]
    return z

s=input('Zadajte vetu 2:')
while len(s)>0 and s.find(' ')>0:
    p=s.find(' ')
    slovo=s[:p]
    s2=otoc(slovo)
    print(s2,end=' ')
    s=s[p+1: ]
if len(s)>0:
    s2=otoc(s)
    print(s2)
