from .conexion_db import Conexion
from tkinter import messagebox
def crear_tabla():
    conexion = Conexion()
    sql='''
    CREATE TABLE pelicula(
        id_pelicula INTEGER, 
        nombre VARCHAR(100),
        duracion VARCHAR(30),
        genero VARCHAR(30),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:

        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'se creo la tabla en la base de datos'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'la tabla ya esta creada'
        messagebox.showerror(titulo,mensaje)
        

def borrar_tabla():
    conexion = Conexion()
    sql = 'DROP TABLE pelicula'
    try:

        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Eliminar Registro'
        mensaje = 'se elimino la tabla en la base de datos'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = 'Eliminar Registro'
        mensaje = 'la tabla ya esta eliminada'
        messagebox.showerror(titulo,mensaje)
class Pelicula:
    def __init__(self, nombre,duracion,genero):
        self.id_pelicula= None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula: {self.nombre}, Duracion: {self.duracion}, Genero: {self.genero}'

def guardar(pelicula):
    conexion = Conexion()
    sql = f"""
    INSERT INTO pelicula(nombre, duracion, genero) 
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror('Conexion al registro', 'La tabla peliculas no esta creada')

