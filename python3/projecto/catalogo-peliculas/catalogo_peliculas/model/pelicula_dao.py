from .conexion_db import Conexion
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