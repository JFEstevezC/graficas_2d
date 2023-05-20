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
"""linea1 = c.create_line(10,10, BASE-10, 10, fill="red", width=3)
linea2 = c.create_line(BASE-10,10, BASE-10, ALTURA-10, fill="red", width=3)
linea3 = c.create_line(BASE-10,ALTURA-10, 10, ALTURA-10, fill="red", width=3)
linea4 = c.create_line(10,ALTURA-10, 10,10, fill="red", width=3)
#linea5 = c.create_line(10,10, BASE-10, ALTURA-10, fill="blue", width=3)
#linea6 = c.create_line(BASE-10,10, 10,ALTURA-10, fill="blue", width=3)

# Cruz
linea1 = c.create_line(BASE-305,10, BASE-155, 10, fill="dark violet", width=3)
linea2 = c.create_line(BASE-305,10, BASE-305, ALTURA-145, fill="dark violet", width=3)
linea3 = c.create_line(BASE-305, ALTURA-145, BASE-450, ALTURA-145, fill="dark violet", width=3)
linea4 = c.create_line(BASE-450, ALTURA-145, BASE-450,ALTURA-75, fill="dark violet", width=3)
linea5 = c.create_line(BASE-450,ALTURA-75, BASE-305, ALTURA-75, fill="dark violet", width=3)
linea6 = c.create_line(BASE-305, ALTURA-75, BASE-305, ALTURA-10, fill="dark violet", width=3)
linea7 = c.create_line(BASE-305, ALTURA-10, BASE-155, ALTURA-10, fill="dark violet", width=3)
linea8 = c.create_line(BASE-155, ALTURA-10, BASE-155, ALTURA-75, fill="dark violet", width=3)
linea9 = c.create_line(BASE-155, ALTURA-75, BASE-10, ALTURA-75, fill="dark violet", width=3)
linea10 = c.create_line(BASE-10, ALTURA-75, BASE-10, ALTURA-145, fill="dark violet", width=3)
linea11 = c.create_line(BASE-10, ALTURA-145, BASE-155, ALTURA-145, fill="dark violet", width=3)
linea12 = c.create_line(BASE-155, ALTURA-145,BASE-155, 10, fill="dark violet", width=3)

#linea1= c.create_line(204, 33, 204, ALTURA-135, fill="NavajoWhite4", width=3)
#linea2= c.create_line(204, 33, BASE-204, 33, fill="NavajoWhite4", width=3)
#linea3= c.create_line(255, 33, 255, ALTURA-135, fill="NavajoWhite4", width=3)
#linea4= c.create_line(255, ALTURA-135, 306, ALTURA-135, fill="NavajoWhite4", width=3)
#linea5= c.create_line(306, ALTURA-135, 306, ALTURA-84, fill="NavajoWhite4", width=3)
#linea6= c.create_line(306, ALTURA-84, BASE-204, ALTURA-84, fill="NavajoWhite4", width=3)
#linea7= c.create_line(BASE-204, ALTURA-84, BASE-204, ALTURA-33, fill="NavajoWhite4", width=3)
#linea8= c.create_line(BASE-204, ALTURA-33, BASE-255, ALTURA-33, fill="NavajoWhite4", width=3)
#linea9= c.create_line(BASE-255, ALTURA-33, BASE-255, ALTURA-84, fill="NavajoWhite4", width=3)
#linea9= c.create_line(BASE-255, ALTURA-33, BASE-255, ALTURA-84, fill="NavajoWhite4", width=3)
#linea10= c.create_line(BASE-255, ALTURA-84,BASE-306, ALTURA-84,  fill="NavajoWhite4", width=3)
#linea11= c.create_line(BASE-306, ALTURA-84,BASE-306, ALTURA-135,  fill="NavajoWhite4", width=3)
#linea12= c.create_line(BASE-306, ALTURA-135,BASE-255, ALTURA-135,  fill="NavajoWhite4", width=3)

# TEXTO
texto1 = c.create_text(BASE/2, ALTURA/2, text="SISTEMAS UIS SOCORRO", anchor="w", font=("Times New Roman", "20", "bold"), fill="green", activefill="white")

# Cuadros y rectángulos

rect1 = c.create_rectangle(20, 20, 120, 120, fill="blue", outline="red", width=3)"""

# Polígonos
#poligono1 = c.create_polygon(BASE/5, 0, BASE/2, ALTURA/5, BASE/5, ALTURA/2,0,ALTURA/5, fill= "red")
#poligono2 = c.create_polygon(0, ALTURA, BASE/2, ALTURA/2, BASE, ALTURA, fill= "green")
#poligono3 = c.create_polygon(0, 0, BASE/2, ALTURA/2, 0, ALTURA, fill= "blue")

poligono1 = c.create_polygon(BASE/4, 0, BASE/2, ALTURA/4, BASE/4, ALTURA/2,0,ALTURA/4, fill= "red")
poligono2 = c.create_polygon(BASE/4,ALTURA/2,BASE/2,(ALTURA/4)*3,BASE/4, ALTURA, 0,(ALTURA/4)*3, fill= "blue")
poligono1 = c.create_polygon((BASE/4)*3, 0, BASE, ALTURA/4, (BASE/4)*3, ALTURA/2,BASE/2,ALTURA/4, fill= "green")
poligono2 = c.create_polygon((BASE/4)*3,ALTURA/2,BASE,(ALTURA/4)*3,(BASE/4)*3, ALTURA, BASE/2,(ALTURA/4)*3, fill= "black")

# OVALOS - CIRCULO
#elipse1 = c.create_oval((BASE/2)-5, (ALTURA/2)-5, (BASE/2)+5, (ALTURA/2)+5, fill ="yellow")

# ARCOS
arc1=c.create_arc((BASE/2)-30, (ALTURA/2)-30, (BASE/2)+30, (ALTURA/2)+30, start=30, extent=300, fill ="black")

elipse1 = c.create_oval((BASE/2-5), (ALTURA/2-5)-15, (BASE/2+5), (ALTURA/2+5)-15, fill ="yellow")

arc2=c.create_arc(BASE/4-30,ALTURA/4-30,BASE/4+30,ALTURA/4+30, start=30, extent=300, fill ="yellow")
elipse2 = c.create_oval(BASE/4-3,(ALTURA/4-3)-15,BASE/4+3,(ALTURA/4+3)-15, fill ="black")

arc3=c.create_arc(BASE*3/4-30,ALTURA*3/4-30,BASE*3/4+30,ALTURA*3/4+30, start=30, extent=300, fill ="yellow")
elipse3 = c.create_oval(BASE*3/4-3,(ALTURA*3/4-3)-15,BASE*3/4+3,(ALTURA*3/4+3)-15, fill ="black")

arc4=c.create_arc(BASE*3/4-30,ALTURA/4-30,BASE*3/4+30,ALTURA/4+30, start=30, extent=300, fill ="yellow")
elipse4 = c.create_oval(BASE*3/4-3,(ALTURA/4-3)-15,BASE*3/4+3,(ALTURA/4+3)-15, fill ="black")

arc5=c.create_arc(BASE/4-30,ALTURA*3/4-30,BASE/4+30,ALTURA*3/4+30, start=30, extent=300, fill ="yellow")
elipse5 = c.create_oval(BASE/4-3,(ALTURA*3/4-3)-15,BASE/4+3,(ALTURA*3/4+3)-15, fill ="black")


ventana_principal.mainloop()