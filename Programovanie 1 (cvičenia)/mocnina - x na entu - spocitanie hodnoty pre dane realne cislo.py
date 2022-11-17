#pocitanie x na entu pre dane realne cislo
x=int(input('Zadajte cislo:'))
n=int(input('Zadajte na kolkatu je to cislo:'))
def exponent(x,n):
    z=1
    for i in range(n):
        z=z*x
    return(z)
