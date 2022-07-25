import sqlite3 

conexion = sqlite3.connect("bd") #crear-abrir conexion

cursor = conexion.cursor() #crear puntero
try:
    cursor.execute("CREATE TABLE Productos (Nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(30))")
except: 
    print("ya esta creada la tabla productos")

varios_productos=[
    ("Camiseta",10,"Deportes"),
    ("Remera",14,"Cualquiera")


]
cursor.execute("DELETE FROM Productos;") #elimina las filas de productos 
cursor.executemany("INSERT INTO Productos VALUES(?,?,?)",varios_productos)
cursor.execute("INSERT INTO Productos VALUES('Balon',15,'Deportes')")
cursor.execute("SELECT * FROM Productos ")
tabla = cursor.fetchall() #devuelve una lista 
print(tabla)
for producto in tabla:
    print (producto)
conexion.commit()
conexion.close()


#---------------------------------------------------

conexion2 = sqlite3.connect("db2")
cursor2 = conexion2.cursor()

try:
    cursor2.execute('''
        CREATE TABLE Produc (
            CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
            NOMBRE_ARTICULO VARCHAR(20),
            PRECIO INTEGER,
            SECCION VARCHAR(20)
        )

    ''')
except: 
    print("ya existe tabla productos")

cursor2.execute("DELETE FROM PRODUCTOS;")
cursor2.execute("DELETE FROM Produc;")

productos2 = [
    ("AA", "Pelota",25000,"Peloteria"),
    ("BB","Torta",26000,"Tortoleria")
]

cursor2.executemany("INSERT INTO Produc VALUES (?,?,?,?)",productos2)
tabla2 = cursor2.fetchall()
print(tabla2)
for p in tabla2:
    print(p)