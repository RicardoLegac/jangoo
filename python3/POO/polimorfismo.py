class Coche():
    def desplazamiento(self):
        print("4 ruedas")

class Moto():
    def desplazamiento(self):
        print("2 ruedas")

class Camion():
    def desplazamiento(self):
        print("6 ruedas")

unamoto= Moto()
unamoto.desplazamiento()

uncoche = Coche()
uncoche.desplazamiento()

uncamion = Camion()
uncamion.desplazamiento() 

def DesplazamientoVehiculo(vehiculo):
    print("\npolimorfismo ..")
    vehiculo.desplazamiento()

unvehiculo = Camion()
DesplazamientoVehiculo(unvehiculo)