import sqlite3 

conexion = sqlite3.connect("bd") #crear-abrir conexion

cursor = conexion.cursor() #crear puntero

cursor.execute("CREATE TABLE Productos (Nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(30))")

conexion.close()