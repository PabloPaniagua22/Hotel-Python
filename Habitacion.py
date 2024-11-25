from crear_conexion_bd import conectar_bd
import random
from faker import Faker
from tkinter import simpledialog, messagebox
import datetime
fake = Faker()

# Función para crear una habitación
def crear_habitacion(cantidad_camas, costo, frigobar, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO HABITACIONES (CANTIDAD_CAMAS, COSTO, FRIGOBAR, OBSERVACIONES)
            VALUES (?, ?, ?, ?)
        """, (cantidad_camas, costo, frigobar, observaciones))
        conexion.commit()
        conexion.close()

# Función para obtener todas las habitaciones
def obtener_habitaciones():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM HABITACIONES")
        habitaciones = cursor.fetchall()
        conexion.close()
        return habitaciones

# Función para actualizar una habitación
def actualizar_habitacion(id_habitacion, cantidad_camas, costo, frigobar, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE HABITACIONES SET CANTIDAD_CAMAS = ?, COSTO = ?, FRIGOBAR = ?, OBSERVACIONES = ?
            WHERE ID_HABITACION = ?
        """, (cantidad_camas, costo, frigobar, observaciones, id_habitacion))
        conexion.commit()
        conexion.close()

# Función para eliminar una habitación
def eliminar_habitacion(id_habitacion):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM HABITACIONES WHERE ID_HABITACION = ?", (id_habitacion,))
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
            'Cantidad_Camas': random.randint(1, 3),
            'Costo': round(random.uniform(50, 200), 2),
            'Frigobar': random.choice([True, False]),
            'Observaciones': fake.text()
        }
        # Insertamos los registros generados en la base de datos
        crear_habitacion(
            habitacion['Cantidad_Camas'], 
            habitacion['Costo'], 
            habitacion['Frigobar'], 
            habitacion['Observaciones']
        )
    
    messagebox.showinfo("Generación Completa", f"Se han generado {cantidad_registros} registros de habitación.")
