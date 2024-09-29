import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

import mysql.connector

conexion = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='gestion_de_transporte_y_reservas',
    port=3306  
)

print(conexion)
