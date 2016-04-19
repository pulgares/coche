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
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
def Radio():
    def lift_win1():
	otra_ventana4.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana4 = tk.Toplevel()
    otra_ventana4.config(bg="black")
    otra_ventana4.geometry("800x420")
    otra_ventana4.title('Calefacion')

    buttonr1 = tk.Button(otra_ventana4, text="A/C ON",command=ACon)
    buttonr1.place (x=10, y=10)
    buttonr1.config( height = 6, width = 20 )
    root.iconify()

    buttonr2 = tk.Button(otra_ventana4, text="A/C OFF",command=ACoff)
    buttonr2.place (x=250, y=10)
    buttonr2.config( height = 6, width = 20 )

    buttonr3 = tk.Button(otra_ventana4, text="frente",command=ACoff)
    buttonr3.place (x=10, y=300)
    buttonr3.config( height = 6, width = 20 )

    buttonr4 = tk.Button(otra_ventana4, text="piesfrente",command=ACoff)
    buttonr4.place (x=90, y=200)
    buttonr4.config( height = 6, width = 20 )

    buttonr5 = tk.Button(otra_ventana4, text="pies",command=ACoff)
    buttonr5.place (x=220, y=120)
    buttonr5.config( height = 6, width = 20 )

    buttonr13 = tk.Button(otra_ventana4, image=imagenatras,fg="White",command=lift_win1)
    buttonr13.place (x=410, y=300)
    buttonr13.config( height = 96, width = 96 )
    buttonr13.config(bg="black")



def subefrecuencia():
    arduino.write('b')
    print "ACon"
def bajafrecuencia():
    arduino.write('c')
    print "ACoff"


#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

def Calefacion():
    def lift_win1():
	otra_ventana.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana = tk.Toplevel()
    otra_ventana.config(bg="black")
    otra_ventana.geometry("800x420")
    otra_ventana.title('Calefacion')

    buttonc1 = tk.Button(otra_ventana, text="A/C ON",command=ACon)
    buttonc1.place (x=10, y=10)
    buttonc1.config( height = 6, width = 20 )
    root.iconify()

    buttonc2 = tk.Button(otra_ventana, text="A/C OFF",command=ACoff)
    buttonc2.place (x=250, y=10)
    buttonc2.config( height = 6, width = 20 )

    buttonc3 = tk.Button(otra_ventana, text="frente",command=ACoff)
    buttonc3.place (x=10, y=300)
    buttonc3.config( height = 6, width = 20 )

    buttonc4 = tk.Button(otra_ventana, text="piesfrente",command=ACoff)
    buttonc4.place (x=90, y=200)
    buttonc4.config( height = 6, width = 20 )

    buttonc5 = tk.Button(otra_ventana, text="pies",command=ACoff)
    buttonc5.place (x=220, y=120)
    buttonc5.config( height = 6, width = 20 )

    buttonc13 = tk.Button(otra_ventana, image=imagenatras,fg="White",command=lift_win1)
    buttonc13.place (x=410, y=300)
    buttonc13.config( height = 96, width = 96 )
    buttonc13.config(bg="black")

    w = Scale(otra_ventana, label="Temp",  from_=0, to=500, orient=HORIZONTAL ,fg="White",command=Temp,
    length=200) #Creamos un dial para recoger datos numericos
    w.config(bg="black")
    w.place (x=450, y=10)

    w = Scale(otra_ventana, label="Caudal", from_=0, to=500, orient=HORIZONTAL ,fg="White",command=caudal,
    length=200) #Creamos un dial para recoger datos numericos
    w.config(bg="black")
    w.place (x=450, y=120)

def ACon():
    arduino.write('b')
    print "ACon"
def ACoff():
    arduino.write('c')
    print "ACoff"
def Temp():
    arduino.write(int)
def caudal():
    arduino.write(int)

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
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
    button5 = Button(otra_ventana1, text="Luces posicion ON",fg="blue", command=Luzposicionon)
    button5.config( height = 6, width = 20 )
    button5.place (x=10, y=10)                                                                          # pin arduino 6

    button6 = Button(otra_ventana1, text="Luces posicion OFF",fg="blue", command=Luzposicionoff)
    button6.place (x=220, y=10)
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
    button10.place (x=430, y=10)
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

    root.iconify()
#-----------------------------------------------------------------------------------------------------
def Luzposicionon():
    arduino.write('b')
    print "Posicion on"
def Luzposicionoff():           # pin arduino 6
    arduino.write('a')
    print "Posicion off"
def todos():
    arduino.write('i')
    print "todos on"

def Luzespejoon():
    arduino.write('g')
    print "LuzespejoON"         #Pin arduino 8
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
def Luztechooff():          # pin arduino 5
    arduino.write('f')
    print "Luztecho on"
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
def Puertas():
    def lift_win1():
	otra_ventana2.withdraw() # Oculta la otra_ventana

	root.deiconify()

    otra_ventana2 = tk.Toplevel()
    otra_ventana2.config(bg="black")
    otra_ventana2.geometry("800x420")
    otra_ventana2.title('Puertas')

    buttonP1 = Button(otra_ventana2, image=imagenarriba,fg="White", command=VenDISube)#Ventanilla delantera izquierda sube
    buttonP1.config( height = 96, width = 96)
    buttonP1.place (x=10, y=5)

    buttonP2 = Button(otra_ventana2, image=imagenabajo,fg="White", command=VenDIBaja)#Ventanilla delantera izquierda baja
    buttonP2.config( height = 96, width = 96)
    buttonP2.place (x=10, y=109)

    buttonP3 = Button(otra_ventana2, image=imagenarriba,fg="White", command=VenDDSube)#Ventanilla delantera derecha sube
    buttonP3.config( height = 96, width = 96)
    buttonP3.place (x=690, y=5)

    buttonP4 = Button(otra_ventana2, image=imagenabajo,fg="White", command=VenDDBaja)#Ventanilla delantera derecha baja
    buttonP4.config( height = 96, width = 96)
    buttonP4.place (x=690, y=109)

    buttonP5 = Button(otra_ventana2, image=imagenarriba,fg="White", command=VenTISube)#Ventanilla trasera izquierda sube
    buttonP5.config( height = 96, width = 96)
    buttonP5.place (x=120, y=210)

    buttonP6 = Button(otra_ventana2, image=imagenabajo,fg="White", command=VenTIBaja)#Ventanilla trasera izquierda baja
    buttonP6.config( height = 96, width = 96)
    buttonP6.place (x=120, y=315)

    buttonP7 = Button(otra_ventana2, image=imagenarriba,fg="White", command=VenTDSube)#Ventanilla trasera derecha sube
    buttonP7.config( height = 96, width = 96)
    buttonP7.place (x=590, y=210)

    buttonP8 = Button(otra_ventana2, image=imagenabajo,fg="White", command=VenTDBaja)#Ventanilla trasera derecha baja
    buttonP8.config( height = 96, width = 96)
    buttonP8.place (x=590, y=315)

    buttonP9 = Button(otra_ventana2, image=imagenbloqueopuerta,fg="White", command=BloqueoON)#bloqueo de puerta ON
    buttonP9.config( height = 96, width = 96)
    buttonP9.place (x=280, y=5)

    buttonP10 = Button(otra_ventana2, image=imagendesbloqueopuerta,fg="White", command=BloqueoOFF)#bloqueo de puerta Off
    buttonP10.config( height = 96, width = 96)
    buttonP10.place (x=280, y=109)

    buttonP11 = Button(otra_ventana2, image=imagenwindow1,fg="White", command=BloqueoONw)#bloqueo de ventana ON
    buttonP11.config( height = 96, width = 96)
    buttonP11.place (x=430, y=5)

    buttonP12 = Button(otra_ventana2, image=imagenwindow2,fg="White", command=BloqueoOFFW)#bloqueo de ventana Off
    buttonP12.config( height = 96, width = 96)
    buttonP12.place (x=430, y=109)


    buttonP13 = tk.Button(otra_ventana2, image=imagenatras,fg="White", command=lift_win1)
    buttonP13.place (x=350, y=300)
    buttonP13.config( height = 96, width = 96 )
    buttonP13.config(bg="black")

    buttonp14 = Button(otra_ventana2, text="OFF", fg="blue", command=todosoff)
    #button12.grid(row=6, column=2)
    buttonp14.config( height = 5, width = 7 )
    buttonp14.place (x=260, y=300)

    root.iconify()

def todosoff():
    arduino.write('k')
    print "todos off"

def VenDISube():#Ventanilla delantera izquierda sube
    arduino.write('i')
    print "Sube ventanilla del izq"
def VenDIBaja():#Ventanilla delantera izquierda baja
    arduino.write('j')
    print "Baja ventanilla del izq"

def VenDDSube():#Ventanilla delantera izquierda sube
    arduino.write('p')
    print "Sube ventanilla del der"
def VenDDBaja():#Ventanilla delantera izquierda baja
    arduino.write('q')
    print "Baja ventanilla del de"

def VenTISube():#Ventanilla delantera izquierda sube
    arduino.write('r')
    print "Sube ventanilla tras izq"
def VenTIBaja():#Ventanilla delantera izquierda baja
    arduino.write('s')
    print "Baja ventanilla tras izq"

def VenTDSube():#Ventanilla delantera izquierda sube
    arduino.write('t')
    print "Sube ventanilla tras der"
def VenTDBaja():#Ventanilla delantera izquierda baja
    arduino.write('u')
    print "Baja ventanilla trras der"
def BloqueoON():#bloque de puertas ON
    arduino.write('v')
    print "bloquea puerta"
def BloqueoOFF():#bloque de puertas Off
    arduino.write('w')
    print "desbloquea puertas"
def BloqueoONw():#bloque de puertas ON
    arduino.write('X')
    print "bloquea puerta"
def BloqueoOFFW():#bloque de puertas Off
    arduino.write('Y')
    print "desbloquea puertas"

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
def Sensores():
    def lift_win1():
	otra_ventana3.withdraw() # Oculta la otra_ventana

	root.deiconify()


    otra_ventana3 = tk.Toplevel()
    otra_ventana3.config(bg="grey")
    otra_ventana3.geometry("800x420")
    otra_ventana3.title('Sensores')
   # lblimagen=Label(otra_ventana3, image=imagenfondo).place(x=150, y=0)


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

def Servo1(int):
    arduino.write('q')#esta letra no vale
    arduino.write(int)
    arduino.write('\n')
    print (int)

def Servo2(int):
    arduino.write('p')#esta letra no vale
    arduino.write(int)
    arduino.write('\n')
    print (int)

def Servo3(int):
    arduino.write('r')#esta letra no vale
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

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH








def arrancar():
    arduino.write('o')
    print "arrancar"

root = Tk()
#root.config(bg="black")
imagenfondo=PhotoImage(file="car.gif")
imagenradio=PhotoImage(file="fichiers_mp3.gif")
imagenwindow1=PhotoImage(file="Window.gif")
imagenwindow2=PhotoImage(file="Window_close.gif")
imagenarriba=PhotoImage(file="arriba.gif")
imagenabajo=PhotoImage(file="abajo.gif")
imagenatras=PhotoImage(file="izquierda.gif")
imagenluz=PhotoImage(file="luz.gif")
imagenpuerta=PhotoImage(file="puerta.gif")
imagencalefacion=PhotoImage(file="calefacion.gif")
imagensensor=PhotoImage(file="sensor.gif")
imagenbloqueopuerta=PhotoImage(file="Close.gif")
imagendesbloqueopuerta=PhotoImage(file="Open.gif")
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


button17 = Button(root, text="nada",fg="blue", command=Luces)
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
button22.place (x=10, y=150)

button23 = Button(root, image=imagenradio, fg="blue", command=Radio)
#button13.grid(row=12, column=2)
button23.config( height = 96, width = 96 )
button23.place (x=10, y=300)

cerrar = Button(root,image=imagencerrar, command=root.destroy)
cerrar.config( height = 96, width = 96 )
cerrar.place (x=700, y=200)
#Button31.pack()

root.title('GUI de Leds')
root.geometry("800x420")

root.mainloop()