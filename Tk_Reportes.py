import tkinter as tk
import customtkinter as ctk
import subprocess
import os


class ReportesMenu:
    def __init__(self):
        # Configuración del tema
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Configuración de la ventana principal
        self.root = ctk.CTk()
        self.root.title("Reportes del Hotel")
        self.root.geometry("1200x700")

        # Frame principal con diseño de grid
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        titulo = ctk.CTkLabel(
            self.main_frame, 
            text="Reportes del Hotel", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=20)

        # Frame para los botones
        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(expand=True)

        # Crear botones con íconos
        self.create_module_button(
            button_frame,
            "Asistencia de Empleados",
            "Generar reporte de asistencia",
            0, 1,
            lambda: self.abrir_modulo("Tk_AsistenciaEmpleados.py")
        )

        self.create_module_button(
            button_frame,
            "Ingreso por Servicios Adicionales",
            "Generar reporte de ingresos por servicios",
            0, 2,
            lambda: self.abrir_modulo("Tk_IngresoServiciosAdicionales.py")
        )

        self.create_module_button(
            button_frame,
            "Reservas Realizadas",
            "Generar reporte de reservas realizadas",
            0, 3,
            lambda: self.abrir_modulo("Tk_ReservasRealizadas.py")
        )

        # Footer con información
        footer = ctk.CTkLabel(
            self.main_frame,
            text="© 2024 Sistema de Reportes - Todos los derechos reservados",
            font=ctk.CTkFont(size=10)
        )
        footer.pack(side="bottom", pady=10)

    def create_module_button(self, parent, title, description, row, col, command):
        # Frame para cada módulo
        module_frame = ctk.CTkFrame(parent)
        module_frame.grid(row=row, column=col, padx=20, pady=20)

        # Botón principal
        button = ctk.CTkButton(
            module_frame,
            text=title,
            font=ctk.CTkFont(size=16, weight="bold"),
            width=250,
            height=100,
            command=command
        )
        button.pack(padx=20, pady=(20, 10))

        # Descripción
        description_label = ctk.CTkLabel(
            module_frame,
            text=description,
            font=ctk.CTkFont(size=12),
            wraplength=200
        )
        description_label.pack(padx=20, pady=(0, 20))

    def abrir_modulo(self, archivo):
        try:
            # Obtener la ruta absoluta del archivo actual
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Construir la ruta al módulo
            module_path = os.path.join(current_dir, archivo)
            
            # Verificar si el archivo existe
            if os.path.exists(module_path):
                subprocess.Popen(['python', module_path])
            else:
                tk.messagebox.showerror("Error", f"No se encuentra el archivo: {archivo}")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error al abrir el módulo: {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ReportesMenu()
    app.run()
