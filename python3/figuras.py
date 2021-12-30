class Figura():
    def __init__(self,nombre):
        self.nombre= nombre
    def area():
        pass
    def perimetro():
        pass

class Rectangulo(Figura):
    def __init__(self,base,altura):
        self.nombre= __class__.__name__ #obtener el nombre de la clase
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base * 2 + self.altura * 2
class Circulo(Figura):
    def __init__(self):
        print('circulo')

def probar_figura():
    pass