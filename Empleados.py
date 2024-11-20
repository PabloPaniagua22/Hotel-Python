from crear_conexion_bd import conectar_bd
import random
from faker import Faker
from tkinter import simpledialog, messagebox
import datetime

fake = Faker()
def crear_empleado(nombre, apellido, dni, telefono, email, direccion, tipo_empleado, salario, fecha_contratacion):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Empleado (Nombre, Apellido, DNI, Telefono, Email, Direccion, Tipo_Empleado, Salario, Fecha_Contratacion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido, dni, telefono, email, direccion, tipo_empleado, salario, fecha_contratacion))
        conexion.commit()
        conexion.close()

def obtener_empleados():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Empleado")
        empleados = cursor.fetchall()
        conexion.close()
        return empleados

def actualizar_empleado(id_empleado, nombre, apellido, dni, telefono, email, direccion, tipo_empleado, salario, fecha_contratacion):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Empleado SET Nombre = ?, Apellido = ?, DNI = ?, Telefono = ?, Email = ?, Direccion = ?, Tipo_Empleado = ?, Salario = ?, Fecha_Contratacion = ?
            WHERE ID_Empleado = ?
        """, (nombre, apellido, dni, telefono, email, direccion, tipo_empleado, salario, fecha_contratacion, id_empleado))
        conexion.commit()
        conexion.close()

def eliminar_empleado(id_empleado):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Empleado WHERE ID_Empleado = ?", (id_empleado,))
        conexion.commit()
        conexion.close()

# Función para generar empleados con cantidad definida
def generar_empleado():
    cantidad_registros = simpledialog.askinteger("Cantidad de Empleados", "¿Cuántos registros de empleado deseas crear?")

    if cantidad_registros is None or cantidad_registros <= 0:
        messagebox.showerror("Error", "La cantidad de registros debe ser mayor que 0.")
        return

    for _ in range(cantidad_registros):
        empleado = {
            'Nombre': fake.first_name(),
            'Apellido': fake.last_name(),
            'DNI': fake.unique.ssn(),
            'Telefono': fake.phone_number(),
            'Email': fake.email(),
            'Direccion': fake.address(),
            'Tipo_Empleado': random.choice(['Administrativo', 'Recepcionista', 'Limpieza', 'Gerente']),
            'Salario': round(random.uniform(15000, 50000), 2),
            'Fecha_Contratacion': fake.date_this_decade()
        }
        # Aquí puedes insertar el registro en la base de datos
    
    messagebox.showinfo("Generación Completa", f"Se han generado {cantidad_registros} registros de empleado.")