class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False 
         
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado (self):
        print("Marca", self.marca, "\nModelo", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)

class Moto(Vehiculos):
    def estado (self):
        print("Marca", self.marca, "\nModelo", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\nes moto")

un_vehiculo = Moto("Honda", "gt")
un_vehiculo.acelerar()
un_vehiculo.estado()