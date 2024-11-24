from crear_conexion_bd import conectar_bd
from faker import Faker
import random
from tkinter import simpledialog, messagebox
import customtkinter as ctk


fake = Faker()

# Creacion de Huesped 
def crear_huesped(dni, cuil, nombre, apellido, telefono, email, domicilio, condicion_iva, tipo_huesped, fecha_nacimiento, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()

        # Verificar si el DNI ya existe
        cursor.execute("SELECT COUNT(*) FROM HUESPEDES WHERE DNI = ?", (dni,))
        if cursor.fetchone()[0] > 0:
            print(f"Error: El DNI {dni} ya existe en la base de datos.")
            return

        # Insertar nuevo huésped
        cursor.execute("""
            INSERT INTO HUESPEDES (DNI, CUIL, NOMBRE, APELLIDO, TELEFONO, EMAIL, DOMICILIO, CONDICION_IVA, TIPO_HUESPED, FECHA_NACIMIENTO, OBSERVACIONES)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (dni, cuil, nombre, apellido, telefono, email, domicilio, condicion_iva, tipo_huesped, fecha_nacimiento, observaciones))
        conexion.commit()
        conexion.close()
        print(f"Huésped con DNI {dni} creado exitosamente.")

#Obtiene los huesped de la tabla 
def obtener_huespedes(treeview):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = """
            SELECT 
                ID_HUESPED, DNI, CUIL, NOMBRE, APELLIDO, TELEFONO, EMAIL, DOMICILIO, 
                CONDICION_IVA, TIPO_HUESPED, FECHA_NACIMIENTO, OBSERVACIONES
            FROM HUESPEDES
        """
        cursor.execute(query)
        huespedes = cursor.fetchall()
        
        # Limpiar Treeview antes de cargar los nuevos datos
        for item in treeview.get_children():
            treeview.delete(item)
        
        # Insertar datos en el Treeview
        for huesped in huespedes:
            # Convertir valores a cadena (o manejar valores nulos)
            datos_limpiados = [str(valor) if valor is not None else '' for valor in huesped]
            treeview.insert("", "end", values=datos_limpiados)

    except Exception as e:
        print(f"Error al obtener huéspedes: {e}")
    finally:
        if 'conexion' in locals() and conexion:
            conexion.close()

def editar_huesped(treeview):
    seleccion = treeview.selection()  # Obtener selección actual
    if not seleccion:
        print("No se ha seleccionado ningún huésped.")
        return

    # Obtener valores del huésped seleccionado
    item = treeview.item(seleccion[0])
    valores = item['values']  # Lista con los valores seleccionados

    # Crear ventana emergente para editar
    ventana_editar = ctk.CTkToplevel()
    ventana_editar.title("Editar Huésped")
    ventana_editar.geometry("400x600")

    # Campos para editar
    campos = ["ID_HUESPED", "DNI", "CUIL", "NOMBRE", "APELLIDO", "TELEFONO", "EMAIL", "DOMICILIO", "CONDICION_IVA", "TIPO_HUESPED", "FECHA_NACIMIENTO", "OBSERVACIONES"]
    entradas = {}  # Diccionario para almacenar las entradas

    for i, campo in enumerate(campos):
        ctk.CTkLabel(ventana_editar, text=campo).grid(row=i, column=0, padx=10, pady=5)
        entrada = ctk.CTkEntry(ventana_editar, width=300)
        entrada.grid(row=i, column=1, padx=10, pady=5)
        entrada.insert(0, valores[i])  # Rellenar con valor actual
        entradas[campo] = entrada

    # Botón para guardar cambios
    def guardar_cambios():
        try:
            # Obtener datos actualizados de las entradas
            datos = [entradas[campo].get() for campo in campos]

            # Conectar y ejecutar la actualización
            conexion = conectar_bd()
            cursor = conexion.cursor()
            query = """
                UPDATE HUESPEDES 
                SET DNI = ?, CUIL = ?, NOMBRE = ?, APELLIDO = ?, TELEFONO = ?, EMAIL = ?, DOMICILIO = ?, 
                    CONDICION_IVA = ?, TIPO_HUESPED = ?, FECHA_NACIMIENTO = ?, OBSERVACIONES = ?
                WHERE ID_HUESPED = ?
            """
            cursor.execute(query, (
                datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7],
                datos[8], datos[9], datos[10], datos[11], int(datos[0])
            ))
            conexion.commit()
            print(f"Huésped con ID {datos[0]} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar huésped: {e}")
        finally:
            if 'conexion' in locals():
                conexion.close()

        ventana_editar.destroy()  # Cerrar ventana
        obtener_huespedes(treeview)  # Refrescar tabla

    ctk.CTkButton(ventana_editar, text="Guardar", command=guardar_cambios).grid(row=len(campos), column=0, columnspan=2, pady=10)



# Elimina del huesped poniendo con el ID del Huesped
def eliminar_huesped(id_huesped):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM HUESPEDES WHERE ID_HUESPED = ?", (int(id_huesped),))  # Aseguramos que sea entero
        conexion.commit()
        print(f"Huésped con ID {id_huesped} eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar huésped: {e}")
    finally:
        if 'conexion' in locals():
            conexion.close()


# Generador de Huesped por parte del facker 
def generar_huesped():
    cantidad_registros = simpledialog.askinteger("Cantidad de Registros", "¿Cuántos registros deseas crear?")
    
    if cantidad_registros is None or cantidad_registros <= 0:
        messagebox.showerror("Error", "La cantidad de registros debe ser mayor que 0.")
        return

    for _ in range(cantidad_registros):
        # Generar datos con Faker
        telefono = fake.phone_number()[:20]  # Limitar a 20 caracteres
        huesped = {
            'DNI': fake.unique.random_number(digits=8),
            'CUIL': fake.unique.random_number(digits=11),
            'NOMBRE': fake.first_name(),
            'APELLIDO': fake.last_name(),
            'TELEFONO': telefono,
            'EMAIL': fake.email(),
            'DOMICILIO': fake.address(),
            'CONDICION_IVA': random.choice(['Responsable Inscripto', 'Monotributista', 'Exento', 'Consumidor Final']),
            'TIPO_HUESPED': random.choice(['VIP', 'Gold', 'Platinum', 'Corporativo']),
            'FECHA_NACIMIENTO': fake.date_of_birth(minimum_age=18, maximum_age=80),
            'OBSERVACIONES': fake.text()
        }

        # Conectar a la base de datos
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO HUESPEDES (DNI, CUIL, NOMBRE, APELLIDO, TELEFONO, EMAIL, DOMICILIO, CONDICION_IVA, TIPO_HUESPED, FECHA_NACIMIENTO, OBSERVACIONES)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (huesped['DNI'], huesped['CUIL'], huesped['NOMBRE'], huesped['APELLIDO'], huesped['TELEFONO'], huesped['EMAIL'], huesped['DOMICILIO'], 
                 huesped['CONDICION_IVA'], huesped['TIPO_HUESPED'], huesped['FECHA_NACIMIENTO'], huesped['OBSERVACIONES']))
            conexion.commit()
            conexion.close()

    messagebox.showinfo("Generación Completa", f"Se han generado {cantidad_registros} registros.")
