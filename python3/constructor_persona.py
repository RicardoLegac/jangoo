class Persona:
    def __init__(self,nombre,edad): 
        self.nombre = nombre 
        self.edad = edad

def main():
    persona1 = Persona('ricardo',24)
    print (persona1)
if __name__ == '__main__':
    main() 