import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from tkcalendar import DateEntry
from Empleados import *  # Importar funciones CRUD para empleados

# Configuración de tema
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

# Campos para agregar empleados
campos = [("Nombre", "entry_nombre"), ("Apellido", "entry_apellido"), ("DNI", "entry_DNI"),
          ("Teléfono", "entry_telefono"), ("Email", "entry_email"), ("Dirección", "entry_direccion")]

entries = {}
for i, (label, var) in enumerate(campos):
    ctk.CTkLabel(frame_empleado_nuevo, text=label).grid(row=i, column=0)
    entries[var] = ctk.CTkEntry(frame_empleado_nuevo)
    entries[var].grid(row=i, column=1)

# Campo para Tipo de Empleado
ctk.CTkLabel(frame_empleado_nuevo, text="Tipo de Empleado").grid(row=6, column=0)
combo_tipo_empleado = ctk.CTkComboBox(frame_empleado_nuevo, values=["Administrativo", "Recepcionista", "Mucama", "Gerente"])
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
def agregar_empleado():
    try:
        crear_empleado(
            entries["entry_nombre"].get(),
            entries["entry_apellido"].get(),
            entries["entry_DNI"].get(),
            entries["entry_telefono"].get(),
            entries["entry_email"].get(),
            entries["entry_direccion"].get(),
            combo_tipo_empleado.get(),
            float(entry_salario.get()),
            date_entry_contratacion.get()
        )
        messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
        cargar_empleados()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo agregar el empleado: {e}")

ctk.CTkButton(frame_empleado_nuevo, text="Agregar Empleado", command=agregar_empleado).grid(row=9, column=0, columnspan=2, pady=10)

# Botón para generar Faker
ctk.CTkButton(frame_empleado_nuevo, text="Generar Faker", command=generar_empleado).grid(row=10, column=0, columnspan=2)

# Tabla para ver empleados
frame_ver_empleado = ttk.LabelFrame(tab_verEmpleado, text="Ver Empleado")
frame_ver_empleado.pack(fill="both", expand=True, padx=10, pady=10)

tree_empleado = ttk.Treeview(frame_ver_empleado, columns=("ID", "Nombre", "Apellido", "DNI", "Telefono", "Email", "Direccion", "Tipo Empleado", "Salario", "Fecha Contratacion"), show="headings")
for col in tree_empleado["columns"]:
    tree_empleado.heading(col, text=col)
tree_empleado.pack(fill="both", expand=True)

# Cargar datos de empleados en la tabla
def cargar_empleados():
    for row in tree_empleado.get_children():
        tree_empleado.delete(row)  # Limpia filas existentes

    empleados = obtener_empleados()
    for empleado in empleados:
        # Asegúrate de que todos los datos sean cadenas para evitar errores de formato
        tree_empleado.insert("", "end", values=[str(dato) for dato in empleado])

# Función para eliminar empleado
def eliminar_empleado():
    try:
        selected_item = tree_empleado.selection()[0]
        empleado_id = tree_empleado.item(selected_item, "values")[0]
        eliminar_empleado(int(empleado_id))
        tree_empleado.delete(selected_item)
        messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un empleado para eliminar.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el empleado: {e}")

# Función para editar empleado (interfaz simplificada)
def editar_empleado():
    try:
        selected_item = tree_empleado.selection()[0]
        empleado = tree_empleado.item(selected_item, "values")
        # Implementa aquí una ventana emergente para editar los campos y actualizar en la base de datos
        messagebox.showinfo("Info", f"Editar empleado con ID {empleado[0]} aún no implementado.")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un empleado para editar.")

# Botones para editar y eliminar empleados
ctk.CTkButton(frame_ver_empleado, text="Editar", command=editar_empleado).pack(side="left", padx=5, pady=5)
ctk.CTkButton(frame_ver_empleado, text="Eliminar", command=eliminar_empleado).pack(side="left", padx=5, pady=5)

# Cargar empleados al iniciar
cargar_empleados()

# Bucle principal de tkinter
root.mainloop()
