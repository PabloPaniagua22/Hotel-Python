from crear_conexion_bd import conectar_bd
import random
from faker import Faker
from tkinter import simpledialog, messagebox

fake = Faker()

# Crear empleado en la base de datos
def crear_empleado(nombre, apellido, dni, telefono, email, domicilio, tipo_empleado, salario, fecha_contratacion):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO EMPLEADOS (NOMBRE, APELLIDO, DNI, TELEFONO, EMAIL, DOMICILIO, TIPO_EMPLEADO, SALARIO, FECHA_CONTRATACION)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido, dni, telefono, email, domicilio, tipo_empleado, salario, fecha_contratacion))
        conexion.commit()
        conexion.close()

# Obtener todos los empleados
def obtener_empleados():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM EMPLEADOS")
        empleados = cursor.fetchall()
        conexion.close()
        return empleados

# Actualizar empleado
def actualizar_empleado(id_empleado, nombre, apellido, dni, telefono, email, domicilio, tipo_empleado, salario, fecha_contratacion):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE EMPLEADOS SET NOMBRE = ?, APELLIDO = ?, DNI = ?, TELEFONO = ?, EMAIL = ?, DOMICILIO = ?, TIPO_EMPLEADO = ?, SALARIO = ?, FECHA_CONTRATACION = ?
            WHERE ID_EMPLEADO = ?
        """, (nombre, apellido, dni, telefono, email, domicilio, tipo_empleado, salario, fecha_contratacion, id_empleado))
        conexion.commit()
        conexion.close()

# Eliminar empleado
def eliminar_empleado(id_empleado):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM EMPLEADOS WHERE ID_EMPLEADO = ?", (id_empleado,))
        conexion.commit()
        conexion.close()

# Generar empleados con Faker
def generar_empleado():
    cantidad_registros = simpledialog.askinteger("Cantidad de Empleados", "¿Cuántos registros de empleado deseas crear?")

    if cantidad_registros is None or cantidad_registros <= 0:
        messagebox.showerror("Error", "La cantidad de registros debe ser mayor que 0.")
        return

    for _ in range(cantidad_registros):
        empleado = {
            'NOMBRE': fake.first_name(),
            'APELLIDO': fake.last_name(),
            'DNI': fake.unique.ssn(),
            'TELEFONO': fake.phone_number(),
            'EMAIL': fake.email(),
            'DOMICILIO': fake.address(),
            'TIPO_EMPLEADO': random.choice(['Administrativo', 'Recepcionista', 'Mucama', 'Gerente']),
            'SALARIO': round(random.uniform(15000, 50000), 2),
            'FECHA_CONTRATACION': fake.date_this_decade()
        }
        # Insertar empleado en la base de datos
        crear_empleado(
            empleado['NOMBRE'],
            empleado['APELLIDO'],
            empleado['DNI'],
            empleado['TELEFONO'],
            empleado['EMAIL'],
            empleado['DOMICILIO'],
            empleado['TIPO_EMPLEADO'],
            empleado['SALARIO'],
            empleado['FECHA_CONTRATACION']
        )
    
    messagebox.showinfo("Generación Completa", f"Se han generado {cantidad_registros} registros de empleado.")
