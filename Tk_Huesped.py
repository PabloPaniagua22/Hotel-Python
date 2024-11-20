import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from faker import Faker

# Importar funciones CRUD
from Huesped import *
from Reserva import *
from Empleados import *
from ServiciosAdicionales import *

# Configuración de Faker
faker = Faker()

# Configuracion de tema de sistema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("1000x700")
root.title("Sistema de Gestión de Hotel")

# Creación de Tabs
tabControl = ttk.Notebook(root)
tab_huesped = ttk.Frame(tabControl)
tab_verHuesped = ttk.Frame(tabControl)
tabControl.add(tab_huesped, text="Huésped")
tabControl.add(tab_verHuesped, text="Ver Huésped")
tabControl.pack(expand=1, fill="both")

# Sección "Huésped" (Agregar y Ver Huésped)
frame_huesped_nuevo = ttk.LabelFrame(tab_huesped, text="Nuevo Huésped")
frame_huesped_nuevo.pack(fill="x", padx=20, pady=20)

ctk.CTkLabel(frame_huesped_nuevo, text="DNI").grid(row=0, column=0)
entry_DNI = ctk.CTkEntry(frame_huesped_nuevo)
entry_DNI.grid(row=0, column=1)

ctk.CTkLabel(frame_huesped_nuevo, text="CUIL").grid(row=1, column=0)
entry_CUIL = ctk.CTkEntry(frame_huesped_nuevo)
entry_CUIL.grid(row=1, column=1)

ctk.CTkLabel(frame_huesped_nuevo, text="Nombre").grid(row=2, column=0)
entry_nombre = ctk.CTkEntry(frame_huesped_nuevo)
entry_nombre.grid(row=2, column=1)

ctk.CTkLabel(frame_huesped_nuevo, text="Apellido").grid(row=3, column=0)
entry_apellido = ctk.CTkEntry(frame_huesped_nuevo)
entry_apellido.grid(row=3, column=1)

ctk.CTkLabel(frame_huesped_nuevo, text="Teléfono").grid(row=4, column=0)
entry_telefono = ctk.CTkEntry(frame_huesped_nuevo)
entry_telefono.grid(row=4, column=1)

ctk.CTkLabel(frame_huesped_nuevo, text="Mail").grid(row=5, column=0)
entry_Mail = ctk.CTkEntry(frame_huesped_nuevo)
entry_Mail.grid(row=5, column=1)

ctk.CTkLabel(frame_huesped_nuevo, text="Domicilio").grid(row=6, column=0)
entry_Domicilio = ctk.CTkEntry(frame_huesped_nuevo)
entry_Domicilio.grid(row=6, column=1)

# Agregar un select para 'Condicion_IVA' con las opciones
ctk.CTkLabel(frame_huesped_nuevo, text="Condición_IVA").grid(row=7, column=0)
combo_condicion_iva = ctk.CTkComboBox(frame_huesped_nuevo, values=["Responsable Inscripto", "Exento", "Monotributista", "Consumidor Final"])
combo_condicion_iva.grid(row=7, column=1)

# Agregar un select para 'Tipo_Cliente' con las opciones
ctk.CTkLabel(frame_huesped_nuevo, text="Tipo_Cliente").grid(row=8, column=0)
combo_Tipo_Cliente = ctk.CTkComboBox(frame_huesped_nuevo, values=["Nuevo", "Regular", "VIP"])
combo_Tipo_Cliente.grid(row=8, column=1)

# Agregar el campo de fecha de nacimiento
ctk.CTkLabel(frame_huesped_nuevo, text="Fecha de Nacimiento (FNAC)").grid(row=9, column=0)
date_entry_fnac = DateEntry(frame_huesped_nuevo, date_pattern='yyyy-mm-dd')
date_entry_fnac.grid(row=9, column=1)

# Agregar el campo de Observaciones
ctk.CTkLabel(frame_huesped_nuevo, text="Observaciones").grid(row=10, column=0)
entry_observaciones = ctk.CTkEntry(frame_huesped_nuevo)
entry_observaciones.grid(row=10, column=1)

# Botón para agregar el huésped
boton_agregar_huesped = ctk.CTkButton(
    frame_huesped_nuevo,
    text="Agregar Huésped",
    command=lambda: crear_huesped(
        dni=entry_DNI.get(),
        cuil=entry_CUIL.get(),
        nombre=entry_nombre.get(),
        apellido=entry_apellido.get(),
        telefono=entry_telefono.get(),
        mail=entry_Mail.get(),
        domicilio=entry_Domicilio.get(),
        condicion_iva=combo_condicion_iva.get(),
        tipo_cliente=combo_Tipo_Cliente.get(),
        fnac=date_entry_fnac.get(),
        observaciones=entry_observaciones.get()
    )
)
boton_agregar_huesped.grid(row=11, column=0, columnspan=2, pady=10)

# Agregar el botón para generar Faker
ctk.CTkButton(frame_huesped_nuevo, text="Generar Faker", command=generar_huesped).grid(row=12, column=0, columnspan=2)

# Tabla para ver huéspedes
frame_ver_huesped = ttk.LabelFrame(tab_verHuesped, text="Ver Huésped")
frame_ver_huesped.pack(fill="both", expand=True, padx=10, pady=10)

tree_huesped = ttk.Treeview(frame_ver_huesped, columns=("ID", "DNI", "CUIL", "Nombre", "Apellido", "Teléfono", "Mail", "Domicilio", "Condición_IVA", "Tipo_Cliente", "Fecha de Nacimiento (FNAC)", "Observaciones"), show="headings")
tree_huesped.heading("ID", text="ID")
tree_huesped.heading("DNI", text="DNI ")
tree_huesped.heading("CUIL", text="CUIL")
tree_huesped.heading("Nombre", text="Nombre")
tree_huesped.heading("Apellido", text="Apellido")
tree_huesped.heading("Teléfono", text="Teléfono")
tree_huesped.heading("Mail", text="Mail")
tree_huesped.heading("Domicilio", text="Domicilio")
tree_huesped.heading("Condición_IVA", text="Condición_IVA")
tree_huesped.heading("Tipo_Cliente", text="Tipo_Cliente")
tree_huesped.heading("Fecha de Nacimiento (FNAC)", text="Fecha de Nacimiento (FNAC)")
tree_huesped.heading("Observaciones", text="Observaciones")

tree_huesped.pack(fill="both", expand=True)

# Llamar a obtener_huespedes para cargar los datos en la interfaz gráfica
obtener_huespedes(tree_huesped)

ctk.CTkButton(frame_ver_huesped, text="Editar", command=lambda: actualizar_huesped(tree_huesped.selection())).pack(side="left", padx=5, pady=5)
ctk.CTkButton(frame_ver_huesped, text="Eliminar", command=lambda: eliminar_huesped(tree_huesped.selection())).pack(side="left", padx=5, pady=5)

# Finaliza con el bucle principal de tkinter
root.mainloop()
