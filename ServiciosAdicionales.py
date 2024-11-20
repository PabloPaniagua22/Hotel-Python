from crear_conexion_bd import conectar_bd

def agregar_servicio(id_empleado, tipo, costo, disponible, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO ServicioAdicionales (ID_Empleado, Tipo, Costo, Disponible, Observaciones)
            VALUES (?, ?, ?, ?, ?)
        """, (id_empleado, tipo, costo, disponible, observaciones))
        conexion.commit()
        conexion.close()

def obtener_servicios():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ServicioAdicionales")
        servicios = cursor.fetchall()
        conexion.close()
        return servicios

def actualizar_servicio(id_servicio, id_empleado, tipo, costo, disponible, observaciones):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE ServicioAdicionales SET ID_Empleado = ?, Tipo = ?, Costo = ?, Disponible = ?, Observaciones = ?
            WHERE ID_ServicioAdicionales = ?
        """, (id_empleado, tipo, costo, disponible, observaciones, id_servicio))
        conexion.commit()
        conexion.close()

def eliminar_servicio(id_servicio):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM ServicioAdicionales WHERE ID_ServicioAdicionales = ?", (id_servicio,))
        conexion.commit()
        conexion.close()
