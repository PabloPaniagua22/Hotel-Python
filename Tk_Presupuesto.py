import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import datetime
from faker import Faker
from Presupuesto import crear_presupuesto, obtener_presupuestos, eliminar_presupuesto, actualizar_presupuesto

# Configuración de Faker
faker = Faker()

# Configuración de tema de sistema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("1000x700")
root.title("Sistema de Gestión de Presupuestos")

# Creación de Tabs
tabControl = ttk.Notebook(root)
tab_presupuesto = ttk.Frame(tabControl)
tab_verPresupuesto = ttk.Frame(tabControl)
tabControl.add(tab_presupuesto, text="Presupuesto")
tabControl.add(tab_verPresupuesto, text="Ver Presupuestos")
tabControl.pack(expand=1, fill="both")

# Sección "Presupuesto" (Agregar Presupuesto)
frame_presupuesto_nuevo = ttk.LabelFrame(tab_presupuesto, text="Nuevo Presupuesto")
frame_presupuesto_nuevo.pack(fill="x", padx=20, pady=20)

# Campos de entrada
ctk.CTkLabel(frame_presupuesto_nuevo, text="ID Huésped").grid(row=0, column=0)
entry_id_huesped = ctk.CTkEntry(frame_presupuesto_nuevo)
entry_id_huesped.grid(row=0, column=1)

ctk.CTkLabel(frame_presupuesto_nuevo, text="ID Habitación").grid(row=1, column=0)
entry_id_habitacion = ctk.CTkEntry(frame_presupuesto_nuevo)
entry_id_habitacion.grid(row=1, column=1)

ctk.CTkLabel(frame_presupuesto_nuevo, text="ID Servicio Adicional").grid(row=2, column=0)
entry_id_sa = ctk.CTkEntry(frame_presupuesto_nuevo)
entry_id_sa.grid(row=2, column=1)

ctk.CTkLabel(frame_presupuesto_nuevo, text="Ingreso").grid(row=3, column=0)
date_ingreso = DateEntry(frame_presupuesto_nuevo, date_pattern="yyyy-mm-dd")
date_ingreso.grid(row=3, column=1)

ctk.CTkLabel(frame_presupuesto_nuevo, text="Egreso").grid(row=4, column=0)
date_egreso = DateEntry(frame_presupuesto_nuevo, date_pattern="yyyy-mm-dd")
date_egreso.grid(row=4, column=1)

ctk.CTkLabel(frame_presupuesto_nuevo, text="Importe").grid(row=5, column=0)
entry_importe = ctk.CTkEntry(frame_presupuesto_nuevo)
entry_importe.grid(row=5, column=1)

ctk.CTkLabel(frame_presupuesto_nuevo, text="Observaciones").grid(row=6, column=0)
entry_observaciones = ctk.CTkEntry(frame_presupuesto_nuevo)
entry_observaciones.grid(row=6, column=1)

# Botón para agregar presupuesto
boton_agregar_presupuesto = ctk.CTkButton(
    frame_presupuesto_nuevo,
    text="Agregar Presupuesto",
    command=lambda: crear_presupuesto(
        id_huesped=int(entry_id_huesped.get()),
        id_habitacion=int(entry_id_habitacion.get()),
        id_sa=int(entry_id_sa.get()),
        ingreso=date_ingreso.get(),
        egreso=date_egreso.get(),
        importe=float(entry_importe.get()),
        observaciones=entry_observaciones.get()
    )
)
boton_agregar_presupuesto.grid(row=7, column=0, columnspan=2, pady=10)

# Tabla para ver presupuestos
frame_ver_presupuesto = ttk.LabelFrame(tab_verPresupuesto, text="Ver Presupuestos")
frame_ver_presupuesto.pack(fill="both", expand=True, padx=10, pady=10)

tree_presupuesto = ttk.Treeview(
    frame_ver_presupuesto,
    columns=("ID_PRESUPUESTO", "ID_HUESPED", "ID_HABITACION", "ID_SA", "INGRESO", "EGRESO", "IMPORTE", "OBSERVACIONES", "FECHA"),
    show="headings"
)

# Configuración de los encabezados
for col in tree_presupuesto["columns"]:
    tree_presupuesto.heading(col, text=col)
    tree_presupuesto.column(col, anchor="center", width=120)

tree_presupuesto.pack(fill="both", expand=True)

# Función para cargar presupuestos en la tabla
def cargar_presupuestos():
    for item in tree_presupuesto.get_children():
        tree_presupuesto.delete(item)
    presupuestos = obtener_presupuestos()
    for presupuesto in presupuestos:
        tree_presupuesto.insert("", "end", values=presupuesto)

cargar_presupuestos()

# Botón para eliminar presupuesto
def eliminar_presupuesto_seleccion():
    seleccion = tree_presupuesto.selection()
    if not seleccion:
        print("No se ha seleccionado ningún presupuesto.")
        return
    item = tree_presupuesto.item(seleccion[0])
    id_presupuesto = item["values"][0]
    eliminar_presupuesto(id_presupuesto)
    cargar_presupuestos()

ctk.CTkButton(
    frame_ver_presupuesto,
    text="Eliminar",
    command=eliminar_presupuesto_seleccion
).pack(side="left", padx=5, pady=5)

# Finaliza con el bucle principal de tkinter
root.mainloop()
