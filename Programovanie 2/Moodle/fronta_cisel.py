#Fronta celych cisel
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

    def endqueue(self,data):   #pridanie prvku na koniec
        if self.zac is None:
            self.zac=self.kon=self.Vrchol(data)
        else:
            self.kon.next=self.Vrchol(data)
            self.kon=self.kon.next

    def beginqueue(self):
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
            
    def min_queue(self):
        if self.is_empty():
            print('Fronta je prazdna...')
        else:
            pom=self.zac
            minimum=pom.data
            while pom is not None:
                if pom.data<minimum:
                    minimum=pom.data
                pom=pom.next
        return minimum
    
#Hlavny program
z=Queue()
while True:
    print()
    print('Pridanie prvku na koniec...........1')
    print('Vypis prvkov fronty................2')
    print('Odobratie prvku zo zaciatku........3')
    print('Najdenie minimalneho prvku.........4')
    print('Koniec programu....................0')
    volba=int(input())
    if volba==1:
        x=int(input('Zadaj cislo '))
        z.endqueue(x)
    elif volba==2:
        z.write_queue()
    elif volba==3:
        x=z.beginqueue()
        print('Vyradil som prvok ',x)
    elif volba==4:
        x=z.min_queue()
        if x is not None:
            print('Minimalna hodnota je ',x)       
    else:
        print('Koniec programu...')
        break
            
        
