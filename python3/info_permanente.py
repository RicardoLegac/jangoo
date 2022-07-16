import pickle 
class Persona:
    def __init__(self,nombre,edad,genero):
        self.nombre =nombre
        self.edad = edad
        self.genero = genero
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.edad, self.genero)

class ListarPersonas:
    personas = []
    def agregarPersonas(self,persona):
        self.personas.append(persona)
    
    def mostrarPersonas(self):
        for c in self.personas:
            print(c)

p1 = Persona("Ricardo",24,"M")
p2 = Persona("Marlyn",24,"F")
lista = ListarPersonas()
lista.agregarPersonas(p1)
lista.agregarPersonas(p2)
print(p1.__str__())