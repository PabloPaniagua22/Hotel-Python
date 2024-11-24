""" 
Esta función es utilizada en el resto del código 
    para establecer la conexión con la base de datos 

    Por ejemplo, importando en otro programa
        de la siguiente manera:
    
    from crear_conexion_bd import conectar_bd
    
"""

import pyodbc
    
# def conectar_bd(server='TSSIT01', database='reservahotel1', usuario='Soporte', contrasena='Instituto_2023'):
#     try:       
#         connection_string = (
#             'DRIVER={ODBC Driver 17 for SQL Server};'
#             f'SERVER={server};'
#             f'DATABASE={database};'
#             f'UID={usuario};'
#             f'PWD={contrasena};'
#         )
#         connection = pyodbc.connect(connection_string)
#         print('Conexión Exitosa a la base de datos')
#         return connection
#     except pyodbc.Error as e:
#         print(f"Error al conectar a la base de datos: {e}")
#         print(f"Detalles del error: {str(e)}")
#         return None



def conectar_bd(server='(localdb)\\PaniG5', database='RESERVA_HOTEL', trusted_connection=True, usuario='', contrasena=''):
    try:
        # Construcción de la cadena de conexión
        if trusted_connection:
            connection_string = (
                'DRIVER={ODBC Driver 17 for SQL Server};'
                f'SERVER={server};'
                f'DATABASE={database};'
                'Trusted_Connection=yes;'
            )
        else:
            connection_string = (
                'DRIVER={ODBC Driver 17 for SQL Server};'
                f'SERVER={server};'
                f'DATABASE={database};'
                f'UID={usuario};'
                f'PWD={contrasena};'
            )
        
        # Intento de conexión
        connection = pyodbc.connect(connection_string)
        print('Conexión Exitosa a la base de datos')
        return connection

    except pyodbc.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        print(f"Detalles del error: {str(e)}")
        return None

# Llamada a la función
conexion = conectar_bd()
if conexion:
    # Si la conexión es exitosa, puedes usarla
    print("Listo para operar con la base de datos")

