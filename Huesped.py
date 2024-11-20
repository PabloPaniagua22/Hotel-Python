from crear_conexion_bd import conectar_bd
from faker import Faker
import random
from tkinter import simpledialog, messagebox

fake = Faker()

def crear_huesped(dni, cuil, nombre, apellido, telefono, mail, domicilio, condicion_iva, tipo_cliente, fnac, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()

        # Verificar si el DNI ya existe
        cursor.execute("SELECT COUNT(*) FROM Huesped WHERE DNI = ?", (dni,))
        if cursor.fetchone()[0] > 0:
            print(f"Error: El DNI {dni} ya existe en la base de datos.")
            return

        # Insertar si no hay duplicados
        cursor.execute("""
            INSERT INTO Huesped (DNI, CUIL, Nombre, Apellido, Telefono, Mail, Domicilio, Condicion_IVA, Tipo_Cliente, FNAC, Observaciones)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (dni, cuil, nombre, apellido, telefono, mail, domicilio, condicion_iva, tipo_cliente, fnac, observaciones))
        conexion.commit()
        conexion.close()


def obtener_huespedes(treeview):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Huesped")
        huespedes = cursor.fetchall()
        conexion.close()

        # Limpiar el Treeview antes de insertar nuevos datos
        for item in treeview.get_children():
            treeview.delete(item)

        # Insertar los datos en el Treeview
        for huesped in huespedes:
            treeview.insert("", "end", values=huesped)


def actualizar_huesped(id_huesped, dni, cuil, nombre, apellido, telefono, mail, domicilio, condicion_iva, tipo_cliente, fnac, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Huesped SET DNI = ?, CUIL = ?, Nombre = ?, Apellido = ?, Telefono = ?, Mail = ?, Domicilio = ?, Condicion_IVA = ?, Tipo_Cliente = ?, FNAC = ?, Observaciones = ?
            WHERE ID_Huesped = ?
        """, (dni, cuil, nombre, apellido, telefono, mail, domicilio, condicion_iva, tipo_cliente, fnac, observaciones, id_huesped))
        conexion.commit()
        conexion.close()

def eliminar_huesped(id_huesped):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Huesped WHERE ID_Huesped = ?", (id_huesped,))
        conexion.commit()
        conexion.close()
        
        
def generar_huesped():
    cantidad_registros = simpledialog.askinteger("Cantidad de Registros", "¿Cuántos registros deseas crear?")
    
    if cantidad_registros is None:
        return

    if cantidad_registros <= 0:
        messagebox.showerror("Error", "La cantidad de registros debe ser mayor que 0.")
        return

    for _ in range(cantidad_registros):
        # Generar datos de huésped con Faker
        telefono = fake.phone_number()
        
        # Limitar el tamaño del teléfono para que no supere los 20 caracteres (ajusta si es necesario)
        telefono = telefono[:20]
        
        huesped = {
            'DNI': fake.unique.ssn(),
            'CUIL': fake.unique.ssn(),
            'Nombre': fake.first_name(),
            'Apellido': fake.last_name(),
            'Telefono': telefono,  # Aquí se usa el teléfono limitado
            'Mail': fake.email(),
            'Domicilio': fake.address(),
            'Condicion_IVA': random.choice(['Responsable Inscripto', 'Monotributista', 'Exento']),
            'Tipo_Cliente': random.choice(['VIP', 'Frecuente', 'Ocasional']),
            'FNAC': fake.date_of_birth(),
            'Observaciones': fake.text()
        }

        # Conectar a la base de datos
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Huesped (DNI, CUIL, Nombre, Apellido, Telefono, Mail, Domicilio, Condicion_IVA, Tipo_Cliente, FNAC, Observaciones)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (huesped['DNI'], huesped['CUIL'], huesped['Nombre'], huesped['Apellido'], huesped['Telefono'], 
                  huesped['Mail'], huesped['Domicilio'], huesped['Condicion_IVA'], huesped['Tipo_Cliente'], 
                  huesped['FNAC'], huesped['Observaciones']))
            conexion.commit()
            conexion.close()

    messagebox.showinfo("Generación Completa", f"Se han generado {cantidad_registros} registros.")
