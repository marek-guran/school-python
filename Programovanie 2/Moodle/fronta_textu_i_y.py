#Program na vytvorenie fronty, ktora v textovom subore nahradi i,y znakom _
class Queue:
    class Vrchol:
        def __init__(self,data,next=None):
            self.data=data
            self.next=next

    def __init__(self):
        self.zac=None
        self.kon=None

    def push(self,data):
        if data in ['i','I','y','Y']:
            data='_'
        if self.zac is None:
            self.zac=self.kon=self.Vrchol(data)
        else:
            self.kon.next=self.Vrchol(data)
            self.kon=self.kon.next
        return True
            
    def write_queue(self):
        pom=self.zac
        while pom is not None:
            print(pom.data,end='')
            pom=pom.next
        print('')
    
#--------Main program-----------
z1=Queue()
nazov=input('Zadaj nazov suboru ')
f=open(nazov,'r')
for riadok in f:
    for i in range(len(riadok)):
        z1.push(riadok[i])
z1.write_queue()    
f.close()
