#Binarny vyhladavaci strom - telefonny zoznam
import tkinter

class Strom:
    canvas=None
    
    class Vrchol:
        def __init__(self, meno, telefon, left=None, right=None):
            self.meno=meno
            self.telefon=telefon
            self.right=right
            self.left=left

        def __repr__(self):
            return repr(self.meno,self.telefon)

    def __init__(self):
        self.root=None

    def pocet(vrch):
        if vrch is None:
            return 0
        return 1+pocet(vrch.left)+pocet(vrch.right)

    def push(self,meno,telefon):
        if self.root is None:
            self.root=self.Vrchol(meno,telefon)
        else:
            najdeny=False
            pom=self.root
            while pom is not None:
                if pom.meno == meno:
                    najdeny=True
                    break
                if pom.meno > meno:
                    pom=pom.left
                else:
                    pom=pom.right
            if najdeny == False:
                pom=self.root
                while pom.meno != meno:
                    if pom.meno > meno:     #posuv dolava
                        if pom.left is not None:
                            pom=pom.left
                        else:
                            pom.left=self.Vrchol(meno,telefon)
                    else:                  #posuv doprava
                        if pom.right is None:
                            pom.right=self.Vrchol(meno,telefon)
                        else:
                            pom=pom.right

    def inorder(self):
        print('{:<20}| {:<15}'.format('Meno','Telefon'))
        print('-----------------------------------') 
        def vypis(pom):
            if pom is None:
                return
            vypis(pom.left)
            print('{:<20}| {:<15}'.format(pom.meno,pom.telefon))
            vypis(pom.right)
        vypis(self.root)
        print()
            
    def search(self,meno):
        pom=self.root
        while pom is not None:
            if pom.meno == meno:
                return pom.telefon
            else:
                if meno < pom.meno:
                    pom=pom.left
                else:
                    pom=pom.right
        return 0

    def pop(self):
        return self.meno,self.telefon
            
    def erase(self,data):
        pass
        
#-----------------Hlavny program------------------------
s=Strom()

while True:
    print()
    print('Novy ucastnik zoznamu.........1')
    print('Vypis telefonneho zoznamu.....2')
    print('Vyhladanie podla mena.........3')
    print('Koniec programu...............0')
    volba=int(input())
    if volba==1:
        ret1=input('Zadajte priezvisko a meno ')
        ret2=input('Zadajte telefonne cislo ')
        s.push(ret1,ret2)
    elif volba==2:
        s.inorder()
    elif volba==3:
        ret=input('Zadaj meno ')
        if s.search(ret) != 0:
            print('{:<20}| {:<15}'.format('Meno','Telefon'))
            print('-----------------------------------')                     
            print('{:<20}| {:<15}'.format(ret,s.search(ret)))
        else:
            print('Meno ',ret,' sa nenachadza v zozname...' )
                
    else:
        print('Koniec programu...')
        break
