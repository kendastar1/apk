import tkinter as tk
from tkinter import messagebox
import os
import subprocess  # Importamos el módulo para ejecutar otro archivo Python

# Nombre del archivo para almacenar las credenciales
ARCHIVO_CREDENCIALES = "usuarios.txt"

# Función para verificar las credenciales de inicio de sesión
def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    # Leer el archivo de credenciales y verificar si existe la combinación de usuario y contraseña
    if os.path.exists(ARCHIVO_CREDENCIALES):
        with open(ARCHIVO_CREDENCIALES, "r") as archivo:
            for linea in archivo:
                usuario_guardado, contrasena_guardada = linea.strip().split(",")
                if usuario == usuario_guardado and contrasena == contrasena_guardada:
                    messagebox.showinfo("Login", "Inicio de sesión exitoso")
                    
                    # Abrir el archivo inicio.py
                    ventana.destroy()  # Cerrar la ventana de login
                    subprocess.Popen(["python", "inicio.py"])  # Ejecutar inicio.py
                    return
    messagebox.showerror("Login", "Usuario o contraseña incorrectos")

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    if usuario and contrasena:
        # Verificar si el usuario ya existe en el archivo
        if os.path.exists(ARCHIVO_CREDENCIALES):
            with open(ARCHIVO_CREDENCIALES, "r") as archivo:
                for linea in archivo:
                    usuario_guardado, _ = linea.strip().split(",")
                    if usuario == usuario_guardado:
                        messagebox.showwarning("Registro", "El usuario ya existe.")
                        return
        
        # Guardar el nuevo usuario y contraseña en el archivo
        with open(ARCHIVO_CREDENCIALES, "a") as archivo:
            archivo.write(f"{usuario},{contrasena}\n")
        messagebox.showinfo("Registro", "Usuario registrado con éxito")
        entry_usuario.delete(0, tk.END)
        entry_contrasena.delete(0, tk.END)
    else:
        messagebox.showwarning("Registro", "Por favor, ingrese un usuario y una contraseña.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("300x500")  # Tamaño de la ventana (similar a un teléfono)
ventana.configure(bg="#2c3e50")  # Fondo azul oscuro
ventana.eval('tk::PlaceWindow . center')  # Centrar la ventana en la pantalla

# Crear título de la aplicación
label_titulo = tk.Label(ventana, text="Inicio de Sesión", font=("Arial", 24, "bold"), bg="#2c3e50", fg="#ecf0f1")
label_titulo.pack(pady=30)

# Crear etiqueta y campo para el usuario
label_usuario = tk.Label(ventana, text="Usuario:", font=("Arial", 14), bg="#2c3e50", fg="#ecf0f1")
label_usuario.pack(pady=10)
entry_usuario = tk.Entry(ventana, font=("Arial", 14), bg="#ecf0f1", fg="#34495e", relief="flat", borderwidth=5)
entry_usuario.pack(pady=10, padx=20)

# Crear etiqueta y campo para la contraseña
label_contrasena = tk.Label(ventana, text="Contraseña:", font=("Arial", 14), bg="#2c3e50", fg="#ecf0f1")
label_contrasena.pack(pady=10)
entry_contrasena = tk.Entry(ventana, show="*", font=("Arial", 14), bg="#ecf0f1", fg="#34495e", relief="flat", borderwidth=5)
entry_contrasena.pack(pady=10, padx=20)

# Botón de inicio de sesión
boton_login = tk.Button(
    ventana, 
    text="Iniciar sesión", 
    font=("Arial", 14, "bold"), 
    bg="#3498db", 
    fg="white", 
    activebackground="#2980b9", 
    activeforeground="white", 
    relief="flat", 
    borderwidth=5, 
    command=verificar_credenciales
)
boton_login.pack(pady=10)

# Botón de registro
boton_registro = tk.Button(
    ventana, 
    text="Registrarse", 
    font=("Arial", 14, "bold"), 
    bg="#2ecc71",  # Verde para el botón de registro
    fg="white", 
    activebackground="#27ae60", 
    activeforeground="white", 
    relief="flat", 
    borderwidth=5, 
    command=registrar_usuario
)
boton_registro.pack(pady=10)

# Crear una etiqueta de pie de página
label_footer = tk.Label(ventana, text="© 2024 TuAplicación", font=("Arial", 10), bg="#2c3e50", fg="#7f8c8d")
label_footer.pack(side="bottom", pady=10)

# Ejecutar ventana
ventana.mainloop()
