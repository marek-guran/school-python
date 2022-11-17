#Program na zistenie poctu vyskytov pismen v retazci
class Queue:
    class Vrchol:
        def __init__(self,data,pocet,next=None):
            self.data=data
            self.pocet=pocet
            self.next=next

    def __init__(self):
        self.zac=None
        self.kon=None

    def push(self,data,pocet):
        if self.zac is None:
            self.zac=self.kon=self.Vrchol(data,pocet)
        else:
            self.kon.next=self.Vrchol(data,pocet)
            self.kon=self.kon.next
        return True

    def update(self,data):
        result=False
        if self.zac is not None:
            pom=self.zac
            while pom is not None:
                if pom.data==data:
                    pom.pocet=pom.pocet+1
                    result=True
                    break
                pom=pom.next
            return result
        else:
            return result

    def begin_queue(self):
        if self.zac is not None:
            return self.zac.data
        else:
            return None
            
    def write_queue(self):
        pom=self.zac
        while pom is not None:
            print(pom.data,':',pom.pocet,end=' -> ')
            pom=pom.next
        print('None')

    
#--------Main program-----------
z1=Queue()
ret=input('Zadaj vety... ')
for i in range(len(ret)):
    if z1.update(ret[i]) == False:
        z1.push(ret[i],1)
z1.write_queue()
