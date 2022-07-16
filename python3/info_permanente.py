import pickle 
class Persona:
    def __init__(self,nombre,edad,genero):
        self.nombre =nombre
        self.edad = edad
        self.genero = genero
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.edad, self.genero)

p1 = Persona("Ricardo",24,"M")
print(p1.__str__())