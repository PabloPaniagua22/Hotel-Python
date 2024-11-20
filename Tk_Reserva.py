import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from crear_conexion_bd import conectar_bd
from faker import Faker

# Importar funciones CRUD
from Huesped import *
from Empleados import *
from ServiciosAdicionales import *
from Reserva import *

# Configuración de Faker
faker = Faker()

# Configuración de tema de sistema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("1200x800")
root.title("Sistema de Gestión de Hotel")

# Creación de Tabs
tabControl = ttk.Notebook(root)
tab_reserva = ttk.Frame(tabControl)
tab_verReserva = ttk.Frame(tabControl)
tabControl.add(tab_reserva, text="Reserva")
tabControl.add(tab_verReserva, text="Ver Reserva")
tabControl.pack(expand=1, fill="both")


# --------------------------
# Pestaña para crear "Reserva"
# --------------------------

frame_reserva_nueva = ttk.LabelFrame(tab_reserva, text="Nueva Reserva")
frame_reserva_nueva.pack(fill="x", padx=20, pady=20)

# Campos para la reserva
ctk.CTkLabel(frame_reserva_nueva, text="ID Empleado").grid(row=0, column=0)
entry_id_empleado = ctk.CTkEntry(frame_reserva_nueva)
entry_id_empleado.grid(row=0, column=1)

ctk.CTkLabel(frame_reserva_nueva, text="ID Huésped").grid(row=1, column=0)
entry_id_huesped = ctk.CTkEntry(frame_reserva_nueva)
entry_id_huesped.grid(row=1, column=1)

ctk.CTkLabel(frame_reserva_nueva, text="ID Habitación").grid(row=2, column=0)
entry_id_habitacion = ctk.CTkEntry(frame_reserva_nueva)
entry_id_habitacion.grid(row=2, column=1)

ctk.CTkLabel(frame_reserva_nueva, text="ID Servicios Adicionales").grid(row=3, column=0)
entry_id_servicios_adicionales = ctk.CTkEntry(frame_reserva_nueva)
entry_id_servicios_adicionales.grid(row=3, column=1)

ctk.CTkLabel(frame_reserva_nueva, text="Fecha de Ingreso").grid(row=4, column=0)
date_entry_ingreso = DateEntry(frame_reserva_nueva, date_pattern='yyyy-mm-dd')
date_entry_ingreso.grid(row=4, column=1)

ctk.CTkLabel(frame_reserva_nueva, text="Fecha de Egreso").grid(row=5, column=0)
date_entry_egreso = DateEntry(frame_reserva_nueva, date_pattern='yyyy-mm-dd')
date_entry_egreso.grid(row=5, column=1)

ctk.CTkLabel(frame_reserva_nueva, text="Importe").grid(row=6, column=0)
entry_importe = ctk.CTkEntry(frame_reserva_nueva)
entry_importe.grid(row=6, column=1)

ctk.CTkLabel(frame_reserva_nueva, text="Observaciones").grid(row=7, column=0)
entry_observaciones = ctk.CTkEntry(frame_reserva_nueva)
entry_observaciones.grid(row=7, column=1)

# Botón para agregar la reserva
ctk.CTkButton(frame_reserva_nueva, text="Agregar Reserva", command=lambda: crear_reserva(entry_id_empleado.get(), entry_id_huesped.get(), entry_id_habitacion.get(), entry_id_servicios_adicionales.get(), date_entry_ingreso.get(), date_entry_egreso.get(), entry_importe.get(), entry_observaciones.get())).grid(row=8, column=0, columnspan=2, pady=10)

# --------------------------
# Pestaña para ver y gestionar "Reservas"
# --------------------------

frame_ver_reserva = ttk.LabelFrame(tab_verReserva, text="Ver Reservas")
frame_ver_reserva.pack(fill="both", expand=True, padx=10, pady=10)

tree_reserva = ttk.Treeview(frame_ver_reserva, columns=("ID Reserva", "ID Empleado", "ID Huésped", "ID Habitación", "ID Servicios Adicionales", "Ingreso", "Egreso", "Importe", "Observaciones"), show="headings")
tree_reserva.heading("ID Reserva", text="ID Reserva")
tree_reserva.heading("ID Empleado", text="ID Empleado")
tree_reserva.heading("ID Huésped", text="ID Huésped")
tree_reserva.heading("ID Habitación", text="ID Habitación")
tree_reserva.heading("ID Servicios Adicionales", text="ID Servicios Adicionales")
tree_reserva.heading("Ingreso", text="Ingreso")
tree_reserva.heading("Egreso", text="Egreso")
tree_reserva.heading("Importe", text="Importe")
tree_reserva.heading("Observaciones", text="Observaciones")
tree_reserva.pack(fill="both", expand=True)

# # Función para cargar reservas en el treeview
# def cargar_reservas():
#     for i in tree_reserva.get_children():
#         tree_reserva.delete(i)
#     for reserva in obtener_reservas():
#         tree_reserva.insert("", "end", values=reserva)

obtener_reservas()

# Botones para editar y eliminar reservas
ctk.CTkButton(frame_ver_reserva, text="Editar", command=lambda: actualizar_reserva(tree_reserva.selection())).pack(side="left", padx=5, pady=5)
ctk.CTkButton(frame_ver_reserva, text="Eliminar", command=lambda: eliminar_reserva(tree_reserva.selection())).pack(side="left", padx=5, pady=5)

# Finaliza con el bucle principal de tkinter
root.mainloop()
