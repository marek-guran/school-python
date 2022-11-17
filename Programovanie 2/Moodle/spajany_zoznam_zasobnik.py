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

z=Stack()
for i in range (10):
	z.push(i)
k=z.top()
k=z.pop()
k=z.pop()
	
	

                  
            
            
            
