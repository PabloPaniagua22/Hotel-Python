import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from Descuentos import *  # Asegúrate de importar las funciones CRUD de descuentos aquí

# Configuración de tema de sistema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("1000x700")
root.title("Sistema de Gestión de Descuentos")

# Creación de Tabs
tabControl = ttk.Notebook(root)
tab_descuento = ttk.Frame(tabControl)
tab_verDescuento = ttk.Frame(tabControl)
tabControl.add(tab_descuento, text="Descuento")
tabControl.add(tab_verDescuento, text="Ver Descuento")
tabControl.pack(expand=1, fill="both")

# Sección "Descuento" (Agregar y Ver Descuento)
frame_descuento_nuevo = ttk.LabelFrame(tab_descuento, text="Nuevo Descuento")
frame_descuento_nuevo.pack(fill="x", padx=20, pady=20)

# Campo para seleccionar el tipo de huésped
ctk.CTkLabel(frame_descuento_nuevo, text="Tipo de Huesped").grid(row=0, column=0)
combo_tipo_huesped = ctk.CTkComboBox(frame_descuento_nuevo, values=["VIP", "Gold", "Platinum", "Corporativo"])
combo_tipo_huesped.grid(row=0, column=1)

# Campo para ingresar el descuento
ctk.CTkLabel(frame_descuento_nuevo, text="Descuento (%)").grid(row=1, column=0)
entry_descuento = ctk.CTkEntry(frame_descuento_nuevo)
entry_descuento.grid(row=1, column=1)

# Botón para agregar descuento
ctk.CTkButton(frame_descuento_nuevo, text="Agregar Descuento", command=lambda: crear_descuento(
    combo_tipo_huesped.get(), entry_descuento.get())
).grid(row=2, column=0, columnspan=2, pady=10)

# Tabla para ver descuentos
frame_ver_descuento = ttk.LabelFrame(tab_verDescuento, text="Ver Descuento")
frame_ver_descuento.pack(fill="both", expand=True, padx=10, pady=10)

tree_descuento = ttk.Treeview(frame_ver_descuento, columns=("ID", "Tipo Huesped", "Descuento"), show="headings")

# Configurar las columnas para que tengan un ancho adecuado
tree_descuento.column("ID", width=50, anchor="center")
tree_descuento.column("Tipo Huesped", width=150, anchor="center")
tree_descuento.column("Descuento", width=100, anchor="center")

# Configurar los encabezados
tree_descuento.heading("ID", text="ID")
tree_descuento.heading("Tipo Huesped", text="Tipo Huesped")
tree_descuento.heading("Descuento", text="Descuento (%)")

# Agregar scrollbar si es necesario
scrollbar = ttk.Scrollbar(frame_ver_descuento, orient="vertical", command=tree_descuento.yview)
tree_descuento.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

tree_descuento.pack(fill="both", expand=True)

# Cargar datos de descuentos en la interfaz gráfica
def cargar_descuentos():
    for row in tree_descuento.get_children():
        tree_descuento.delete(row)  # Limpia filas existentes

    descuentos = obtener_descuentos()
    for descuento in descuentos:
        # Asegúrate de formatear los valores correctamente (por ejemplo, el descuento debe tener dos decimales)
        tipo_huesped = descuento[1]
        descuento_value = f"{descuento[2]:.2f}"  # Formatear el descuento con dos decimales
        tree_descuento.insert("", "end", values=(descuento[0], tipo_huesped, descuento_value))

cargar_descuentos()

# Botones para editar y eliminar descuentos
ctk.CTkButton(frame_ver_descuento, text="Editar", command=lambda: actualizar_descuento(
    tree_descuento.selection()
)).pack(side="left", padx=5, pady=5)

ctk.CTkButton(frame_ver_descuento, text="Eliminar", command=lambda: eliminar_descuento(
    tree_descuento.selection()
)).pack(side="left", padx=5, pady=5)

# Bucle principal de tkinter
root.mainloop()
