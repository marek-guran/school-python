#Program na rad
class Queue:
      class Vrchol():
            def __init__(self,data,next=None):
                  self.data,self.next=data,next
            
      def __init__(self):    #inicializacia vnutornej reprezentacie
            self.zac=self.kon=None

      def is_empty(self):    #kontrola prazdnosti
            return self.zac is None

      def endqueue(self,data):  #na koniec vlozi hodnotu
            if self.zac is None:
                  self.zac=self.kon=self.Vrchol(data)
            else:
                  self.kon.next=self.Vrchol(data)
                  self.kon=self.kon.next

      def beginqueue(self):     #vyberie zo zaciatku prvu hodnotu
            if self.is_empty():
                  print('Fronta je prazdna...')
            else:
                  prvy=self.zac
                  self.zac=prvy.next
                  if self.zac is None:
                        self.kon=None
                  return prvy.data

            
      def front(self):    #vrati prvu hodnotu zo zaciatku radu
            if self.is_empty():
                  print('Fronta je prazdna...')
            else:
                  print('Na vrchole fronty je: ',self.zac.data)
                  return self.zac.data

z=Queue()            

            
            
