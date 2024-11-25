import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from faker import Faker

# Importar funciones CRUD
from ServiciosAdicionales import *

# Configuración de Faker
faker = Faker()

# Configuración de tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Ventana principal
root = ctk.CTk()
root.geometry("800x600")
root.title("Sistema de Gestión de Hotel - Servicios Adicionales")

# Tabs
tabControl = ttk.Notebook(root)
tab_servicio = ttk.Frame(tabControl)
tab_verServicio = ttk.Frame(tabControl)
tabControl.add(tab_servicio, text="Servicio")
tabControl.add(tab_verServicio, text="Ver Servicios")
tabControl.pack(expand=1, fill="both")

# Sección "Servicio" (Agregar Servicio)
frame_servicio_nuevo = ttk.LabelFrame(tab_servicio, text="Nuevo Servicio")
frame_servicio_nuevo.pack(fill="x", padx=20, pady=20)

ctk.CTkLabel(frame_servicio_nuevo, text="Tipo de Servicio").grid(row=0, column=0)
combo_tipo = ctk.CTkComboBox(frame_servicio_nuevo, values=["Lavandería", "Room Service", "Spa", "Gimnasio", "Transporte", "Otro"])
combo_tipo.grid(row=0, column=1)

ctk.CTkLabel(frame_servicio_nuevo, text="Costo").grid(row=1, column=0)
entry_costo = ctk.CTkEntry(frame_servicio_nuevo)
entry_costo.grid(row=1, column=1)

ctk.CTkLabel(frame_servicio_nuevo, text="Observaciones").grid(row=2, column=0)
entry_observaciones = ctk.CTkEntry(frame_servicio_nuevo)
entry_observaciones.grid(row=2, column=1)

# Botón para agregar el servicio
ctk.CTkButton(frame_servicio_nuevo, text="Agregar Servicio",
              command=lambda: agregar_servicio(
                  combo_tipo.get(),
                  float(entry_costo.get()),
                  entry_observaciones.get()
              )).grid(row=3, column=0, columnspan=2, pady=10)

# Función para generar datos faker
def generar_servicio_faker():
    combo_tipo.set(faker.random_element(elements=combo_tipo._values))
    entry_costo.delete(0, 'end')
    entry_costo.insert(0, str(faker.random_int(min=100, max=10000)))
    entry_observaciones.delete(0, 'end')
    entry_observaciones.insert(0, faker.sentence())

# Botón para generar Faker
ctk.CTkButton(frame_servicio_nuevo, text="Generar Faker",
              command=generar_servicio_faker).grid(row=4, column=0, columnspan=2)

# Tabla para ver servicios
frame_ver_servicio = ttk.LabelFrame(tab_verServicio, text="Ver Servicios")
frame_ver_servicio.pack(fill="both", expand=True, padx=10, pady=10)

tree_servicio = ttk.Treeview(frame_ver_servicio,
                             columns=("ID", "Tipo", "Costo", "Observaciones"),
                             show="headings")
tree_servicio.heading("ID", text="ID")
tree_servicio.heading("Tipo", text="Tipo")
tree_servicio.heading("Costo", text="Costo")
tree_servicio.heading("Observaciones", text="Observaciones")
tree_servicio.pack(fill="both", expand=True)

def actualizar_tabla():
    # Limpiar tabla existente
    for item in tree_servicio.get_children():
        tree_servicio.delete(item)
    
    # Obtener servicios y formatear los datos
    servicios = obtener_servicios()
    for servicio in servicios:
        id_sa = servicio[0]
        tipo = servicio[1]
        costo = f"${servicio[2]:,.2f}"  # Formato: $1,234.56
        observaciones = servicio[3] if servicio[3] else "N/A"  # Manejar observaciones nulas
        
        # Insertar fila formateada en el Treeview
        tree_servicio.insert('', 'end', values=(id_sa, tipo, costo, observaciones))


# Función para eliminar servicio seleccionado
def eliminar_servicio_seleccionado():
    seleccion = tree_servicio.selection()
    if seleccion:
        item = tree_servicio.item(seleccion[0])
        eliminar_servicio(item['values'][0])
        actualizar_tabla()

# Botón de eliminación
ctk.CTkButton(frame_ver_servicio, text="Eliminar",
              command=eliminar_servicio_seleccionado).pack(side="left", padx=5, pady=5)

# Cargar datos iniciales
actualizar_tabla()

# Iniciar la aplicación
root.mainloop()
