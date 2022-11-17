#Program na otocenie slov v retazci
def otocene_slova(s):
    s2=''
    while len(s)>0:
        p=s.find(' ')
        if p>-1:
            r=''
            for i in range(len(s[:p]),-1,-1):
                r=r+s[i]
            s2=s2+r
            s=s[p+1:]
        else:
            break
    print(s)    
    if len(s)>0:
        s2=s2+' '
        r=''
        for i in range(len(s)-1,-1,-1):
            r=r+s[i]
        s2=s2+r
        print(s)
    return s2     
