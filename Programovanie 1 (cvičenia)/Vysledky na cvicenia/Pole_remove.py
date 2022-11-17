#Program na vyhodenie znaku zo vsetkych retazcov
ret=input('Zadaj vetu: ')
p=list(ret)
while 'a' in p:
    p.remove('a')
