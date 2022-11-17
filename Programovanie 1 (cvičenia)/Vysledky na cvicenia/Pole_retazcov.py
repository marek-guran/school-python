#PROGRAM na zlepenie retazcov z pola retazcov do jedneho retazca
ret=input('Zadajte pole retazcov oddelenych medzerou ')
p=[]
for prvok in ret.split(' '):
    p.append(prvok)
    
p2='|'.join(p)
print(p2)
