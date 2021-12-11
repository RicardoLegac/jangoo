class Persona:
    def __init__(self,nombre,edad): 
        self.nombre = nombre 
        self.edad = edad
    def mostrar_datos(self):
        print(f"nombre: {self.nombre} edad: {self.edad} ")

def main():
    persona1 = Persona('ricardo',24)
    persona1.mostrar_datos()
if __name__ == '__main__':
    main() 