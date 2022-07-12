class Persona():
    def __init__(self,nombre,edad,direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
    
    def descripcion(self):
        print("nombre: ",self.nombre,"\tedad: ",self.edad,"\tdireccion: ",self.direccion)

class Empleado(Persona):
    def __init__(self,salario, antiguedad):
        self.salario = salario
        self.antiguedad = antiguedad

persona = Persona("Antonio",15,"Paraguay")