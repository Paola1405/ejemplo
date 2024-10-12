import tkinter as GUI
import serial 
import time 



window = GUI.Tk()
PUERTO= "COM3"
arduino = serial.Serial(port='PUERTO', baudrate=115200, timeout=.1) 


def CONECTAR():
    global PUERTO
    print("funcion conectar")
    PUERTO= EntryCOM.get()

    
def SEND():
    global PUERTO
    print("Funcion de datos")
    x= SpinDATA.get()
    arduino.write(bytes(x, 'utf-8')) 
    time.sleep(0.05) 
    data = arduino.readline() 
    LabelRECIVE.config(text=f'dato recibido = {data}')
    
     data = utf-8(arduino.readline()) 
    LabelRECIVE.config(text="dato recibido"+{data})
    
def CERRAR():
    print("cerrar")
    arduino.close()
    window.destroy()


#instancia de los objetos
LabelCOM_NAME= GUI.Label(window,text="escribe el nombre del puerto; ejempo: COM2")
EntryCOM= GUI.Entry(window)
BotonCONECT=GUI.Button(window,text="CONECTAR",
                       command=CONECTAR())
SpinDATA=GUI.Spinbox(window,from_=0, to=100)
BotonSEND=GUI.Button(window, text= "ENVIAR",
                     command=SEND())
LabelRECIVE= GUI.Label(window, text= "Dato recibido=")
BotonCerrar = GUI.Button(window, tect="SALIR", command=CERRAR())

#incrustacion en VENTANA
LabelCOM_NAME.pack(padx=1, pady=2)
EntryCOM.pack(padx=1, pady=2)
BotonCONECT.pack(padx=1, pady=2)
SpinDATA.pack(padx=1, pady=2)
BotonSEND.pack(padx=1, pady=2)
LabelRECIVE.pack(padx=1, pady=2)
BotonCerrar.pack(padx=1, pady=2)











window. mainloop()