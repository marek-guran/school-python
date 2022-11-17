#Binarny vyhladavaci strom - menu:pridat,vyhladat,vymazat,vypisat,vykreslit
import tkinter

class Strom:
    canvas=None
    
    class Vrchol:
        def __init__(self, data, left=None, right=None):
            self.data=data
            self.right=right
            self.left=left

        def __repr__(self):
            return repr(self.data)

    def __init__(self):
        self.root=None

    def push(self,data):
        if self.root is None:
            self.root=self.Vrchol(data)
        else:
            pom=self.root
            while pom.data != data:
                if pom.data > data:     #posuv dolava
                    if pom.left is not None:
                        pom=pom.left
                    else:
                        pom.left=self.Vrchol(data)
                else:                  #posuv doprava
                    if pom.right is None:
                        pom.right=self.Vrchol(data)
                    else:
                        pom=pom.right

    def preorder(self):
        def vypis(pom):
            if pom is None:
                return
            print(pom.data, end=' ')
            vypis(pom.left)
            vypis(pom.right)
        vypis(self.root)
        print()

    def inorder(self):
        def vypis(pom):
            if pom is None:
                return
            vypis(pom.left)
            print(pom.data,end=' ')
            vypis(pom.right)
        vypis(self.root)
        print()
            
    def search(self,data):
        pom=self.root
        while pom is not None:
            if pom.data == data:
                return True
            else:
                if data < pom.data:
                    pom=pom.left
                else:
                    pom=pom.right
        return False

    def draw(self):
        def draw_rek(vrch,sir,x,y):
            if vrch is None:
                return
            if vrch.left is not None:
                self.canvas.create_line(x, y, x-sir//2, y+40)
                draw_rek(vrch.left, sir//2, x-sir//2, y+40)
            if vrch.right is not None:
                self.canvas.create_line(x, y, x+sir//2, y+40)
                draw_rek(vrch.right, sir//2, x+sir//2, y+40)
            self.canvas.create_oval(x-15, y-15, x+15, y+15, fill='lightgray',outline='')
            self.canvas.create_text(x, y, text=vrch.data, font='consolas 12 bold')

        if self.canvas is None:
            Strom.canvas = tkinter.Canvas(bg='white', width=800,height=400)
            self.canvas.pack()
        self.canvas.delete('all')
        draw_rek(self.root, 380, 400, 40)
            
    def maxleft(self):
        pom=self.root
        pom=pom.left
        while pom.left is not None and pom.right is not None :
            if pom.left is not None and pom.right is not None:
                pom=pom.right
            elif pom.left is not None and pom.right is None:
                pom=pom.left
            elif pom.left is None and pom.right is not None:
                pom=pom.right
        return pom.data       
            
    def erase(self,data):
        pom=self.root
        pom2=self.root
        najdeny=False
        while pom is not None:
            if pom.data > data:
                pom2=pom
                pom=pom.left
            else:
                if pom.data<data:
                    pom2=pom
                    pom=pom.right
                else:
                    najdeny=True
                    break
                
        if najdeny == False:       #nasiel taky uzol
            return False
        else:
            if pom2 == pom and pom.left is None and pom.right is None: #zmazanie roota bez nasledovnikov
                self.root=None
                del pom,pom2
                return True
            if pom.left is None and pom.right is None:  #zmazanie listu
                if pom2.data > data:
                    pom2.left=None
                else:
                    pom2.right=None
                del pom,pom2
                return True
            if pom.left is not None and pom.right is None: #uzol s lavym nasledovnikom
                if pom2.data > data:
                    pom2.left=pom.left
                else:
                    pom2.right=pom.left
                del pom
                return True
            if pom.left is None and pom.right is not None: #uzol s pravym nasledovnikom
                if pom2.data > data:
                    pom2.left=pom.right
                else:
                    pom2.right=pom.right
                del pom
                return True
            if pom.left is not None and pom.right is not None: #uzol ma 2 nasleodvnikov
                pom3=pom2 
                pom2=pom.left
                while pom2.left is not None and pom2.right is not None :
                    if pom2.left is not None and pom2.right is not None:
                        pom3=pom2
                        pom2=pom2.right
                    elif pom2.left is not None and pom2.right is None:
                        pom3=pom2
                        pom2=pom2.left
                    elif pom2.left is None and pom2.right is not None:
                        pom3=pom2
                        pom2=pom2.right
                print('Nahradzam ',pom.data,' najvacsim z laveho podstromu',pom2.data)
                pom.data=pom2.data
                if pom3.data>pom2.data:
                    pom3.left=None
                    del pom2
                else:
                    pom3.right=None
                    del pom2
                return True    
            
#-----------------Hlavny program------------------------
s=Strom()
while True:
    print()
    print('Novy prvok do stromu..........1')
    print('Vypis stromu preorder.........2')
    print('Vypis stromu inorder..........3')
    print('Vykreslenie stromu............4')
    print('Vyhladanie prvku..............5')
    print('Zmazanie uzla.................6')
    print('Maximum z laveho podstromu....7')
    print('Koniec programu...............0')
    volba=int(input())
    if volba==1:
        x=int(input('Zadaj cislo '))
        s.push(x)
    elif volba==2:
        s.preorder()
    elif volba==3:
        s.inorder()
    elif volba==4:    
        s.draw()
        s.canvas.mainloop()
    elif volba==5:
        x=int(input('Zadaj hladane cislo '))
        if s.search(x):
            print('Hodnota ',x,' sa nachadza v strome...' )
        else:
            print('Hodnota ',x,' sa nenachadza v strome...' )
    elif volba==6:
        x=int(input('Zadaj cislo na zmazanie '))
        if s.erase(x) == True:
            print('Uzol s cislom ',x,' sa podarilo zmazat!')
        else:
            print('Uzol s cislom ',x,' sa nenachadzal v strome!')
    elif volba==7:
        print('Maximalny uzol zlava je ',s.maxleft())
    else:
        print('Koniec programu...')
        break
