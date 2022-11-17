#Spajany zoznam - zasobnik
class Stack:
      class Vrchol:
            def __init__(self, data, next=None):
                  self.data=data
                  self.next=next
                  
      def __init__(self):
            self.zac=None

      def is_empty(self):       #kontrola ci je prazdny
            return self.zac is None
      
      def push(self,data):       #vlozi na vrchol nove data
            self.zac=self.Vrchol(data,self.zac)
            print('Vlozil som ',data)

      def pop(self):            #vyber prvku zo zaciatku
            if self.is_empty():
                  print('Zasobnik je prazdny pre operaciu pop...')
            else:
                  prvy=self.zac
                  self.zac=self.zac.next
                  print('Vybral som ',prvy.data)
                  return prvy.data

      def top(self):           #pozrie co je na vrchole
            if self.is_empty():
                  print('Zasobnik je prazdny pre operaciu top...')
                  return None
            else:
                  print('Na vrchole je ',self.zac.data)
                  return self.zac.data

      def write_out(self):     #vypis vsetkych prvkov zasobnika
            if self.is_empty==True:
                  print('Zasobnik je prazdny...')
            else:
                  print('Zoznam prvkov zasobnika:')
                  pom=self.zac
                  while pom is not None:
                        print(pom.data,end='->')
                        pom=pom.next
                  print('None')

      def del_duplicate(self):
            if self.is_empty==True:
                  print('Zasobnik je prazdny...')
            else:
                  pom=self.zac
                  #print(pom.data,end='->')
                  while (pom is not None):
                        #print(pom.data,end='->')
                        if (pom.next is not None) and (pom.data==pom.next.data):
                              pom=pom.next
                        else:
                              print(pom.data,end='->')
                              pom=pom.next
                                    
                  print('None')

      def file_stack(self):
            if self.is_empty==True:
                  print('Zasobnik je prazdny...')
            else:
                  nazov=input('Zadajte nazov suboru ')
                  f=open(nazov,'w')
                  pom=self.zac
                  while pom is not None:
                        print(pom.data,end='->',file=f)
                        pom=pom.next
                  print('None',file=f)
                  f.close()
                              
#Hlavny program cez menu
z=Stack()
while True:
      print()
      print('Vyber polozku z menu: ')
      print('Pridanie prvku na vrchol...........1')
      print('Vypis prvkov zasobnika.............2')
      print('Odobratie prvku z vrchola .........3')
      print('Vypis posledneho prvku.............4')
      print('Vymazanie opakujucich sa pismen....5')
      print('Zapis zasobnika do suboru..........6')
      print('Koniec programu....................0')
      volba=int(input())
      if volba==1:
            veta=input('Zadaj vety z pismen ')
            for i in range(len(veta)):
                  x=veta[i]
                  z.push(x)
      elif volba==2:
            z.write_out()
      elif volba==3:
            x=z.pop()
            print('Odobraty prvok je ',x)
      elif volba==4:
            x=z.top()
            print('Na vrchole je: ',x)
      elif volba==5:
            z.del_duplicate()
      elif volba==6:
            z.file_stack()
      else:
            print('Koniec programu...')
            break	

                  
            
