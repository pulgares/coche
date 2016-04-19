#!/usr/bin/env python
import serial
import Tkinter as tk
from Tkinter import *
from time   import sleep
import ttk
try:
    arduino = serial.Serial( 'COM7', 9600 )
except:
    print "Cannot conect to the port"


def Luzposicionon():
    arduino.write('b')
    print "Posicion on"
def Luzposicionoff():           # pin arduino 6
    arduino.write('a')
    print "Posicion off"

def Calefacion():
    def lift_win1():
	otra_ventana.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana = tk.Toplevel()
    otra_ventana.config(bg="black")
    otra_ventana.geometry("800x420")
    otra_ventana.title('Calefacion')

    button1 = tk.Button(otra_ventana, text="A/C ON",command=ACon)
    button1.place (x=10, y=10)
    button1.config( height = 6, width = 20 )
    root.iconify()

    button2 = tk.Button(otra_ventana, text="A/C OFF",command=ACoff)
    button2.place (x=250, y=10)
    button2.config( height = 6, width = 20 )

    button3 = tk.Button(otra_ventana, image=imagenatras,fg="White",command=lift_win1)
    button3.place (x=410, y=300)
    button3.config( height = 96, width = 96 )
    button3.config(bg="black")

def ACon():
    arduino.write('b')
    print "ACon"
def ACoff():
    arduino.write('c')
    print "ACoff"
#------------------------------------------------------------------------------------------
def Luces():
    def lift_win1():
	otra_ventana1.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana1 = tk.Toplevel()
    otra_ventana1.config(bg="black")
    otra_ventana1.geometry("800x420")
    otra_ventana1.title('Luces')
#------------------------------------------------------------------------------------------------
    button4 = tk.Button(otra_ventana1, image=imagenatras,fg="White",command=lift_win1)
    button4.place (x=410, y=300)
    button4.config( height = 96, width = 96 )
    button4.config(bg="black")

#----------------------------------------------------------------------------------------------------
    button5 = Button(otra_ventana1, text="Luces posicion ON",fg="red", command=Luzposicionon)
    button5.config( height = 6, width = 20 )
    button5.place (x=10, y=10)                                                                          # pin arduino 6

    button6 = Button(otra_ventana1, text="Luces posicion OFF",fg="red", command=Luzposicionoff)
    button6.place (x=250, y=10)
    button6.config( height = 6, width = 20 )
#--------------------------------------------------------------------------------------------------
    button7 = Button(otra_ventana1, text="Luz Cruze ON",fg="blue", command=Luzcruceon)
#button8.grid(row=4, column=1)
    button7.place (x=10, y=150)                                                                         #pin arduino 7
    button7.config( height = 6, width = 20 )
    button8 = Button(otra_ventana1, text="Luz cruze OFF",fg="blue", command=Luzcruceoff)
#button7.grid(row=4, column=2)
    button8.config( height = 6, width = 20 )
    button8.place (x=220, y=150)
#------------------------------------------------------------------------------------------------------

    button9 = Button(otra_ventana1, text="Luz techo OFF", fg="blue",command=Luztechooff)
    button9.place (x=640, y=10)
    button9.config( height = 6, width = 20 )                                                                #pin arduino 5
    button10 = Button(otra_ventana1, text="Luz techo ON", fg="blue",command=Luztecho)
    button10.place (x=440, y=10)
    button10.config( height = 6, width = 20 )
#------------------------------------------------------------------------------------------------------

    button11 = Button(otra_ventana1, text="Luz espejo ON",fg="blue", command=Luzespejoon)
#button9.grid(row=5, column=1)
    button11.config( height = 6, width = 20 )                                                           #pin arduino 8
    button11.place (x=430, y=150)
    button12 = Button(otra_ventana1, text="Luz espejo OFF",fg="blue", command=Luzespejooff)
#button10.grid(row=5, column=2)
    button12.config( height = 6, width = 20 )
    button12.place (x=640, y=150)
#-------------------------------------------------------------------------------------------------
    button13 = Button(otra_ventana1, text="Apagar todos", fg="blue", command=todosoff)
#button12.grid(row=6, column=2)
    button13.config( height = 6, width = 20 )
    button13.place (x=220, y=300)
    root.iconify()
#-----------------------------------------------------------------------------------------------------
def todos():
    arduino.write('i')
    print "todos on"
def todosoff():
    arduino.write('l')
    print "todos off"
def Luzespejoon():
    arduino.write('g')
    print "LuzespejoON"
def Luzespejooff():
    arduino.write('h')
    print "LuzespejoOFF"

def Luzcruceon():
    arduino.write('d')
    print "Cruce on"         #pin arduino 7
def Luzcruceoff():
    arduino.write('c')
    print "Cruce off"

def Luztecho():
    arduino.write('e')
    print "Luztecho on"
def Luztechooff():
    arduino.write('f')
    print "Luztecho on"
#---------------------------------------------------------------------------------------
def Puertas():
    def lift_win1():
	otra_ventana2.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana2 = tk.Toplevel()
    otra_ventana2.config(bg="black")
    otra_ventana2.geometry("800x420")
    otra_ventana2.title('Puertas')

    button14 = Button(otra_ventana2, image=imagen1,fg="blue", command=Flipflop)
    button14.config( height = 18, width = 20)
    button14.place (x=10, y=10)

    button15 = tk.Button(otra_ventana2, image=imagenatras,fg="White", command=lift_win1)
    button15.place (x=410, y=300)
    button15.config( height = 96, width = 96 )
    button15.config(bg="black")
    root.iconify()
def Sensores():
    def lift_win1():
	otra_ventana3.withdraw() # Oculta la otra_ventana

	root.deiconify()


    otra_ventana3 = tk.Toplevel()
    otra_ventana3.config(bg="black")
    otra_ventana3.geometry("800x420")
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

    button16 = tk.Button(otra_ventana3, image=imagenatras, fg="White", command=lift_win1)
    button16.place (x=410, y=300)
    button16.config( height = 96, width = 96 )
    button16.config(bg="black")
    root.iconify()








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
def arrancar():
    arduino.write('o')
    print "arrancar"

root = Tk()
#root.config(bg="black")
imagenfondo=PhotoImage(file="car.gif")
imagen1=PhotoImage(file="flechaarriba.gif")
imagenatras=PhotoImage(file="izquierda.gif")
imagenluz=PhotoImage(file="luz.gif")
imagenpuerta=PhotoImage(file="puerta.gif")
imagencalefacion=PhotoImage(file="calefacion.gif")
imagensensor=PhotoImage(file="sensor.gif")
imagencontacto=PhotoImage(file="contacto.gif")
imagencerrar=PhotoImage(file="radioactive.gif")
lblimagen=Label(root, image=imagenfondo).place(x=150, y=0)
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


button17 = Button(root, text="Parpadeo",fg="blue", command=Parpadeo)
#button3.grid(row=1, column=2)
button17.config( height = 3, width = 11 )

button18 = Button(root, image=imagenluz, fg="blue", command=Luces)
button18.place (x=10, y=10)
button18.config(  height = 96, width = 96  )



button19 = Button(root, image=imagenpuerta,fg="blue", command=Puertas)
#button6 grid(row=1, column=1)
button19.config( height = 96, width = 96)
button19.place (x=570, y=10)
button20 = Button(root, image=imagensensor,fg="blue", command=Sensores)
#button11.grid(row=6, column=1)
button20.config( height = 96, width = 96 )
button20.place (x=700, y=10)

button21 = Button(root, image=imagencalefacion, fg="blue", command=Calefacion)
#button13.grid(row=12, column=2)
button21.config( height = 96, width = 96 )
button21.place (x=140, y=10)

button22 = Button(root, image=imagencontacto, fg="blue", command=arrancar)
#button13.grid(row=12, column=2)
button22.config( height = 96, width = 96 )
button22.place (x=10, y=200)


cerrar = Button(root,image=imagencerrar, command=root.destroy)
cerrar.config( height = 96, width = 96 )
cerrar.place (x=700, y=200)
#Button31.pack()

root.title('GUI de Leds')
root.geometry("800x420")

root.mainloop()