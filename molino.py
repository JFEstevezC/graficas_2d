from tkinter import *
import tkinter as tk
import random 

# Variables Globales
BASE = 460
ALTURA = 220
RADIO = 50
# Función para modificar el arco
def modificar_arco(angulo):
    c.itemconfig(aspa1,start=int(angulo)+45)  
    c.itemconfig(aspa2,start=int(angulo)+135) 
    c.itemconfig(aspa3,start=int(angulo)+225)
    c.itemconfig(aspa4,start=int(angulo)+315)

ventana_principal = tk.Tk()
ventana_principal.title("GRÁFICAS 2D - Líneas Rectas")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")   
ventana_principal.config(bg = "white")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10, y=10)
c.config(bg="black")
# Base
triangulo = c.create_polygon(BASE*2/5,ALTURA, BASE/2, ALTURA/2, BASE*3/5, ALTURA, fill="red")


# Arco
aspa1 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=45, extent=45, fill="blue")
aspa2 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=135, extent=45, fill="yellow")
aspa3 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=225, extent=45, fill="orange")
aspa4 = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=315, extent=45, fill="green")

# frame controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg = "green", width=480, height=230)
frame_controles.place(x=10, y=260)

# barra de deslizamiento
barra_deslizamiento = Scale(frame_controles, label='Angulo', from_= 0, to=360, orient='horizontal', length=460, tickinterval=45, command=modificar_arco)
barra_deslizamiento.place(x=10, y=10)



ventana_principal.mainloop()