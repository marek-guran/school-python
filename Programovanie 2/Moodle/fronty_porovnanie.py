#Program na zistenie ci su 2 fronty rovnake
class Queue:
    class Vrchol:
        def __init__(self,data,next=None):
            self.data=data
            self.next=next

    def __init__(self):
        self.zac=None
        self.kon=None

    def push(self,data):
        if self.zac is None:
            self.zac=self.kon=self.Vrchol(data)
        else:
            self.kon.next=self.Vrchol(data)
            self.kon=self.kon.next
        return True

    def pop(self):
        if self.zac is not None:
            novy=self.zac
            self.zac=self.zac.next
            return novy.data
        else:
            return None

    def begin_queue(self):
        if self.zac is not None:
            return self.zac.data
        else:
            return None
            
    def write_queue(self):
        pom=self.zac
        while pom is not None:
            print(pom.data,end='->')
            pom=pom.next
        print('None')

def compare_queue(zac1,zac2):
    result=True
    while zac1.begin_queue() is not None and zac2.begin_queue() is not None:
        x1=zac1.pop()
        x2=zac2.pop()
        if x1 != x2:
            result=False
    if zac1.begin_queue() is not None:
        result=False
    if zac2.begin_queue() is not None:
        result=False
    return result    
    
#--------Main program-----------
z1=Queue()
z2=Queue()
ret=input('Zadaj prvky 1. postupnosti ')
pole=ret.split()
for i in range(len(pole)):
    x=int(pole[i])
    z1.push(x)
ret=input('Zadaj prvky 2. postupnosti ')
pole=ret.split()
for i in range(len(pole)):
    x=int(pole[i])
    z2.push(x)
pom=compare_queue(z1,z2)
if pom is True:
    print('Spajane zoznamy su identicke.')
else:
    print('Spajane zoznamy su rozdielne.')
