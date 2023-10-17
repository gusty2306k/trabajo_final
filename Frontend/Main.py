from tkinter import Tk, ttk
import sqlite3
from Backend.Crud import Atraer_Seleccion_Argentina

import sys
sys.path.append("")

ventana = Tk()
ventana.title("Seleccion")
ventana.geometry("1000x300")

tree = ttk.Treeview(ventana, columns=("#0", "#1", "#2", "#3", "#4"))

tree.heading("#0", text="id")
tree.heading("#1", text="Arqueros")
tree.heading("#2", text="Defensores")
tree.heading("#3", text="Mediocampistas")
tree.heading("#4", text="Delanteros")


boton = ttk.Button(ventana, text="Eliminar",command= Atraer_Seleccion_Argentina)


tree.pack()



ventana.mainloop()