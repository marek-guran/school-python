# program na vytvorenie stromu s pismenami angl. abecedy a pocetnostou vyskytou
class Strom:
    class Vrchol:
        def __init__(self,data,left=None,right=None,pocet=1):
            self.data=data
            self.left=left
            self.right=right
            self.pocet=pocet
        def __repr__(self):
            return repr(self.data)

    def __init__(self):
        self.root=None

    def preorder(self):
        def vypis(v):
            if v is None:
                return
            print(v.data,":",v.pocet,end="  ")
            vypis(v.left)
            vypis(v.right)
        vypis(self.root)
        print ()

    def inorder (self):
        def vypis(v):
            if v is None:
                return
            vypis(v.left)
            print(v.data,":",v.pocet,end="  ")
            vypis(v.right)
        vypis(self.root)
        print ()

    def vkladanie(self,data):
        if self.root is None:
            self.root=self.Vrchol(data)
        else:
            pom=self.root
            n=False
            while pom is not None:
                if pom.data==data:
                    pom.pocet=pom.pocet+1
                    n=True
                    break
                if pom.data>data:
                    if pom.left is not None:
                        pom=pom.left
                    else:
                        pom.left=self.Vrchol(data)
                else:
                    if pom.right is not None:
                        pom=pom.right
                    else:
                        pom.right=self.Vrchol(data)
    def najdi(self,data):
        pom=self.root
        n=False
        while pom is not None:
            if pom.data==data:
                n=True
            if pom.data>data:
                pom=pom.left
            else:
                pom=pom.right
        return n

#Hlavny program
s=Strom()
while True:
    print()
    print('Pridanie prvkov.....1')
    print('Vypis preorder......2')
    print('Vypis inorder.......3')
    print('Nájdenie prvku......4')
    print('Koniec..............0')
    volba=int(input())
    if volba==1:
        ret=input('Zadajte vetu ')
        for i in range(len(ret)):
            if ret[i].isalpha():
                s.vkladanie(ret[i])
    elif volba==2:
        s.preorder()
    elif volba==3:
        s.inorder()
    elif volba==4:
        x=input('Zadaj znak ')
        if s.najdi(x) == True:
            print(x,' sa nachádza v strome.')
        else:
            print(x,' sa nenachádza v strome.')
    else:
        print('Koniec programu')
        break
              
        

                    






        
        
