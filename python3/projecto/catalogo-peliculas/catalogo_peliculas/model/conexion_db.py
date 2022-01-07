import sqlite3  

class Conexion():
    def __init__(self):
        self.base_datos = 'database/peliculas.db' #la ruta donde tenemos la base de datos 