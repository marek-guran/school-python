import tkinter
from random import *
canvas = tkinter.Canvas(width=600, height=400, bg='white')


def kruzok():
    global y
    global x
    canvas.delete('all')
    y = y + 10
    if y > 400:
        y = 10
        x = randrange(590)
    canvas.create_oval(x-v, y-v, x+v, y+v)
    if pokracovat == 1:
        canvas.after(10, kruzok)    

def klik(suradnice):
    global x, y
    x = suradnice.x
    y = suradnice.y

def start_stop():
    global pokracovat
    global v
    v = int(entry1.get())
    if pokracovat == 1:
        pokracovat = 0
    else:
        pokracovat = 1
        kruzok()

y = 10
x = 50
pokracovat = 0
v = 5
canvas.bind('<Button-1>', klik)
tlacidlo1 = tkinter.Button(text='start/stop', command=start_stop)
tlacidlo1.pack()
label1 = tkinter.Label(text='zadaj polomer lopticky:')
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()
canvas.pack()
