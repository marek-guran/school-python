#Grafika - trojuholnik, stvorec
import tkinter

canvas = tkinter.Canvas(width=600,height=500)
canvas.pack()
#Trojuholnik
canvas.create_line(240,20,140,200,340,200,250,20)
canvas.create_line(120,210,70,297,170,297,120,210,width=10,fill='red')

#Obdlznik
canvas.create_rectangle(350,350,500,500,width=6,fill='cyan',outline='')

#Elipsa
canvas.create_oval(50,320,150,370,fill='blue')
canvas.create_oval(150,320,250,420,fill='green')

#Polygon
canvas.create_polygon(10,30,110,80,30,150,60,30,90,150,fill='pink')

#Pisanie textu
canvas.create_text(150,120,text='Polygon')
