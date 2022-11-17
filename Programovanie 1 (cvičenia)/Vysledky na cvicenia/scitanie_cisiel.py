#Program na scitanie 2 velmi dlhych ulozenych v subore

nazov1=input("zadajte nazov 1 suboru ")
nazov2=input("zadajte nazov 2 suboru ")
p1=[]
p2=[]
f1=open(nazov1, "r")
f2=open(nazov2, "r")
s1=f1.read()
s2=f2.read()
for i in range (len(s1)-1):
    p1.append(int(s1[i]))
for i in range (len(s2)-1):
    p2.append(int(s2[i]))
p3=[]
if (len(p1))<(len(p2)):
    for i in range (len(p2)-(len(p1))):
        p1.insert(i,0)
else:
    for i in range (len(p1)-(len(p2))):
        p2.insert(i,0)
prenos=0
for i in range (len(p1)-1,-1,-1):
    x=p1[i]+p2[i]+prenos
    p3.append (x%10)
    prenos=x//10
if prenos>0:
    p3.append (1)
print ("vypis scitania")
for i in range (len(p3)-1,-1,-1):
    print(p3[i],end="")
    
    
        
             

    

