class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'nombre:  {self.nombre} edad: {self.edad}')
    def __str__(self):
        return f'nombre: {self.nombre} edad: {self.edad}'
    
class Cliente (Persona):
    pass

class Empleado(Persona):
    def __init__(self, nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    def detalle_empleado(self):
        super().mostrar_datos()
        print(f'sueldo: {self.sueldo}')
    
    def __str__ (self):
        super().__str__() + f'sueldo : {self.sueldo} '
def main():
    cliente1 = Cliente('ricardo',254)
    cliente1.mostrar_datos()

    empleado1 = Empleado('RODRIGO',25, 25000)
    empleado1.detalle_empleado()
    
if __name__ == '__main__':
    main()
