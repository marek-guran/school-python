#Fronta celych cisel - utriedena
class Queue:
    class Vrchol:
        def __init__(self, data, next=None):
            self.data=data
            self.next=next

    def __init__(self):
        self.zac=None
        self.kon=None

    def is_empty(self):
        return self.zac is None

    def sort_queue(self,data):   #pridanie prvku na spravne miesto5
        if self.zac is None:
            self.zac=self.kon=self.Vrchol(data)
        else:
            if self.zac.data>data:
                pom=self.Vrchol(data)
                pom.next=self.zac
                self.zac=pom
            elif self.kon.data<data:
                self.kon.next=self.Vrchol(data)
                self.kon=self.kon.next
            else:
                pom=self.zac
                while pom is not None and pom.data<data and pom.next.data<data:
                    pom=pom.next
                novy=self.Vrchol(data)
                novy.next=pom.next
                pom.next=novy
            
    def begin_queue(self):
        if self.is_empty():
            print('Fronta je prazdna...')
        else:
            prvy=self.zac
            self.zac=prvy.next
            if self.zac is None:
                self.kon=None
        return prvy.data

    def write_queue(self):     #vypis kompletnej fronty
        if self.is_empty():
            print('Fronta je prazdna...')
        else:
            pom=self.zac
            while pom is not None:
                print(pom.data,end='->')
                pom=pom.next
            print('None')
            
    
#Hlavny program
z=Queue()
while True:
    print()
    print('Prvok do utriedenej fronty........1')
    print('Vypis prvkov fronty................2')
    print('Odobratie prvku zo zaciatku........3')
    print('Najdenie minimalneho prvku.........4')
    print('Nacitanie prvkov zo suboru.........5')
    print('Koniec programu....................0')
    volba=int(input())
    if volba==1:
        x=int(input('Zadaj cislo '))
        z.sort_queue(x)
    elif volba==2:
        z.write_queue()
    elif volba==3:
        x=z.begin_queue()
        print('Vyradil som prvok ',x)
    elif volba==4:
        x=z.min_queue()
        if x is not None:
            print('Minimalna hodnota je ',x)
    elif volba==5:
        nazov=input('Zadaj nazov suboru ')
        f=open(nazov,'r')
        ret=f.read()
        pole=ret.split()
        f.close()
        for i in range(len(pole)):
            x=int(pole[i])
            z.sort_queue(x)
    else:
        print('Koniec programu...')
        break
            
        
