from crear_conexion_bd import conectar_bd
import random
from faker import Faker
from tkinter import simpledialog, messagebox
import datetime
fake = Faker()

# Función para crear una habitación
def crear_habitacion(cantidad_huespedes, costo, cantidad_camas, cantidad_baños, frigobar, disponibilidad, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Habitacion (Cantidad_Huespedes, Costo, Cantidad_Camas, Cantidad_Baños, Frigobar, Disponibilidad, Observaciones)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (cantidad_huespedes, costo, cantidad_camas, cantidad_baños, frigobar, disponibilidad, observaciones))
        conexion.commit()
        conexion.close()

# Función para obtener todas las habitaciones
def obtener_habitaciones():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Habitacion")
        habitaciones = cursor.fetchall()
        conexion.close()
        return habitaciones

# Función para actualizar una habitación
def actualizar_habitacion(id_habitacion, cantidad_huespedes, costo, cantidad_camas, cantidad_baños, frigobar, disponibilidad, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Habitacion SET Cantidad_Huespedes = ?, Costo = ?, Cantidad_Camas = ?, Cantidad_Baños = ?, Frigobar = ?, Disponibilidad = ?, Observaciones = ?
            WHERE ID_Habitacion = ?
        """, (cantidad_huespedes, costo, cantidad_camas, cantidad_baños, frigobar, disponibilidad, observaciones, id_habitacion))
        conexion.commit()
        conexion.close()

# Función para eliminar una habitación
def eliminar_habitacion(id_habitacion):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Habitacion WHERE ID_Habitacion = ?", (id_habitacion,))
        conexion.commit()
        conexion.close()

# Función para generar habitaciones con cantidad definida
def generar_habitacion():
    cantidad_registros = simpledialog.askinteger("Cantidad de Habitaciones", "¿Cuántos registros de habitación deseas crear?")

    if cantidad_registros is None or cantidad_registros <= 0:
        messagebox.showerror("Error", "La cantidad de registros debe ser mayor que 0.")
        return

    for _ in range(cantidad_registros):
        habitacion = {
            'Cantidad_Huespedes': random.randint(1, 4),
            'Costo': round(random.uniform(50, 200), 2),
            'Cantidad_Camas': random.randint(1, 3),
            'Cantidad_Baños': random.randint(1, 2),
            'Frigobar': random.choice([True, False]),
            'Disponibilidad': random.choice([True, False]),
            'Observaciones': fake.text()
        }
        # Aquí puedes insertar el registro en la base de datos
    
    messagebox.showinfo("Generación Completa", f"Se han generado {cantidad_registros} registros de habitación.")
