from crear_conexion_bd import conectar_bd

def verificar_usuario(usuario, contraseña):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT rol FROM usuarios WHERE nombre_usuario = ? AND contraseña = ?"
            cursor.execute(consulta, (usuario, contraseña))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]  # Retorna el rol del usuario
            else:
                return None
        except Exception as e:
            print(f"Error en la consulta: {e}")
            return None
        finally:
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos.")
        return None

def crear_usuario(usuario, contraseña, rol):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "INSERT INTO usuarios (nombre_usuario, contraseña, rol) VALUES (?, ?, ?)"
            cursor.execute(consulta, (usuario, contraseña, rol))
            conexion.commit()
            print(f"Usuario '{usuario}' creado exitosamente con rol '{rol}'.")
            return True
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
            return False
        finally:
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos.")
        return False
