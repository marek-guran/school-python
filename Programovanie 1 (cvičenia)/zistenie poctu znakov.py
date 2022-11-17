#na zistenie vyskytu znaku v retazci
pocet=0
znak=input('Zadajte znak:')
s=input('Zadajte retazec:')
for i in range (len(s)):
    if s[i].upper()==znak.upper:
        pocet=pocet+1
print('V retazci je' , pocet, 'znakov:' ,znak)
