import tkinter as tk
from tkinter import messagebox

#funcion para asgregar tareas
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)


# funcion eliminada de la lista
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        lista_tareas.delete(tare_seleccionada)

    except IndexError:
        messagebox.showwarning("Advertencia, Porfavor seleccione una tarea")




