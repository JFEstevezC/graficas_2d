from tkinter import Tk, Canvas

ventana = Tk()

# Crear el canvas con fondo transparente
canvas = Canvas(ventana, width=400, height=300, bg="SystemTransparent", highlightthickness=0)

# Agregar elementos al canvas
canvas.create_rectangle(50, 50, 200, 200, fill="red")
canvas.create_oval(250, 50, 350, 150, fill="green")

# Mostrar el canvas
canvas.pack()

ventana.mainloop()