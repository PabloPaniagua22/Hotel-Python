from crear_conexion_bd import conectar_bd
import random
from faker import Faker
from tkinter import simpledialog, messagebox
import datetime
fake = Faker()

# Función para crear un presupuesto
def crear_presupuesto(id_reserva, id_huesped, id_habitacion, id_servicio_adicional, ingreso, egreso, importe, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Presupuesto (ID_Reserva, ID_Huesped, ID_Habitacion, ID_ServiciosAdicionales, Ingreso, Egreso, Importe, Observaciones, FechaCreacion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (id_reserva, id_huesped, id_habitacion, id_servicio_adicional, ingreso, egreso, importe, observaciones, datetime.date.today()))
        conexion.commit()
        conexion.close()

# Función para obtener todos los presupuestos
def obtener_presupuestos():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Presupuesto")
        presupuestos = cursor.fetchall()
        conexion.close()
        return presupuestos

# Función para actualizar un presupuesto
def actualizar_presupuesto(id_presupuesto, id_reserva, id_huesped, id_habitacion, id_servicio_adicional, ingreso, egreso, importe, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Presupuesto SET ID_Reserva = ?, ID_Huesped = ?, ID_Habitacion = ?, ID_ServiciosAdicionales = ?, Ingreso = ?, Egreso = ?, Importe = ?, Observaciones = ?
            WHERE ID_Presupuesto = ?
        """, (id_reserva, id_huesped, id_habitacion, id_servicio_adicional, ingreso, egreso, importe, observaciones, id_presupuesto))
        conexion.commit()
        conexion.close()

# Función para eliminar un presupuesto
def eliminar_presupuesto(id_presupuesto):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Presupuesto WHERE ID_Presupuesto = ?", (id_presupuesto,))
        conexion.commit()
        conexion.close()


# Función para generar presupuestos con cantidad definida
def generar_presupuesto():
    cantidad_registros = simpledialog.askinteger("Cantidad de Presupuestos", "¿Cuántos registros de presupuesto deseas crear?")

    if cantidad_registros is None or cantidad_registros <= 0:
        messagebox.showerror("Error", "La cantidad de registros debe ser mayor que 0.")
        return

    for _ in range(cantidad_registros):
        presupuesto = {
            'ID_Reserva': random.randint(1, 100),
            'ID_Huesped': random.randint(1, 100),
            'ID_Habitacion': random.randint(1, 100),
            'ID_ServiciosAdicionales': random.randint(1, 100),
            'Ingreso': fake.date_this_month(),
            'Egreso': fake.date_this_month(),
            'Importe': round(random.uniform(100, 500), 2),
            'Observaciones': fake.text(),
            'FechaCreacion': datetime.date.today()
        }
        # Aquí puedes insertar el registro en la base de datos
    
    messagebox.showinfo("Generación Completa", f"Se han generado {cantidad_registros} registros de presupuesto.")
