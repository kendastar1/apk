import tkinter as tk
from PIL import Image, ImageTk

def ver_detalles(nombre, precio):
    print(f"Detalles de {nombre}: {precio}")

def toggle_menu():
    global menu_visible
    if menu_visible:
        ocultar_menu()
    else:
        mostrar_menu()

def mostrar_menu():
    global menu_visible
    x = 400
    while x > 200:
        menu_frame.place(x=x, y=0)
        menu_frame.update()
        x -= 10
    menu_visible = True

def ocultar_menu():
    global menu_visible
    x = 200
    while x < 400:
        menu_frame.place(x=x, y=0)
        menu_frame.update()
        x += 10
    menu_visible = False

ventana = tk.Tk()
ventana.title("Tienda de Teléfonos")
ventana.geometry("400x700")
ventana.configure(bg="#f0f0f0")
ventana.eval('tk::PlaceWindow . center')

# Cargar imagen de fondo
try:
    fondo_imagen = Image.open("imagen/telefono1.jg")  # Asegúrate de tener esta imagen en el directorio
    fondo_imagen = fondo_imagen.resize((400, 700), Image.ANTIALIAS)
    fondo = ImageTk.PhotoImage(fondo_imagen)
except Exception as e:
    print(f"Error al cargar la imagen de fondo: {e}")
    fondo = None

# Crear un label para la imagen de fondo
if fondo:
    label_fondo = tk.Label(ventana, image=fondo)
    label_fondo.place(x=0, y=0)

titulo = tk.Label(ventana, text="Tienda de Teléfonos", font=("Arial", 24, "bold"), fg="#34495e", bg="#f0f0f0")
titulo.pack(pady=10)

boton_menu = tk.Button(ventana, text="☰", font=("Arial", 16, "bold"), bg="#3498db", fg="white", borderwidth=0, command=toggle_menu)
boton_menu.place(x=360, y=10)

productos = [
    {"nombre": "Teléfono A", "precio": "$499", "imagen": "telefono1.png"},
    {"nombre": "Teléfono B", "precio": "$599", "imagen": "telefono2.png"},
    {"nombre": "Teléfono C", "precio": "$699", "imagen": "telefono3.png"},
    {"nombre": "Teléfono D", "precio": "$799", "imagen": "telefono4.png"},
]

marco_principal = tk.Frame(ventana, bg="#f0f0f0")
marco_principal.pack(pady=10)

canvas = tk.Canvas(marco_principal, bg="#f0f0f0", width=400, height=400, highlightthickness=0)
canvas.pack(side=tk.TOP)

marco_productos = tk.Frame(canvas, bg="#f0f0f0")
canvas.create_window((0, 0), window=marco_productos, anchor="nw")

for producto in productos:
    marco_producto = tk.Frame(marco_productos, bg="white", bd=2, relief="groove")
    marco_producto.pack(side=tk.LEFT, padx=10, pady=10)

    try:
        imagen_original = Image.open(producto["imagen"])
        imagen_redimensionada = imagen_original.resize((100, 100), Image.ANTIALIAS)
        imagen_producto = ImageTk.PhotoImage(imagen_redimensionada)
        label_imagen = tk.Label(marco_producto, image=imagen_producto, bg="white")
        label_imagen.image = imagen_producto
        label_imagen.pack(pady=10)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

    label_nombre = tk.Label(marco_producto, text=producto["nombre"], font=("Arial", 14, "bold"), bg="white", fg="#34495e")
    label_nombre.pack(anchor="w", padx=10)
    
    label_precio = tk.Label(marco_producto, text=producto["precio"], font=("Arial", 12), bg="white", fg="#2ecc71")
    label_precio.pack(anchor="w", padx=10)

    boton_detalles = tk.Button(
        marco_producto,
        text="Ver detalles",
        font=("Arial", 10, "bold"),
        bg="#3498db",
        fg="white",
        borderwidth=0,
        padx=10,
        pady=5,
        command=lambda p=producto: ver_detalles(p["nombre"], p["precio"])
    )
    boton_detalles.pack(pady=5)

marco_productos.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

scrollbar_horizontal = tk.Scrollbar(marco_principal, orient="horizontal", command=canvas.xview, width=10)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill="x")

canvas.configure(xscrollcommand=scrollbar_horizontal.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

menu_visible = False
menu_frame = tk.Frame(ventana, width=200, height=700, bg="#2c3e50")
menu_frame.place(x=400, y=0)

boton_cerrar_menu = tk.Button(menu_frame, text="X", font=("Arial", 16), bg="#e74c3c", fg="white", borderwidth=0, command=ocultar_menu)
boton_cerrar_menu.place(x=160, y=10)

tk.Label(menu_frame, text="Menú de Navegación", font=("Arial", 14), bg="#2c3e50", fg="white").pack(pady=(50, 20))
tk.Button(menu_frame, text="Inicio", font=("Arial", 12), bg="#3498db", fg="white").pack(fill="x", pady=(5,), padx=(10,))
tk.Button(menu_frame, text="Productos", font=("Arial", 12), bg="#3498db", fg="white").pack(fill="x", pady=(5,), padx=(10,))
tk.Button(menu_frame, text="Ofertas", font=("Arial", 12), bg="#3498db", fg="white").pack(fill="x", pady=(5,), padx=(10,))
tk.Button(menu_frame, text="Contacto", font=("Arial", 12), bg="#3498db", fg="white").pack(fill="x", pady=(5,), padx=(10,))
tk.Button(menu_frame, text="Salir", font=("Arial", 12), bg="#e74c3c", fg="white").pack(fill="x", pady=(5,), padx=(10,), side=tk.BOTTOM)

ventana.mainloop()