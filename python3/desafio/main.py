from figuras import *

def main():
    while True:
        menu = """
            1. Rectangulo
            2. Circulo
            3. Salir 
            Ingrese la opcion 
        """        
        opcion = int(input (menu))
        if opcion == 1:
            base = float(input('Ingrese la base del rectangulo: '))
            altura = float(input('Ingrese la altura del rectangulo: '))
            rectangulo = Rectangulo(base, altura)
            probar_figura(rectangulo)
        if opcion == 2:
            radio = float(input('ingrese el radio de la circunferencia: '))
            circulo = Circulo(radio)
            probar_figura(circulo)
        if opcion == 3:
            break
        
if __name__ == '__main__':
    main()