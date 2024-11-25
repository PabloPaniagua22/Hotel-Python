from crear_conexion_bd import conectar_bd

# Crear un nuevo descuento
def crear_descuento(tipo_huesped, descuento):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO DESCUENTOS (TIPO_HUESPED, DESCUENTO)
            VALUES (?, ?)
        """, (tipo_huesped, descuento))
        conexion.commit()
        conexion.close()

# Obtener todos los descuentos
def obtener_descuentos():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM DESCUENTOS")
        descuentos = cursor.fetchall()
        conexion.close()
        return descuentos

# Actualizar un descuento
def actualizar_descuento(id_descuento, tipo_huesped, descuento):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE DESCUENTOS
            SET TIPO_HUESPED = ?, DESCUENTO = ?
            WHERE ID_DESCUENTO = ?
        """, (tipo_huesped, descuento, id_descuento))
        conexion.commit()
        conexion.close()

# Eliminar un descuento
def eliminar_descuento(id_descuento):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM DESCUENTOS WHERE ID_DESCUENTO = ?", (id_descuento,))
        conexion.commit()
        conexion.close()
