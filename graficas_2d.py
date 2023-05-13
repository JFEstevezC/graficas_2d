from tkinter import *
import tkinter as tk

# Variables Globales
BASE = 460
ALTURA = 220

ventana_principal = tk.Tk()
ventana_principal.title("GRÁFICAS 2D - Líneas Rectas")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")   
ventana_principal.config(bg = "black")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=240)
frame_graficacion.place(x=10, y=10)

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10, y=10)
c.config(bg="yellow")

# Líneas
# linea1 = c.create_line(10,10, BASE-10, 10, fill="red")

# linea2 = c.create_line(BASE-10,10, BASE-10, ALTURA-10, fill="red")

# linea3 = c.create_line(BASE-10,ALTURA-10, 10, ALTURA-10, fill="red")

# linea4 = c.create_line(10,ALTURA-10, 10,10, fill="red")

# linea5 = c.create_line(10,10, BASE-10, ALTURA-10, fill="blue")

# linea6 = c.create_line(BASE-10,10, 10,ALTURA-10, fill="blue")

# Cruz
linea1 = c.create_line(BASE-305,5, BASE-155, 5, fill="dark violet", width=3)
linea2 = c.create_line(BASE-305,5, BASE-305, ALTURA-145, fill="dark violet", width=3)
linea3 = c.create_line(BASE-305, ALTURA-145, BASE-455, ALTURA-145, fill="dark violet", width=3)
linea4 = c.create_line(BASE-455, ALTURA-145, BASE-455,ALTURA-75, fill="dark violet", width=3)
linea5 = c.create_line(BASE-455,ALTURA-75, BASE-305, ALTURA-75, fill="dark violet", width=3)
linea6 = c.create_line(BASE-305, ALTURA-75, BASE-305, ALTURA-5, fill="dark violet", width=3)
linea7 = c.create_line(BASE-305, ALTURA-5, BASE-155, ALTURA-5, fill="dark violet", width=3)
linea8 = c.create_line(BASE-155, ALTURA-5, BASE-155, ALTURA-75, fill="dark violet", width=3)
linea9 = c.create_line(BASE-155, ALTURA-75, BASE-5, ALTURA-75, fill="dark violet", width=3)
linea10 = c.create_line(BASE-5, ALTURA-75, BASE-5, ALTURA-145, fill="dark violet", width=3)
linea11 = c.create_line(BASE-5, ALTURA-145, BASE-155, ALTURA-145, fill="dark violet", width=3)
linea12 = c.create_line(BASE-155, ALTURA-145,BASE-155, 5, fill="dark violet", width=3)

linea1= c.create_line(204, 33, 204, ALTURA-135, fill="NavajoWhite4", width=3)
linea2= c.create_line(204, 33, BASE-204, 33, fill="NavajoWhite4", width=3)
linea3= c.create_line(255, 33, 255, ALTURA-135, fill="NavajoWhite4", width=3)
linea4= c.create_line(255, ALTURA-135, 306, ALTURA-135, fill="NavajoWhite4", width=3)
linea5= c.create_line(306, ALTURA-135, 306, ALTURA-84, fill="NavajoWhite4", width=3)
linea6= c.create_line(306, ALTURA-84, BASE-204, ALTURA-84, fill="NavajoWhite4", width=3)
linea7= c.create_line(BASE-204, ALTURA-84, BASE-204, ALTURA-33, fill="NavajoWhite4", width=3)
linea8= c.create_line(BASE-204, ALTURA-33, BASE-255, ALTURA-33, fill="NavajoWhite4", width=3)
linea9= c.create_line(BASE-255, ALTURA-33, BASE-255, ALTURA-84, fill="NavajoWhite4", width=3)
linea9= c.create_line(BASE-255, ALTURA-33, BASE-255, ALTURA-84, fill="NavajoWhite4", width=3)
linea10= c.create_line(BASE-255, ALTURA-84,BASE-306, ALTURA-84,  fill="NavajoWhite4", width=3)
linea11= c.create_line(BASE-306, ALTURA-84,BASE-306, ALTURA-135,  fill="NavajoWhite4", width=3)
linea12= c.create_line(BASE-306, ALTURA-135,BASE-255, ALTURA-135,  fill="NavajoWhite4", width=3)

ventana_principal.mainloop()