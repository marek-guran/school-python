#precitanie udajov zo suboru a z kazdeho riadku zisti minimum a maximum

subor=input('Zadajte meno suboru:')
f=open(subor,'r')

for ret in f:
    while (len(ret)>0 and ret.count(' ')>0):
        ret='118_3_-5_10_-2_0'

m=ret.find(' ')
c=int(ret[ :m])

mini=9999999999999
maxi=-9999999999999

if c>maxi:
    maxi=c
if c<mini:
    mini=c

pom=ret[m+1: ]
ret=pom
