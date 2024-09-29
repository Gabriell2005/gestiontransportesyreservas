import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import gestion

from datetime import date


# Definir colores
COLOR_FONDO = "#2C3E50"  # Azul oscuro
COLOR_WIDGET = "#34495E"  # Azul grisáceo
COLOR_TEXTO = "#ECF0F1"  # Blanco hueso
COLOR_BOTON = "#7F8C8D"  # Gris
COLOR_BOTON_ACTIVO = "#95A5A6"  # Gris claro

# Conexión a la base de datos           
conexion = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='gestion_de_transporte_y_reservas',
    port=3306
)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Transporte y Reservas")
ventana.geometry("400x300")  # Tamaño de la ventana

# Aplicar configuración a la ventana principal
ventana.configure(bg=COLOR_FONDO)

# Título grande
titulo = tk.Label(ventana, text="ArrowCompany", font=("Helvetica", 24), bg=COLOR_FONDO, fg=COLOR_TEXTO)
titulo.pack(pady=20)

# Función para mostrar la interfaz de gestión
import tkinter as tk
import gestion  # Importar el archivo de gestión que define la interfaz de gestión

import tkinter as tk
import gestion  # Importar el archivo de gestión

# Configuración de colores (puedes definir estos valores en tu código)
COLOR_FONDO = "#f0f0f0"
COLOR_TEXTO = "#000000"

def mostrar_interfaz():
    ventana_gestion = tk.Toplevel(ventana)
    ventana_gestion.title("Interfaz de Gestión")
    ventana_gestion.geometry("800x600")
    ventana_gestion.configure(bg=COLOR_FONDO)

    gestion.cargar_interfaz(ventana_gestion)

    mensaje_bienvenida = tk.Label(
        ventana_gestion,
        text="Bienvenido a la Gestión de Transporte y Reservas",
        font=("Helvetica", 16),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    mensaje_bienvenida.pack(pady=20)

# Ventana principal
ventana = tk.Tk()
ventana.title("Ventana Principal")
ventana.geometry("600x400")

# Botón para abrir la interfaz de gestión
btn_mostrar_interfaz = tk.Button(ventana, text="Abrir Interfaz de Gestión", command=mostrar_interfaz)
btn_mostrar_interfaz.pack(pady=20)
    # Puedes agregar más elementos a la ventana de gestión según sea necesario


# Botón para ingresar a la interfaz
boton_ingresar = tk.Button(ventana, text="Ingresar a la Interfaz", command=mostrar_interfaz, bg=COLOR_BOTON, fg=COLOR_TEXTO)
boton_ingresar.pack(pady=10)

# Botón para salir de la aplicación
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg=COLOR_BOTON, fg=COLOR_TEXTO)
boton_salir.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()