from funcionesLogin import verificar_usuario, crear_usuario
import customtkinter as ctk
import subprocess  # Para ejecutar otros archivos Python

# Función para iniciar sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    rol = verificar_usuario(usuario, contraseña)
    
    if rol:
        if rol == "Gerente":
            abrir_vista_gerente()
        elif rol == "Recepcionista":
            abrir_vista_recepcionista()
        else:
            label_resultado.configure(text="Rol no definido.")
    else:
        label_resultado.configure(text="Usuario o contraseña incorrectos.")

# Función para abrir la vista del gerente
def abrir_vista_gerente():
    app.withdraw()  # Cierra la ventana actual
    subprocess.Popen(["python", "Tk_Principal_Gerente.py"])  # Ejecuta el archivo principal del gerente

# Función para abrir la vista del recepcionista
def abrir_vista_recepcionista():
    app.withdraw()  # Cierra la ventana actual
    subprocess.Popen(["python", "Tk_Principal_Empleado.py"])  # Ejecuta el archivo principal del recepcionista

# Función para abrir la ventana de creación de usuarios
def abrir_ventana_crear_usuario():
    ventana_crear = ctk.CTkToplevel(app)
    ventana_crear.geometry("300x250")
    ventana_crear.title("Crear Usuario")
    
    # Etiqueta y entrada de Usuario
    label_nuevo_usuario = ctk.CTkLabel(ventana_crear, text="Usuario:")
    label_nuevo_usuario.pack(pady=5)
    entry_nuevo_usuario = ctk.CTkEntry(ventana_crear)
    entry_nuevo_usuario.pack(pady=5)

    # Etiqueta y entrada de Contraseña
    label_nueva_contraseña = ctk.CTkLabel(ventana_crear, text="Contraseña:")
    label_nueva_contraseña.pack(pady=5)
    entry_nueva_contraseña = ctk.CTkEntry(ventana_crear, show="*")
    entry_nueva_contraseña.pack(pady=5)

    # Desplegable para seleccionar rol
    label_rol = ctk.CTkLabel(ventana_crear, text="Rol:")
    label_rol.pack(pady=5)
    combobox_rol = ctk.CTkComboBox(ventana_crear, values=["Gerente", "Recepcionista"])
    combobox_rol.pack(pady=5)

    # Función para guardar nuevo usuario
    def guardar_usuario():
        nuevo_usuario = entry_nuevo_usuario.get()
        nueva_contraseña = entry_nueva_contraseña.get()
        rol_seleccionado = combobox_rol.get()
        
        if nuevo_usuario and nueva_contraseña and rol_seleccionado:
            exito = crear_usuario(nuevo_usuario, nueva_contraseña, rol_seleccionado)
            if exito:
                ctk.CTkLabel(ventana_crear, text="Usuario creado exitosamente.", text_color="green").pack(pady=5)
            else:
                ctk.CTkLabel(ventana_crear, text="Error al crear el usuario.", text_color="red").pack(pady=5)
        else:
            ctk.CTkLabel(ventana_crear, text="Todos los campos son obligatorios.", text_color="red").pack(pady=5)

    # Botón para guardar
    boton_guardar = ctk.CTkButton(ventana_crear, text="Guardar", command=guardar_usuario)
    boton_guardar.pack(pady=10)

# Interfaz gráfica principal
app = ctk.CTk()
app.geometry("300x300")
app.title("Login")

label_usuario = ctk.CTkLabel(app, text="Usuario:")
label_usuario.pack(pady=5)

entry_usuario = ctk.CTkEntry(app)
entry_usuario.pack(pady=5)

label_contraseña = ctk.CTkLabel(app, text="Contraseña:")
label_contraseña.pack(pady=5)

entry_contraseña = ctk.CTkEntry(app, show="*")
entry_contraseña.pack(pady=5)

boton_login = ctk.CTkButton(app, text="Iniciar Sesión", command=iniciar_sesion)
boton_login.pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=5)

# Botón para crear un nuevo usuario
boton_crear_usuario = ctk.CTkButton(app, text="Crear Usuario", command=abrir_ventana_crear_usuario)
boton_crear_usuario.pack(pady=10)

app.mainloop()
