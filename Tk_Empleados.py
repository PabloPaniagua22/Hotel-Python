import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from faker import Faker
import random
from Empleados import *  # Importar funciones CRUD para empleados

# Configuración de Faker
faker = Faker()

# Configuración de tema de sistema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("1000x700")
root.title("Sistema de Gestión de Empleados")

# Creación de Tabs
tabControl = ttk.Notebook(root)
tab_empleado = ttk.Frame(tabControl)
tab_verEmpleado = ttk.Frame(tabControl)
tabControl.add(tab_empleado, text="Empleado")
tabControl.add(tab_verEmpleado, text="Ver Empleado")
tabControl.pack(expand=1, fill="both")

# Sección "Empleado" (Agregar y Ver Empleado)
frame_empleado_nuevo = ttk.LabelFrame(tab_empleado, text="Nuevo Empleado")
frame_empleado_nuevo.pack(fill="x", padx=20, pady=20)

ctk.CTkLabel(frame_empleado_nuevo, text="Nombre").grid(row=0, column=0)
entry_nombre = ctk.CTkEntry(frame_empleado_nuevo)
entry_nombre.grid(row=0, column=1)

ctk.CTkLabel(frame_empleado_nuevo, text="Apellido").grid(row=1, column=0)
entry_apellido = ctk.CTkEntry(frame_empleado_nuevo)
entry_apellido.grid(row=1, column=1)

ctk.CTkLabel(frame_empleado_nuevo, text="DNI").grid(row=2, column=0)
entry_DNI = ctk.CTkEntry(frame_empleado_nuevo)
entry_DNI.grid(row=2, column=1)

ctk.CTkLabel(frame_empleado_nuevo, text="Teléfono").grid(row=3, column=0)
entry_telefono = ctk.CTkEntry(frame_empleado_nuevo)
entry_telefono.grid(row=3, column=1)

ctk.CTkLabel(frame_empleado_nuevo, text="Email").grid(row=4, column=0)
entry_email = ctk.CTkEntry(frame_empleado_nuevo)
entry_email.grid(row=4, column=1)

ctk.CTkLabel(frame_empleado_nuevo, text="Dirección").grid(row=5, column=0)
entry_direccion = ctk.CTkEntry(frame_empleado_nuevo)
entry_direccion.grid(row=5, column=1)

# Select para 'Tipo_Empleado' con opciones
ctk.CTkLabel(frame_empleado_nuevo, text="Tipo de Empleado").grid(row=6, column=0)
combo_tipo_empleado = ctk.CTkComboBox(frame_empleado_nuevo, values=["Administrativo", "Recepcionista", "Limpieza", "Gerente"])
combo_tipo_empleado.grid(row=6, column=1)

# Campo de salario
ctk.CTkLabel(frame_empleado_nuevo, text="Salario").grid(row=7, column=0)
entry_salario = ctk.CTkEntry(frame_empleado_nuevo)
entry_salario.grid(row=7, column=1)

# Campo de fecha de contratación
ctk.CTkLabel(frame_empleado_nuevo, text="Fecha de Contratación").grid(row=8, column=0)
date_entry_contratacion = DateEntry(frame_empleado_nuevo, date_pattern='yyyy-mm-dd')
date_entry_contratacion.grid(row=8, column=1)

# Botón para agregar empleado
ctk.CTkButton(frame_empleado_nuevo, text="Agregar Empleado", command=lambda: crear_empleado(
    entry_nombre.get(), entry_apellido.get(), entry_DNI.get(), entry_telefono.get(), entry_email.get(), 
    entry_direccion.get(), combo_tipo_empleado.get(), entry_salario.get(), date_entry_contratacion.get())
).grid(row=9, column=0, columnspan=2, pady=10)

# Botón para generar Faker
ctk.CTkButton(frame_empleado_nuevo, text="Generar Faker", command=generar_empleado).grid(row=10, column=0, columnspan=2)

# Tabla para ver empleados
frame_ver_empleado = ttk.LabelFrame(tab_verEmpleado, text="Ver Empleado")
frame_ver_empleado.pack(fill="both", expand=True, padx=10, pady=10)

tree_empleado = ttk.Treeview(frame_ver_empleado, columns=("ID", "Nombre", "Apellido", "DNI", "Telefono", "Email", "Direccion", "Tipo Empleado", "Salario", "Fecha Contratacion"), show="headings")
tree_empleado.heading("ID", text="ID")
tree_empleado.heading("Nombre", text="Nombre")
tree_empleado.heading("Apellido", text="Apellido")
tree_empleado.heading("DNI", text="DNI")
tree_empleado.heading("Telefono", text="Teléfono")
tree_empleado.heading("Email", text="Email")
tree_empleado.heading("Direccion", text="Dirección")
tree_empleado.heading("Tipo Empleado", text="Tipo Empleado")
tree_empleado.heading("Salario", text="Salario")
tree_empleado.heading("Fecha Contratacion", text="Fecha de Contratación")
tree_empleado.pack(fill="both", expand=True)

# Cargar datos de empleados en la interfaz gráfica
def cargar_empleados():
    empleados = obtener_empleados()
    for empleado in empleados:
        tree_empleado.insert("", "end", values=empleado)

cargar_empleados()

# Botones para editar y eliminar empleados
ctk.CTkButton(frame_ver_empleado, text="Editar", command=lambda: actualizar_empleado(tree_empleado.selection())).pack(side="left", padx=5, pady=5)
ctk.CTkButton(frame_ver_empleado, text="Eliminar", command=lambda: eliminar_empleado(tree_empleado.selection())).pack(side="left", padx=5, pady=5)

# Bucle principal de tkinter
root.mainloop()
