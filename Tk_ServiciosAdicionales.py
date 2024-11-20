import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from faker import Faker

# Importar funciones CRUD
from ServiciosAdicionales import *

# Configuración de Faker
faker = Faker()

# Configuracion de tema de sistema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("1000x700")
root.title("Sistema de Gestión de Hotel - Servicios Adicionales")

# Creación de Tabs
tabControl = ttk.Notebook(root)
tab_servicio = ttk.Frame(tabControl)
tab_verServicio = ttk.Frame(tabControl)
tabControl.add(tab_servicio, text="Servicio")
tabControl.add(tab_verServicio, text="Ver Servicios")
tabControl.pack(expand=1, fill="both")

# Sección "Servicio" (Agregar Servicio)
frame_servicio_nuevo = ttk.LabelFrame(tab_servicio, text="Nuevo Servicio")
frame_servicio_nuevo.pack(fill="x", padx=20, pady=20)

ctk.CTkLabel(frame_servicio_nuevo, text="ID Empleado").grid(row=0, column=0)
entry_id_empleado = ctk.CTkEntry(frame_servicio_nuevo)
entry_id_empleado.grid(row=0, column=1)

ctk.CTkLabel(frame_servicio_nuevo, text="Tipo de Servicio").grid(row=1, column=0)
combo_tipo = ctk.CTkComboBox(frame_servicio_nuevo, values=["Lavandería", "Room Service", "Spa", "Gimnasio", "Transporte", "Otro"])
combo_tipo.grid(row=1, column=1)

ctk.CTkLabel(frame_servicio_nuevo, text="Costo").grid(row=2, column=0)
entry_costo = ctk.CTkEntry(frame_servicio_nuevo)
entry_costo.grid(row=2, column=1)

ctk.CTkLabel(frame_servicio_nuevo, text="Disponible").grid(row=3, column=0)
combo_disponible = ctk.CTkComboBox(frame_servicio_nuevo, values=["Sí", "No"])
combo_disponible.grid(row=3, column=1)

ctk.CTkLabel(frame_servicio_nuevo, text="Observaciones").grid(row=4, column=0)
entry_observaciones = ctk.CTkEntry(frame_servicio_nuevo)
entry_observaciones.grid(row=4, column=1)

# Botón para agregar el servicio
ctk.CTkButton(frame_servicio_nuevo, text="Agregar Servicio", 
              command=lambda: agregar_servicio(
                  entry_id_empleado.get(),
                  combo_tipo.get(),
                  float(entry_costo.get()),
                  1 if combo_disponible.get() == "Sí" else 0,
                  entry_observaciones.get()
              )).grid(row=5, column=0, columnspan=2, pady=10)

# Función para generar datos faker
def generar_servicio_faker():
    entry_id_empleado.delete(0, 'end')
    entry_id_empleado.insert(0, str(faker.random_int(min=1, max=100)))
    combo_tipo.set(faker.random_element(elements=combo_tipo._values))
    entry_costo.delete(0, 'end')
    entry_costo.insert(0, str(faker.random_int(min=100, max=10000)))
    combo_disponible.set(faker.random_element(elements=["Sí", "No"]))
    entry_observaciones.delete(0, 'end')
    entry_observaciones.insert(0, faker.sentence())

# Agregar el botón para generar Faker
ctk.CTkButton(frame_servicio_nuevo, text="Generar Faker", 
              command=generar_servicio_faker).grid(row=6, column=0, columnspan=2)

# Tabla para ver servicios
frame_ver_servicio = ttk.LabelFrame(tab_verServicio, text="Ver Servicios")
frame_ver_servicio.pack(fill="both", expand=True, padx=10, pady=10)

tree_servicio = ttk.Treeview(frame_ver_servicio, 
                            columns=("ID", "ID_Empleado", "Tipo", "Costo", "Disponible", "Observaciones"),
                            show="headings")
tree_servicio.heading("ID", text="ID")
tree_servicio.heading("ID_Empleado", text="ID Empleado")
tree_servicio.heading("Tipo", text="Tipo")
tree_servicio.heading("Costo", text="Costo")
tree_servicio.heading("Disponible", text="Disponible")
tree_servicio.heading("Observaciones", text="Observaciones")
tree_servicio.pack(fill="both", expand=True)

# Función para actualizar la tabla
def actualizar_tabla():
    for item in tree_servicio.get_children():
        tree_servicio.delete(item)
    servicios = obtener_servicios()
    for servicio in servicios:
        tree_servicio.insert('', 'end', values=servicio)

# Función para editar servicio seleccionado
def editar_servicio_seleccionado():
    seleccion = tree_servicio.selection()
    if not seleccion:
        return
    
    item = tree_servicio.item(seleccion[0])
    valores = item['values']
    
    # Crear ventana de edición
    ventana_edicion = ctk.CTkToplevel()
    ventana_edicion.title("Editar Servicio")
    ventana_edicion.geometry("400x300")
    
    ctk.CTkLabel(ventana_edicion, text="ID Empleado").pack()
    edit_id_empleado = ctk.CTkEntry(ventana_edicion)
    edit_id_empleado.insert(0, valores[1])
    edit_id_empleado.pack()
    
    ctk.CTkLabel(ventana_edicion, text="Tipo").pack()
    edit_tipo = ctk.CTkComboBox(ventana_edicion, values=["Lavandería", "Room Service", "Spa", "Gimnasio", "Transporte", "Otro"])
    edit_tipo.set(valores[2])
    edit_tipo.pack()
    
    ctk.CTkLabel(ventana_edicion, text="Costo").pack()
    edit_costo = ctk.CTkEntry(ventana_edicion)
    edit_costo.insert(0, valores[3])
    edit_costo.pack()
    
    ctk.CTkLabel(ventana_edicion, text="Disponible").pack()
    edit_disponible = ctk.CTkComboBox(ventana_edicion, values=["Sí", "No"])
    edit_disponible.set("Sí" if valores[4] == 1 else "No")
    edit_disponible.pack()
    
    ctk.CTkLabel(ventana_edicion, text="Observaciones").pack()
    edit_observaciones = ctk.CTkEntry(ventana_edicion)
    edit_observaciones.insert(0, valores[5])
    edit_observaciones.pack()
    
    def guardar_cambios():
        actualizar_servicio(
            valores[0],
            edit_id_empleado.get(),
            edit_tipo.get(),
            float(edit_costo.get()),
            1 if edit_disponible.get() == "Sí" else 0,
            edit_observaciones.get()
        )
        actualizar_tabla()
        ventana_edicion.destroy()
    
    ctk.CTkButton(ventana_edicion, text="Guardar", command=guardar_cambios).pack(pady=10)

# Función para eliminar servicio seleccionado
def eliminar_servicio_seleccionado():
    seleccion = tree_servicio.selection()
    if seleccion:
        item = tree_servicio.item(seleccion[0])
        eliminar_servicio(item['values'][0])
        actualizar_tabla()

# Botones de edición y eliminación
ctk.CTkButton(frame_ver_servicio, text="Editar", 
              command=editar_servicio_seleccionado).pack(side="left", padx=5, pady=5)
ctk.CTkButton(frame_ver_servicio, text="Eliminar", 
              command=eliminar_servicio_seleccionado).pack(side="left", padx=5, pady=5)

# Cargar datos iniciales
actualizar_tabla()

# Iniciar la aplicación
root.mainloop()