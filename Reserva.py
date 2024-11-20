from crear_conexion_bd import conectar_bd

def crear_reserva(id_empleado, id_huesped, id_habitacion, id_servicios_adicionales, ingreso, egreso, importe, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Reserva (ID_Empleado, ID_Huesped, ID_Habitacion, ID_ServiciosAdicionales, Ingreso, Egreso, Importe, Observaciones)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (id_empleado, id_huesped, id_habitacion, id_servicios_adicionales, ingreso, egreso, importe, observaciones))
        conexion.commit()
        conexion.close()

def obtener_reservas():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Reserva")
        reservas = cursor.fetchall()
        conexion.close()
        return reservas

def actualizar_reserva(id_reserva, id_empleado, id_huesped, id_habitacion, id_servicios_adicionales, ingreso, egreso, importe, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Reserva SET ID_Empleado = ?, ID_Huesped = ?, ID_Habitacion = ?, ID_ServiciosAdicionales = ?, Ingreso = ?, Egreso = ?, Importe = ?, Observaciones = ?
            WHERE ID_Reserva = ?
        """, (id_empleado, id_huesped, id_habitacion, id_servicios_adicionales, ingreso, egreso, importe, observaciones, id_reserva))
        conexion.commit()
        conexion.close()

def eliminar_reserva(id_reserva):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Reserva WHERE ID_Reserva = ?", (id_reserva,))
        conexion.commit()
        conexion.close()
