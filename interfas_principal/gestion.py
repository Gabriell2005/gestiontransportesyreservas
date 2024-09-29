import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
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

def cargar_interfaz():
    
    ventana = tk.Toplevel()  # Crear una nueva ventana para la interfaz de gestión
    ventana.title("ARROWCOMPANY")
    ventana.geometry("10000x900")  # Tamaño de la ventana de gestión
    ventana.configure(bg=COLOR_FONDO)

    
# Función para eliminar cliente
def eliminar_cliente():
    id_cliente = entrada_id_cliente_eliminar.get()
    if not id_cliente:
        messagebox.showwarning("Advertencia", "Ingrese el ID del cliente a eliminar")
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cliente WHERE idCliente = %s", (id_cliente,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
            cargar_clientes()  # Recargar datos
        else:
            messagebox.showwarning("Advertencia", "Cliente no encontrado")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo eliminar el cliente: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()



def insertar_cliente():
    nombre = entrada_nombre_cliente.get()
    contacto = entrada_contacto_cliente.get()
    direccion = entrada_direccion_cliente.get()
    contraseña = entrada_contraseña_cliente.get()
    
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO cliente (nombre, contacto, direccion, contraseña) VALUES (%s, %s, %s, AES_ENCRYPT(%s, 'clave_secreta'))"
        valores = (nombre, contacto, direccion, contraseña)
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Cliente insertado correctamente")
        limpiar_campos_cliente()
        cargar_clientes()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo insertar el cliente: {error}")
        # Imprimir información adicional para depuración
        print(f"Error completo: {error}")
        print(f"SQL ejecutado: {cursor._last_executed}")
    finally:
        if conexion.is_connected():
            cursor.close()


# Función para cargar clientes
def cargar_clientes():
    for row in treeview_clientes.get_children():
        treeview_clientes.delete(row)  # Limpiar el Treeview de clientes

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT idCliente, nombre, contacto, direccion FROM cliente")
        clientes = cursor.fetchall()
        
        for cliente in clientes:
            treeview_clientes.insert("", tk.END, values=cliente)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo cargar los clientes: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()
            # Función para eliminar conductor
def eliminar_conductor():
    id_conductor = entrada_id_conductor_eliminar.get()
    if not id_conductor:
        messagebox.showwarning("Advertencia", "Ingrese el ID del conductor a eliminar")
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM conductor WHERE idConductor = %s", (id_conductor,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Conductor eliminado correctamente")
            cargar_conductores()  # Recargar datos
        else:
            messagebox.showwarning("Advertencia", "Conductor no encontrado")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo eliminar el conductor: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()



    

# Función para insertar conductores
def insertar_conductor():
    nombre = entrada_nombre_conductor.get()
    licencia = entrada_licencia_conductor.get()
    contacto = entrada_contacto_conductor.get()
    
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO conductor (nombre, licencia, contacto) VALUES (%s, %s, %s)"
        valores = (nombre, licencia, contacto)
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Conductor insertado correctamente")
        limpiar_campos_conductor()
        cargar_conductores()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo insertar el conductor: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()
# Función para eliminar ruta
def eliminar_ruta():
    id_ruta = entrada_id_ruta_eliminar.get()
    if not id_ruta:
        messagebox.showwarning("Advertencia", "Ingrese el ID de la ruta a eliminar")
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM ruta WHERE idRuta = %s", (id_ruta,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Ruta eliminada correctamente")
            cargar_rutas()  # Recargar datos
        else:
            messagebox.showwarning("Advertencia", "Ruta no encontrada")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo eliminar la ruta: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()



# Función para insertar rutas
def insertar_ruta():
    origen = entrada_origen.get()
    destino = entrada_destino.get()
    distancia = entrada_distancia.get()
    duracion_estimada = entrada_duracion.get()
    
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO ruta (origen, destino, distancia, duracionEstimada) VALUES (%s, %s, %s, %s)"
        valores = (origen, destino, distancia, duracion_estimada)
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Ruta insertada correctamente")
        limpiar_campos_ruta()
        cargar_rutas()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo insertar la ruta: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()

# Función para cargar rutas
def cargar_rutas():
    for row in treeview_rutas.get_children():
        treeview_rutas.delete(row)  # Limpiar el Treeview

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT idRuta, origen, destino, distancia, duracionEstimada FROM ruta")
        rutas = cursor.fetchall()
        
        for ruta in rutas:
            treeview_rutas.insert("", tk.END, values=ruta)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo cargar las rutas: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()
# Función para eliminar reserva
def eliminar_reserva():
    id_reserva = entrada_id_reserva_eliminar.get()
    if not id_reserva:
        messagebox.showwarning("Advertencia", "Ingrese el ID de la reserva a eliminar")
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM reservapasaje WHERE idReserva = %s", (id_reserva,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Reserva eliminada correctamente")
            cargar_reservas()  # Recargar datos
        else:
            messagebox.showwarning("Advertencia", "Reserva no encontrada")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo eliminar la reserva: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()


def insertar_reserva():
    id_cliente = entrada_id_cliente.get()
    id_ruta = entrada_id_ruta.get()
    fecha_viaje = f"{año.get()}-{mes.get():02d}-{dia.get():02d}"  # Formato YYYY-MM-DD
    numero_asiento = entrada_numero_asiento.get()
    estado = entrada_estado.get()
    
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO reservapasaje (idCliente, idRuta, fechaViaje, numeroAsiento, estado) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_cliente, id_ruta, fecha_viaje, numero_asiento, estado)
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Reserva insertada correctamente")
        limpiar_campos_reserva()
        cargar_reservas()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo insertar la reserva: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()

# Función para cargar reservas
def cargar_reservas():
    for row in treeview_reservas.get_children():
        treeview_reservas.delete(row)  # Limpiar el Treeview

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT reservapasaje.idReserva, cliente.nombre, ruta.origen, ruta.destino, reservapasaje.fechaViaje, reservapasaje.numeroAsiento, reservapasaje.estado 
            FROM reservapasaje
            JOIN cliente ON reservapasaje.idCliente = cliente.idCliente
            JOIN ruta ON reservapasaje.idRuta = ruta.idRuta
        """)
        reservas = cursor.fetchall()

        for reserva in reservas:
            treeview_reservas.insert("", tk.END, values=reserva)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo cargar las reservas: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()

# Funciones para limpiar campos
def limpiar_campos_cliente():
    entrada_nombre_cliente.delete(0, tk.END)
    entrada_contacto_cliente.delete(0, tk.END)
    entrada_direccion_cliente.delete(0, tk.END)
    entrada_contraseña_cliente.delete(0, tk.END)

def limpiar_campos_conductor():
    entrada_nombre_conductor.delete(0, tk.END)
    entrada_licencia_conductor.delete(0, tk.END)
    entrada_contacto_conductor.delete(0, tk.END)

def limpiar_campos_ruta():
    entrada_origen.delete(0, tk.END)
    entrada_destino.delete(0, tk.END)
    entrada_distancia.delete(0, tk.END)
    entrada_duracion.delete(0, tk.END)

def limpiar_campos_reserva():
    entrada_id_cliente.delete(0, tk.END)
    entrada_id_ruta.delete(0, tk.END)
    año.set(date.today().year)
    mes.set(date.today().month)
    dia.set(date.today().day)
    entrada_numero_asiento.delete(0, tk.END)
    entrada_estado.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Transporte y Reservas")

# Importar el módulo de estilos
from tkinter import ttk

# Aplicar estilos
style = ttk.Style()
style.theme_use('default')

# Configurar notebook
style.configure("TNotebook", background=COLOR_FONDO)
style.configure("TNotebook.Tab", background=COLOR_WIDGET, foreground=COLOR_TEXTO, padding=[10, 5])
style.map("TNotebook.Tab", background=[("selected", COLOR_BOTON)], foreground=[("selected", COLOR_TEXTO)])

# Configurar frames
style.configure("TFrame", background=COLOR_FONDO)

# Configurar etiquetas
style.configure("TLabel", background=COLOR_FONDO, foreground=COLOR_TEXTO)

# Configurar entradas
style.configure("TEntry", fieldbackground=COLOR_WIDGET, foreground=COLOR_TEXTO)

# Configurar botones
style.configure("TButton", background=COLOR_BOTON, foreground=COLOR_TEXTO)
style.map("TButton", background=[("active", COLOR_BOTON_ACTIVO)])

# Configurar Treeview
style.configure("Treeview", background=COLOR_WIDGET, foreground=COLOR_TEXTO, fieldbackground=COLOR_WIDGET)
style.configure("Treeview.Heading", background=COLOR_BOTON, foreground=COLOR_TEXTO)

# Aplicar configuración a la ventana principal
ventana.configure(bg=COLOR_FONDO)

# Crear un notebook (pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand=True)

# Pestaña para Clientes
tab_cliente = ttk.Frame(notebook)
notebook.add(tab_cliente, text='Clientes')
# Crear entrada y botón en la pestaña de Clientes
tk.Label(tab_cliente, text="ID Cliente a eliminar:").grid(row=6, column=0, padx=5, pady=5)
entrada_id_cliente_eliminar = tk.Entry(tab_cliente)
entrada_id_cliente_eliminar.grid(row=6, column=1, padx=5, pady=5)
boton_eliminar_cliente = tk.Button(tab_cliente, text="Eliminar Cliente", command=eliminar_cliente)
boton_eliminar_cliente.grid(row=7, column=0, columnspan=2, pady=10)
tk.Label(tab_cliente, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entrada_nombre_cliente = tk.Entry(tab_cliente)
entrada_nombre_cliente.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab_cliente, text="Contacto:").grid(row=1, column=0, padx=5, pady=5)
entrada_contacto_cliente = tk.Entry(tab_cliente)
entrada_contacto_cliente.grid(row=1, column=1, padx=5, pady=5)

tk.Label(tab_cliente, text="Dirección:").grid(row=2, column=0, padx=5, pady=5)
entrada_direccion_cliente = tk.Entry(tab_cliente)
entrada_direccion_cliente.grid(row=2, column=1, padx=5, pady=5)

tk.Label(tab_cliente, text="Contraseña:").grid(row=3, column=0, padx=5, pady=5)
entrada_contraseña_cliente = tk.Entry(tab_cliente, show="*")
entrada_contraseña_cliente.grid(row=3, column=1, padx=5, pady=5)

boton_insertar_cliente = tk.Button(tab_cliente, text="Insertar Cliente", command=insertar_cliente)
boton_insertar_cliente.grid(row=4, column=0, columnspan=2, pady=10)

# Treeview para mostrar clientes
treeview_clientes = ttk.Treeview(tab_cliente, columns=("idCliente", "nombre", "contacto", "direccion"), show="headings")
treeview_clientes.heading("idCliente", text="ID Cliente")
treeview_clientes.heading("nombre", text="Nombre")
treeview_clientes.heading("contacto", text="Contacto")
treeview_clientes.heading("direccion", text="Dirección")
treeview_clientes.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Cargar clientes al iniciar la aplicación
cargar_clientes()

# Pestaña para Conductores
tab_conductor = ttk.Frame(notebook)
notebook.add(tab_conductor, text='Conductores')
# Crear entrada y botón en la pestaña de Conductores
tk.Label(tab_conductor, text="ID Conductor a eliminar:").grid(row=4, column=0, padx=5, pady=5)
entrada_id_conductor_eliminar = tk.Entry(tab_conductor)
entrada_id_conductor_eliminar.grid(row=4, column=1, padx=5, pady=5)
boton_eliminar_conductor = tk.Button(tab_conductor, text="Eliminar Conductor", command=eliminar_conductor)
boton_eliminar_conductor.grid(row=5, column=0, columnspan=2, pady=10)
tk.Label(tab_conductor, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entrada_nombre_conductor = tk.Entry(tab_conductor)
entrada_nombre_conductor.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab_conductor, text="Licencia:").grid(row=1, column=0, padx=5, pady=5)
entrada_licencia_conductor = tk.Entry(tab_conductor)
entrada_licencia_conductor.grid(row=1, column=1, padx=5, pady=5)

tk.Label(tab_conductor, text="Contacto:").grid(row=2, column=0, padx=5, pady=5)
entrada_contacto_conductor = tk.Entry(tab_conductor)
entrada_contacto_conductor.grid(row=2, column=1, padx=5, pady=5)

boton_insertar_conductor = tk.Button(tab_conductor, text="Insertar Conductor", command=insertar_conductor)
boton_insertar_conductor.grid(row=3, column=0, columnspan=2, pady=10)

# Treeview para mostrar conductores
treeview_conductores = ttk.Treeview(tab_conductor, columns=("idConductor", "nombre", "licencia", "contacto"), show="headings")
treeview_conductores.heading("idConductor", text="ID Conductor")
treeview_conductores.heading("nombre", text="Nombre")
treeview_conductores.heading("licencia", text="Licencia")
treeview_conductores.heading("contacto", text="Contacto")
treeview_conductores.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Función para cargar conductores
def cargar_conductores():
    for row in treeview_conductores.get_children():
        treeview_conductores.delete(row)  # Limpiar el Treeview de conductores

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT idConductor, nombre, licencia, contacto FROM conductor")
        conductores = cursor.fetchall()
        
        for conductor in conductores:
            treeview_conductores.insert("", tk.END, values=conductor)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo cargar los conductores: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()

# Cargar conductores al iniciar la aplicación
cargar_conductores()
# Pestaña para Rutas
tab_ruta = ttk.Frame(notebook)
notebook.add(tab_ruta, text='Rutas')
# Crear entrada y botón en la pestaña de Rutas
tk.Label(tab_ruta, text="ID Ruta a eliminar:").grid(row=6, column=0, padx=5, pady=5)
entrada_id_ruta_eliminar = tk.Entry(tab_ruta)
entrada_id_ruta_eliminar.grid(row=6, column=1, padx=5, pady=5)
boton_eliminar_ruta = tk.Button(tab_ruta, text="Eliminar Ruta", command=eliminar_ruta)
boton_eliminar_ruta.grid(row=7, column=0, columnspan=2, pady=10)
tk.Label(tab_ruta, text="Origen:").grid(row=0, column=0, padx=5, pady=5)
entrada_origen = tk.Entry(tab_ruta)
entrada_origen.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab_ruta, text="Destino:").grid(row=1, column=0, padx=5, pady=5)
entrada_destino = tk.Entry(tab_ruta)
entrada_destino.grid(row=1, column=1, padx=5, pady=5)

tk.Label(tab_ruta, text="Distancia:").grid(row=2, column=0, padx=5, pady=5)
entrada_distancia = tk.Entry(tab_ruta)
entrada_distancia.grid(row=2, column=1, padx=5, pady=5)

tk.Label(tab_ruta, text="Duración Estimada:").grid(row=3, column=0, padx=5, pady=5)
entrada_duracion = tk.Entry(tab_ruta)
entrada_duracion.grid(row=3, column=1, padx=5, pady=5)

boton_insertar_ruta = tk.Button(tab_ruta, text="Insertar Ruta", command=insertar_ruta)
boton_insertar_ruta.grid(row=4, column=0, columnspan=2, pady=10)

# Treeview para mostrar rutas
treeview_rutas = ttk.Treeview(tab_ruta, columns=("idRuta", "origen", "destino", "distancia", "duracionEstimada"), show="headings")
treeview_rutas.heading("idRuta", text="ID Ruta")
treeview_rutas.heading("origen", text="Origen")
treeview_rutas.heading("destino", text="Destino")
treeview_rutas.heading("distancia", text="Distancia")
treeview_rutas.heading("duracionEstimada", text="Duración Estimada")
treeview_rutas.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Cargar rutas al iniciar la aplicación
cargar_rutas()

# Pestaña para Reservas
tab_reserva = ttk.Frame(notebook)
notebook.add(tab_reserva, text='Reservas')
# Crear entrada y botón en la pestaña de Reservas
tk.Label(tab_reserva, text="ID Reserva a eliminar:").grid(row=7, column=0, padx=5, pady=5)
entrada_id_reserva_eliminar = tk.Entry(tab_reserva)
entrada_id_reserva_eliminar.grid(row=7, column=1, padx=5, pady=5)
boton_eliminar_reserva = tk.Button(tab_reserva, text="Eliminar Reserva", command=eliminar_reserva)
boton_eliminar_reserva.grid(row=8, column=0, columnspan=2, pady=10)

tk.Label(tab_reserva, text="ID Cliente:").grid(row=0, column=0, padx=5, pady=5)
entrada_id_cliente = tk.Entry(tab_reserva)
entrada_id_cliente.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab_reserva, text="ID Ruta:").grid(row=1, column=0, padx=5, pady=5)
entrada_id_ruta = tk.Entry(tab_reserva)
entrada_id_ruta.grid(row=1, column=1, padx=5, pady=5)

# Selección de fecha de viaje
tk.Label(tab_reserva, text="Fecha de Viaje:").grid(row=2, column=0, padx=5, pady=5)
año = tk.IntVar(value=date.today().year)
mes = tk.IntVar(value=date.today().month)
dia = tk.IntVar(value=date.today().day)

entrada_año = tk.Spinbox(tab_reserva, from_=2020, to=2030, textvariable=año, width=5)
entrada_año.grid(row=2, column=1, padx=5, pady=5, sticky="w")

entrada_mes = tk.Spinbox(tab_reserva, from_=1, to=12, textvariable=mes, width=3)
entrada_mes.grid(row=2, column=1, padx=(60, 5), pady=5, sticky="w")

entrada_dia = tk.Spinbox(tab_reserva, from_=1, to=31, textvariable=dia, width=3)
entrada_dia.grid(row=2, column=1, padx=(100, 5), pady=5, sticky="w")

tk.Label(tab_reserva, text="Número de Asiento:").grid(row=3, column=0, padx=5, pady=5)
entrada_numero_asiento = tk.Entry(tab_reserva)
entrada_numero_asiento.grid(row=3, column=1, padx=5, pady=5)

tk.Label(tab_reserva, text="Estado:").grid(row=4, column=0, padx=5, pady=5)
entrada_estado = tk.Entry(tab_reserva)
entrada_estado.grid(row=4, column=1, padx=5, pady=5)

boton_insertar_reserva = tk.Button(tab_reserva, text="Insertar Reserva", command=insertar_reserva)
boton_insertar_reserva.grid(row=5, column=0, columnspan=2, pady=10)

# Treeview para mostrar reservas
treeview_reservas = ttk.Treeview(tab_reserva, columns=("idReserva", "nombreCliente", "origen", "destino", "fechaViaje", "numeroAsiento", "estado"), show="headings")
treeview_reservas.heading("idReserva", text="ID Reserva")
treeview_reservas.heading("nombreCliente", text="Cliente")
treeview_reservas.heading("origen", text="Origen")
treeview_reservas.heading("destino", text="Destino")
treeview_reservas.heading("fechaViaje", text="Fecha de Viaje")
treeview_reservas.heading("numeroAsiento", text="Asiento")
treeview_reservas.heading("estado", text="Estado")
treeview_reservas.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
# Botón para salir de la aplicación
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton_salir.pack(pady=10)
# Cargar reservas al iniciar la aplicación
cargar_reservas()
ventana.mainloop()