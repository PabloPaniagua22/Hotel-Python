from crear_conexion_bd import conectar_bd

def agregar_servicio(tipo_sa, costo, observaciones=None):
    """
    Agrega un nuevo servicio adicional a la tabla SERVICIOS_ADICIONALES.
    """
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO SERVICIOS_ADICIONALES (TIPO_SA, COSTO, OBSERVACIONES)
            VALUES (?, ?, ?)
        """, (tipo_sa, costo, observaciones))
        conexion.commit()
        conexion.close()

def obtener_servicios():
    """
    Obtiene todos los registros de la tabla SERVICIOS_ADICIONALES.
    """
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM SERVICIOS_ADICIONALES")
        servicios = cursor.fetchall()
        conexion.close()
        return servicios

def actualizar_servicio(id_sa, tipo_sa, costo, observaciones=None):
    """
    Actualiza un servicio adicional existente en la tabla SERVICIOS_ADICIONALES.
    """
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE SERVICIOS_ADICIONALES
            SET TIPO_SA = ?, COSTO = ?, OBSERVACIONES = ?
            WHERE ID_SA = ?
        """, (tipo_sa, costo, observaciones, id_sa))
        conexion.commit()
        conexion.close()

def eliminar_servicio(id_sa):
    """
    Elimina un servicio adicional de la tabla SERVICIOS_ADICIONALES.
    """
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM SERVICIOS_ADICIONALES WHERE ID_SA = ?", (id_sa,))
        conexion.commit()
        conexion.close()
