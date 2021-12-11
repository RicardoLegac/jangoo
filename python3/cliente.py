class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'nombre {self.nombre} edad: {self.edad}')
    def __str__(self):
        return f'nombre{self.nombre} edad: {self.edad}'
    
class Cliente (Persona):
    pass

def main():
    cliente1 = Cliente('ricardo',254)
    print(cliente1)
    