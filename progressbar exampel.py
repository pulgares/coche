import serial
import Tkinter as tk
from Tkinter import *
from time   import sleep
import ttk
import threading
#arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1.0)
root = Tk()


progressbar = ttk.Progressbar(root,orient=HORIZONTAL, maximum=300, mode='determinate')
#progressbar.pack(side="bottom")
#progressbar.start(50)
#progressbar=Scale(root, label="Servo1",  from_=0, to=255, orient=VERTICAL ,fg="White",length=200)
progressbar.place (x=0, y=20)
#progressbar.step(amount=line)
progressbar["maximum"]=256
progressbar["value"]=80


def sensor():
    var1=0;
    arr=[25,35,100,200];
    print("Fin init")
    while True:
        #line = arduino.readline()
        line="200"
        print("Linea:"+line)
        if(line !=""):
            print("Lectura")
            #w = Scale(root, label="Servo1",  from_=0, to=255, orient=VERTICAL ,fg="White",command=sensor,
            #length=200) #Creamos un dial para recoger datos numericos
            #w.grid(row=1, column=2)
            # progressbar = ttk.Progressbar(orient=HORIZONTAL, length=500, mode='determinate',variable=line)
            #progressbar.pack(side="bottom") print(var1)
            progressbar["maximum"]=256
            progressbar["value"]=(arr[var1])
            print("Escrito:")
            print(arr[var1])
            var1=var1+1
            var1=var1%4
            sleep(2)
        else:
            progressbar["value"]=0
            print("Fin no lectura")


#button6 = Button(root, text="Puertas",fg="blue", command=sensor)
#button6.grid(row=1, column=1)
#button6.config( height = 6, width = 20)
#button6.place (x=430, y=10)

t1=threading.Thread(target=sensor)
t1.start()


root.title('GUI de Leds')
root.geometry("800x600")

root.mainloop()
