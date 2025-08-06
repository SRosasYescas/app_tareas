
import tkinter as tk
from tkinter import messagebox
from tareas import agregar_tarea, eliminar_tarea


#configuraciuon ventana principal
ventana = tk.Tk()
ventana.title("listas de tareas")

#cuiadro de entrada para agregar nuestras tareas
entrada_tareas = tk.Entry(ventana, width=40)
entrada_tareas.pack(pady=10)

#boton agregar tarea
boton_agregar = tk.Button(ventana, text="agregar tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

#lista para las tares
lista_tareas = tk.Listbox(ventana, width=50)
lista_tareas.pack(padx=10, pady=10)

#boton eliminar tareas
boton_eliminar = tk.Button(ventana, text="eliminar tarea", command=eliminar_tarea)

ventana.mainloop()
