class Persona:
    nombre= None
    edad = None

    def mostar_datos(self): 
        print(self.nombre, self.edad)

persona1 = Persona()
persona1.nombre= 'ricardo'
persona1.edad = 25

persona1.mostar_datos()