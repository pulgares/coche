#! /usr/bin/python

import serial
import Tkinter as tk
from Tkinter import *
from time   import sleep
import ttk
try:
    arduino = serial.Serial( 'COM7', 9600 )
except:
    print "Cannot conect to the port"


def EncenderLED1():
    arduino.write('e')
    print "luces on"
def ApagarLED1():
    arduino.write('a')
    print "luces off"

def Calefacion():
    def lift_win1():
	otra_ventana.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana = tk.Toplevel()
    otra_ventana.config(bg="black")
    otra_ventana.geometry("800x600")
    otra_ventana.title('Calefacion')

    button14 = tk.Button(otra_ventana, text="A/C ON",command=EncenderLED2)
    button14.place (x=10, y=10)
    button14.config( height = 6, width = 20 )
    root.iconify()

    button15 = tk.Button(otra_ventana, text="A/C OFF",command=ApagarLED2)
    button15.place (x=250, y=10)
    button15.config( height = 6, width = 20 )

    button15 = tk.Button(otra_ventana, text="Volver a menu",fg="White",command=lift_win1)
    button15.place (x=450, y=410)
    button15.config( height = 6, width = 20 )
    button15.config(bg="black")
def Luces():
    def lift_win1():
	otra_ventana1.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana1 = tk.Toplevel()
    otra_ventana1.config(bg="black")
    otra_ventana1.geometry("800x600")
    otra_ventana1.title('Luces')

    button16 = Button(otra_ventana1, text="Luces posicion ON",fg="red", command=EncenderLED1)
    button16.config( height = 6, width = 20 )
    button16.place (x=10, y=10)

    button17 = Button(otra_ventana1, text="Luces posicion OFF",fg="red", command=ApagarLED1)
    button17.place (x=250, y=10)
    button17.config( height = 6, width = 20 )

    button18 = tk.Button(otra_ventana1, text="Volver a menu",fg="White",command=lift_win1)
    button18.place (x=450, y=410)
    button18.config( height = 6, width = 20 )
    button18.config(bg="black")

    button5 = Button(otra_ventana1, text="Luz techo OFF", fg="yellow",command=ApagarLED2)
    button5.place (x=640, y=10)
    button5.config( height = 6, width = 20 )

    button8 = Button(otra_ventana1, text="Luz Cruze ON",fg="yellow", command=EncenderLED3)
#button8.grid(row=4, column=1)
    button8.place (x=10, y=150)
    button8.config( height = 6, width = 20 )
    button7 = Button(otra_ventana1, text="Luz cruze OFF",fg="blue", command=ApagarLED3)
#button7.grid(row=4, column=2)
    button7.config( height = 6, width = 20 )
    button7.place (x=220, y=150)
    button9 = Button(otra_ventana1, text="Luz espejo ON",fg="blue", command=EncenderLED4)
#button9.grid(row=5, column=1)
    button9.config( height = 6, width = 20 )
    button9.place (x=430, y=150)
    button10 = Button(otra_ventana1, text="Luz espejo OFF",fg="blue", command=ApagarLED4)
#button10.grid(row=5, column=2)
    button10.config( height = 6, width = 20 )
    button10.place (x=640, y=150)

    button12 = Button(otra_ventana1, text="Apagar todos", fg="blue", command=todosoff)
#button12.grid(row=6, column=2)
    button12.config( height = 6, width = 20 )
    button12.place (x=220, y=300)
    root.iconify()
def Puertas():
    def lift_win1():
	otra_ventana2.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana2 = tk.Toplevel()
    otra_ventana2.config(bg="black")
    otra_ventana2.geometry("800x600")
    otra_ventana2.title('Puertas')

    button6 = Button(otra_ventana2, image=imagen1,fg="blue", command=Flipflop)
    button6.config( height = 18, width = 20)
    button6.place (x=10, y=10)

    button21 = tk.Button(otra_ventana2, text="Volver a menu",fg="White", command=lift_win1)
    button21.place (x=450, y=410)
    button21.config( height = 6, width = 20 )
    button21.config(bg="black")
    root.iconify()
def Sensores():
    def lift_win1():
	otra_ventana3.withdraw() # Oculta la otra_ventana

	root.deiconify()


    otra_ventana3 = tk.Toplevel()
    otra_ventana3.config(bg="black")
    otra_ventana3.geometry("800x600")
    otra_ventana3.title('Sensores')

    w = Scale(otra_ventana3, label="Servo1",  from_=0, to=255, orient=VERTICAL ,fg="White",command=Servo1,
    length=200) #Creamos un dial para recoger datos numericos
    w.config(bg="black")
    w.place (x=50, y=10)
    w = Scale(otra_ventana3, label="Servo2", from_=0, to=255, orient=VERTICAL ,fg="White",command=Servo2,
    length=200) #Creamos un dial para recoger datos numericos
    w.config(bg="black")
    w.place (x=250, y=10)
    w = Scale(otra_ventana3, label="Servo3", from_=0, to=255, orient=VERTICAL ,fg="White",command=Servo3,
    length=200) #Creamos un dial para recoger datos numericos
    w.config(bg="black")
    w.place (x=550, y=10)

    button21 = tk.Button(otra_ventana3, text="Volver a menu",fg="White", command=lift_win1)
    button21.place (x=450, y=410)
    button21.config( height = 6, width = 20 )
    button21.config(bg="black")
    root.iconify()
def EncenderLED2():
    arduino.write('b')
    print "Se encendio el led 2"
def ApagarLED2():
    arduino.write('c')
    print "Se apago el led 2"

def EncenderLED3():
    arduino.write('d')
    print "Se encendio el led 3"
def ApagarLED3():
    arduino.write('f')
    print "Se apago el led 3"

def EncenderLED4():
    arduino.write('g')
    print "Se encendio el led 4"
def ApagarLED4():
    arduino.write('h')
    print "Se apago el led 4"

def todos():
    arduino.write('i')
    print "todos on"
def todosoff():
    arduino.write('j')
    print "todos off"

def Parpadeo():
    arduino.write('e')
    print "Se encendio el led 1"
    sleep(5)
    arduino.write('a')
    print "Se apago el led 1"
    sleep(5)
    arduino.write('e')
    print "Se encendio el led 1"
    sleep(5)
    arduino.write('a')
    print "Se apago el led 1"
    sleep(5)
    arduino.write('e')
    print "Se encendio el led 1"
    sleep(5)
    arduino.write('a')
    print "Se apago el led 1"
    sleep(5)



def Flipflop():
    arduino.write('e')
    print "Se encendio el led 1"
    sleep(1)
    arduino.write('a')
    print "Se apago el led 1"
    sleep(1)
    arduino.write('b')
    print "Se encendio el led 2"
    sleep(1)
    arduino.write('c')
    print "Se apago el led 2"
    sleep(1)

def Servo1(int):
    arduino.write('q')
    arduino.write(int)
    arduino.write('\n')
    print (int)

def Servo2(int):
    arduino.write('p')
    arduino.write(int)
    arduino.write('\n')
    print (int)

def Servo3(int):
    arduino.write('r')
    arduino.write(int)
    arduino.write('\n')
    print (int)

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print 'You selected item %d: "%s"' % (index, value)
    arduino = serial.Serial( value, 9600 )


root = Tk()
#root.config(bg="black")
imagenfondo=PhotoImage(file="car.gif")
imagen1=PhotoImage(file="flechaarriba.gif")
imagenluz=PhotoImage(file="luz.gif")
imagencalefacion=PhotoImage(file="calefacion.gif")
lblimagen=Label(root, image=imagenfondo).place(x=150, y=90)
#w = Scale(root, label="Servo1",  from_=0, to=255, orient=HORIZONTAL ,fg="blue",command=Servo1,
#length=200) #Creamos un dial para recoger datos numericos
#w.grid(row=7,column=1)
#w.place (x=50, y=510)
#w = Scale(root, label="Servo2", from_=0, to=255, orient=HORIZONTAL ,fg="blue",command=Servo2,
#length=200) #Creamos un dial para recoger datos numericos
#w.grid(row=10,column=1)
#w.place (x=300, y=510)
#w = Scale(root, label="Servo3", from_=0, to=255, orient=HORIZONTAL ,fg="blue",command=Servo3,
#length=200) #Creamos un dial para recoger datos numericos
#w.place (x=550, y=510)


button3 = Button(root, text="Parpadeo",fg="blue", command=Parpadeo)
#button3.grid(row=1, column=2)
button3.config( height = 3, width = 11 )

button4 = Button(root, image=imagenluz, fg="blue", command=Luces)
button4.place (x=10, y=10)
button4.config(  height = 96, width = 96  )



button6 = Button(root, text="Puertas",fg="blue", command=Puertas)
#button6.grid(row=1, column=1)
button6.config( height = 6, width = 20)
button6.place (x=430, y=10)
button11 = Button(root, text="Sensores",fg="blue", command=Sensores)
#button11.grid(row=6, column=1)
button11.config( height = 6, width = 20 )
button11.place (x=640, y=10)

button13 = Button(root, image=imagencalefacion, fg="blue", command=Calefacion)
#button13.grid(row=12, column=2)
button13.config( height = 96, width = 96 )
button13.place (x=220, y=10)


root.title('GUI de Leds')
root.geometry("800x600")

root.mainloop()