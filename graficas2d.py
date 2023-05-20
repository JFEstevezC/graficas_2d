from tkinter import *
import tkinter as tk
import random 

# Variables Globales
BASE = 460
ALTURA = 220
RADIO = 50
# Función para modificar el arco
def modificar_arco(angulo):
    c.itemconfig(arco,extent=angulo)

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

# Arco
arco = c.create_arc(BASE/2-RADIO, ALTURA/2-RADIO, BASE/2+RADIO, ALTURA/2+RADIO, start=0, extent=0, fill="blue")

# frame controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg = "green", width=480, height=230)
frame_controles.place(x=10, y=260)

# barra de deslizamiento
barra_deslizamiento = Scale(frame_controles, label='Angulo', from_= 0, to=360, orient='horizontal', length=460, tickinterval=45, command=modificar_arco)
barra_deslizamiento.place(x=10, y=10)


'''''
#graficación
x = 10
y = 10
for i in range(10):
    circulo = c.create_oval(x,y, x+20, y + 20, fill="red")
    x = x + 30
    y = y + 30
    
for i in range(100):
    x = random.randint(0,BASE-20)
    y = random.randint(0,ALTURA-20)
    color = "#"
    for j in range(6):
        color = color + random.choice("0123456789ABCDEF")
    circulo = c.create_oval(x,y, x+20, y + 20, fill=color)
'''''

ventana_principal.mainloop()