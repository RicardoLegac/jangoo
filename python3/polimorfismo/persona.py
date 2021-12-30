class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre
    def moverse(self):
        print('ando caminando')
    
class Atleta(Persona):
    def moverse(self):
        print('ando corriendo')
    
class Ciclista(Persona):
    def moverse(self):
        print('ando pedaleando')
        