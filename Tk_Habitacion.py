import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from faker import Faker

# Importar funciones CRUD
from Habitacion import *

# Configuración de Faker
faker = Faker()

# Configuración de tema de sistema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("1000x700")
root.title("Sistema de Gestión de Hotel - Habitaciones")

# Creación de Tabs
tabControl = ttk.Notebook(root)
tab_habitacion = ttk.Frame(tabControl)
tab_verHabitacion = ttk.Frame(tabControl)
tabControl.add(tab_habitacion, text="Habitación")
tabControl.add(tab_verHabitacion, text="Ver Habitaciones")
tabControl.pack(expand=1, fill="both")

# Sección "Habitación" (Agregar Habitación)
frame_habitacion_nueva = ttk.LabelFrame(tab_habitacion, text="Nueva Habitación")
frame_habitacion_nueva.pack(fill="x", padx=20, pady=20)

# Campo Costo
ctk.CTkLabel(frame_habitacion_nueva, text="Costo").grid(row=0, column=0)
entry_costo = ctk.CTkEntry(frame_habitacion_nueva)
entry_costo.grid(row=0, column=1)

# Campo Cantidad de Camas
ctk.CTkLabel(frame_habitacion_nueva, text="Cantidad de Camas").grid(row=1, column=0)
entry_cantidad_camas = ctk.CTkEntry(frame_habitacion_nueva)
entry_cantidad_camas.grid(row=1, column=1)

# Campo Frigobar
ctk.CTkLabel(frame_habitacion_nueva, text="Frigobar").grid(row=2, column=0)
combo_frigobar = ctk.CTkComboBox(frame_habitacion_nueva, values=["Sí", "No"])
combo_frigobar.grid(row=2, column=1)

# Campo Observaciones
ctk.CTkLabel(frame_habitacion_nueva, text="Observaciones").grid(row=3, column=0)
entry_observaciones = ctk.CTkEntry(frame_habitacion_nueva, height=100)
entry_observaciones.grid(row=3, column=1)

# Función para agregar habitación
def agregar_habitacion_gui():
    try:
        crear_habitacion(
            int(entry_cantidad_camas.get()),
            float(entry_costo.get()),
            1 if combo_frigobar.get() == "Sí" else 0,
            entry_observaciones.get()
        )
        actualizar_tabla()
        messagebox.showinfo("Éxito", "Habitación agregada correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al agregar habitación: {str(e)}")

# Botón para agregar la habitación
ctk.CTkButton(frame_habitacion_nueva, text="Agregar Habitación", 
              command=agregar_habitacion_gui).grid(row=4, column=0, columnspan=2, pady=10)

# Botón para generar datos faker
ctk.CTkButton(frame_habitacion_nueva, text="Generar Datos Aleatorios", 
              command=generar_habitacion).grid(row=5, column=0, columnspan=2)

# Tabla para ver habitaciones
frame_ver_habitacion = ttk.LabelFrame(tab_verHabitacion, text="Ver Habitaciones")
frame_ver_habitacion.pack(fill="both", expand=True, padx=10, pady=10)

tree_habitacion = ttk.Treeview(frame_ver_habitacion, 
                              columns=("ID", "Costo", "Cantidad_Camas", "Frigobar", "Observaciones"),
                              show="headings")

# Configurar las columnas
tree_habitacion.heading("ID", text="ID")
tree_habitacion.heading("Costo", text="Costo")
tree_habitacion.heading("Cantidad_Camas", text="Cantidad Camas")
tree_habitacion.heading("Frigobar", text="Frigobar")
tree_habitacion.heading("Observaciones", text="Observaciones")

# Ajustar el ancho de las columnas
for col in tree_habitacion["columns"]:
    tree_habitacion.column(col, width=120)

tree_habitacion.pack(fill="both", expand=True)

# Función para actualizar la tabla
def actualizar_tabla():
    for item in tree_habitacion.get_children():
        tree_habitacion.delete(item)
    habitaciones = obtener_habitaciones()
    for habitacion in habitaciones:
        # Convertir valores booleanos a texto
        frigobar = "Sí" if habitacion[3] == 1 else "No"
        
        # Los valores de la habitación incluyen: ID, Costo, Cantidad_Camas, Frigobar, Observaciones
        valores = [habitacion[0], habitacion[2], habitacion[1], frigobar, habitacion[4]]
        tree_habitacion.insert('', 'end', values=valores)

# Función para editar habitación seleccionada
def editar_habitacion_seleccionada():
    seleccion = tree_habitacion.selection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Por favor seleccione una habitación")
        return
    
    item = tree_habitacion.item(seleccion[0])
    valores = item['values']
    
    # Crear ventana de edición
    ventana_edicion = ctk.CTkToplevel()
    ventana_edicion.title("Editar Habitación")
    ventana_edicion.geometry("400x500")
    
    # Campos de edición
    ctk.CTkLabel(ventana_edicion, text="Costo").pack()
    edit_costo = ctk.CTkEntry(ventana_edicion)
    edit_costo.insert(0, valores[1])
    edit_costo.pack()
    
    ctk.CTkLabel(ventana_edicion, text="Cantidad de Camas").pack()
    edit_camas = ctk.CTkEntry(ventana_edicion)
    edit_camas.insert(0, valores[2])
    edit_camas.pack()
    
    ctk.CTkLabel(ventana_edicion, text="Frigobar").pack()
    edit_frigobar = ctk.CTkComboBox(ventana_edicion, values=["Sí", "No"])
    edit_frigobar.set(valores[3])
    edit_frigobar.pack()
    
    ctk.CTkLabel(ventana_edicion, text="Observaciones").pack()
    edit_observaciones = ctk.CTkEntry(ventana_edicion, height=100)
    edit_observaciones.insert(0, valores[4])
    edit_observaciones.pack()
    
    def guardar_cambios():
        try:
            actualizar_habitacion(
                valores[0],
                float(edit_costo.get()),
                int(edit_camas.get()),
                1 if edit_frigobar.get() == "Sí" else 0,
                edit_observaciones.get()
            )
            actualizar_tabla()
            ventana_edicion.destroy()
            messagebox.showinfo("Éxito", "Habitación actualizada correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar habitación: {str(e)}")
    
    ctk.CTkButton(ventana_edicion, text="Guardar Cambios", 
                  command=guardar_cambios).pack(pady=10)

# Función para eliminar habitación
def eliminar_habitacion_seleccionada():
    seleccion = tree_habitacion.selection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Por favor seleccione una habitación")
        return
    
    if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta habitación?"):
        item = tree_habitacion.item(seleccion[0])
        eliminar_habitacion(item['values'][0])
        actualizar_tabla()
        messagebox.showinfo("Éxito", "Habitación eliminada correctamente")

# Botones de edición y eliminación
ctk.CTkButton(frame_ver_habitacion, text="Editar", 
              command=editar_habitacion_seleccionada).pack(side="left", padx=5, pady=5)
ctk.CTkButton(frame_ver_habitacion, text="Eliminar", 
              command=eliminar_habitacion_seleccionada).pack(side="left", padx=5, pady=5)

# Llamada inicial para mostrar habitaciones en la tabla
actualizar_tabla()

# Ejecutar la interfaz
root.mainloop()
