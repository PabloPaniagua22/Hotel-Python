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

# Campos de entrada
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

ctk.CTkLabel(frame_huesped_nuevo, text="Email").grid(row=5, column=0)
entry_email = ctk.CTkEntry(frame_huesped_nuevo)
entry_email.grid(row=5, column=1)

ctk.CTkLabel(frame_huesped_nuevo, text="Domicilio").grid(row=6, column=0)
entry_domicilio = ctk.CTkEntry(frame_huesped_nuevo)
entry_domicilio.grid(row=6, column=1)

# ComboBox para 'Condicion_IVA'
ctk.CTkLabel(frame_huesped_nuevo, text="Condición IVA").grid(row=7, column=0)
combo_condicion_iva = ctk.CTkComboBox(frame_huesped_nuevo, values=["Responsable Inscripto", "Exento", "Monotributista", "Consumidor Final"])
combo_condicion_iva.grid(row=7, column=1)

# ComboBox para 'Tipo_Huesped'
ctk.CTkLabel(frame_huesped_nuevo, text="Tipo Huesped").grid(row=8, column=0)
combo_tipo_huesped = ctk.CTkComboBox(frame_huesped_nuevo, values=["VIP", "Gold", "Platinum", "Corporativo"])
combo_tipo_huesped.grid(row=8, column=1)

# Campo para Fecha de Nacimiento
ctk.CTkLabel(frame_huesped_nuevo, text="Fecha de Nacimiento").grid(row=9, column=0)
date_entry_fnac = DateEntry(frame_huesped_nuevo, date_pattern='yyyy-mm-dd')
date_entry_fnac.grid(row=9, column=1)

# Campo para Observaciones
ctk.CTkLabel(frame_huesped_nuevo, text="Observaciones").grid(row=10, column=0)
entry_observaciones = ctk.CTkEntry(frame_huesped_nuevo)
entry_observaciones.grid(row=10, column=1)

# Botón para agregar huésped
boton_agregar_huesped = ctk.CTkButton(
    frame_huesped_nuevo,
    text="Agregar Huésped",
    command=lambda: crear_huesped(
        dni=entry_DNI.get(),
        cuil=entry_CUIL.get(),
        nombre=entry_nombre.get(),
        apellido=entry_apellido.get(),
        telefono=entry_telefono.get(),
        email=entry_email.get(),
        domicilio=entry_domicilio.get(),
        condicion_iva=combo_condicion_iva.get(),
        tipo_huesped=combo_tipo_huesped.get(),
        fecha_nacimiento=date_entry_fnac.get(),
        observaciones=entry_observaciones.get()
    )
)
boton_agregar_huesped.grid(row=11, column=0, columnspan=2, pady=10)

# Botón para generar datos Faker
ctk.CTkButton(frame_huesped_nuevo, text="Generar Faker", command=generar_huesped).grid(row=12, column=0, columnspan=2)

# Tabla para ver huéspedes
frame_ver_huesped = ttk.LabelFrame(tab_verHuesped, text="Ver Huéspedes")
frame_ver_huesped.pack(fill="both", expand=True, padx=10, pady=10)

tree_huesped = ttk.Treeview(
    frame_ver_huesped,
    columns=("ID_HUESPED", "DNI", "CUIL", "NOMBRE", "APELLIDO", "TELEFONO", "EMAIL", "DOMICILIO", "CONDICION_IVA", "TIPO_HUESPED", "FECHA_NACIMIENTO", "OBSERVACIONES"),
    show="headings"
)

# Configuración de los encabezados
tree_huesped.heading("ID_HUESPED", text="ID")
tree_huesped.heading("DNI", text="DNI")
tree_huesped.heading("CUIL", text="CUIL")
tree_huesped.heading("NOMBRE", text="Nombre")
tree_huesped.heading("APELLIDO", text="Apellido")
tree_huesped.heading("TELEFONO", text="Teléfono")
tree_huesped.heading("EMAIL", text="Email")
tree_huesped.heading("DOMICILIO", text="Domicilio")
tree_huesped.heading("CONDICION_IVA", text="Condición IVA")
tree_huesped.heading("TIPO_HUESPED", text="Tipo Huésped")
tree_huesped.heading("FECHA_NACIMIENTO", text="Fecha de Nacimiento")
tree_huesped.heading("OBSERVACIONES", text="Observaciones")

# Configuración del ancho de las columnas
tree_huesped.column("ID_HUESPED", width=50, anchor="center")
tree_huesped.column("DNI", width=100, anchor="center")
tree_huesped.column("CUIL", width=100, anchor="center")
tree_huesped.column("NOMBRE", width=150, anchor="w")
tree_huesped.column("APELLIDO", width=150, anchor="w")
tree_huesped.column("TELEFONO", width=100, anchor="center")
tree_huesped.column("EMAIL", width=200, anchor="w")
tree_huesped.column("DOMICILIO", width=200, anchor="w")
tree_huesped.column("CONDICION_IVA", width=120, anchor="w")
tree_huesped.column("TIPO_HUESPED", width=120, anchor="w")
tree_huesped.column("FECHA_NACIMIENTO", width=120, anchor="center")
tree_huesped.column("OBSERVACIONES", width=200, anchor="w")

# Mostrar el Treeview en el frame
tree_huesped.pack(fill="both", expand=True)

# Llamar a obtener_huespedes
obtener_huespedes(tree_huesped)

# Botones para Editar y Eliminar
ctk.CTkButton(frame_ver_huesped, text="Editar", command=lambda: editar_huesped(tree_huesped)).pack(side="left", padx=5, pady=5)
def eliminar_huesped_seleccion(treeview):
    seleccion = treeview.selection()  # Obtener selección actual
    if not seleccion:
        print("No se ha seleccionado ningún huésped.")
        return

    # Obtener valores de la fila seleccionada
    item = treeview.item(seleccion[0])
    valores = item["values"]

    if not valores:
        print("No se encontraron valores en la fila seleccionada.")
        return

    id_huesped = valores[0]  # El ID_HUESPED debería estar en la primera columna
    try:
        eliminar_huesped(id_huesped)  # Llamar a la función en Huesped.py
        print(f"Huésped con ID {id_huesped} eliminado.")
        obtener_huespedes(treeview)  # Refrescar la tabla después de eliminar
    except Exception as e:
        print(f"Error al eliminar huésped: {e}")

# Botón Eliminar
ctk.CTkButton(
    frame_ver_huesped,
    text="Eliminar",
    command=lambda: eliminar_huesped_seleccion(tree_huesped)
).pack(side="left", padx=5, pady=5)


# Finaliza con el bucle principal de tkinter
root.mainloop()
