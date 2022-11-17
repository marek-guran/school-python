#Zistenie kolko je slov kociacich sa na A a male a v subore
nazov=input("zadajte nazov alebo cestu k suboru:")
f=open(nazov,'r')
ret=f.read()
pa=0
for i in range(len(ret)):
    if (ret[i] in ['a','A'] and ret[i+1] in [' ','\n','.',',','!',':','?','\'']):
        pa=pa+1
print('Pocet slov konciacich na a je:',pa)
f.close()
