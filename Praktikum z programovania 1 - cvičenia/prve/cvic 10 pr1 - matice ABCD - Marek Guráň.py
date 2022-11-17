#Cvicenie 10, priklad 1, Marek Guráň
import random
ma=[]
mb=[]
mc=[]

def vytvor_maticu_A():

    r=5
    for i in range(r):
        temp=[]
        for j in range(r):
            x=random.randint(1,9)
            temp.append(x)
        ma.append(temp)
    return ma

def vypis_matice_A(ma):
    print('Vypis matice A:')
    for i in range(len(ma)):
        for j in range(len(ma[i])):
            print(ma[i][j],end=' ')
        print()
    print()

def vytvor_maticu_B():

    r=5
    for i in range(r):
        temp=[]
        for j in range(r):
            x=random.randint(1,9)
            temp.append(x)
        mb.append(temp)
    return mb

def vypis_matice_B(mb):
    print('Vypis matice B:')
    for i in range(len(mb)):
        for j in range(len(mb[i])):
            print(mb[i][j],end=' ')
        print()
    print()

def scitanie_matic_C(ma,mb):
    print('Scitanie matic C:')
    temp=[]
    for i in range(len(ma)):
        mc=0
        for j in range (len(mb)):
            sucet=ma[i][j] + mb [i][j]
            print(sucet, end=' ')
        print()
    print('\n')

def odcitanie_matic_D(ma,mb):
    print('Odcitanie matic D:')
    temp=[]
    for i in range(len(ma)):
        md=0
        for j in range (len(mb)):
            odcitanie=ma[i][j] - mb [i][j]
            print(odcitanie, end=' ')
        print()

vytvor_maticu_A()
vytvor_maticu_B()
vypis_matice_A(ma)
vypis_matice_B(mb)
scitanie_matic_C(ma,mb)
odcitanie_matic_D(ma,mb)



                             
