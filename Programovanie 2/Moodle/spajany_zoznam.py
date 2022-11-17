#Program na vytvorenie zoznamu
class Vrchol:
    def __init__(self, data,next=None):
        self.data, self.next=data,next

class Zoznam:
    def __init__(self, pole=None):
        self.zac=None
        if pole is not None:
            for prvok in pole:
                self.pridaj_kon(prvok)

    def __repr__(self):
        zoz=self.zac
        vysl=''
        while zoz is not None:
            vysl+=repr(zoz.data) + '->'
            zoz=zoz.next
        return '(' + vysl + ')'

    def __len__(self):
        zoz=self.zac
        vysl=0
        while zoz is not None:
            vysl+=1
            zoz=zoz.next
        return vysl

    def __contains__(self,data):
        zoz=self.zac
        while zoz is not None:
            if zoz.data == data:
                return True
            zoz=zoz.next
        return False

    def pridaj_zac(self,data):
        self.zac=Vrchol(data,self.zac)

    def pridaj_kon(self,data):
        if self.zac is None:
            self.zac=Vrchol(data)
        else:
            kon=self.zac
            while kon.next is not None:
                kon=kon.next
            kon.next=Vrchol(data)    
