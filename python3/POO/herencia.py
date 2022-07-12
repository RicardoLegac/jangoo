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
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        
    def estado (self):
        print("Marca", self.marca, "\nModelo", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\nes moto")

class VElectrico():
    def __init__(self):
        self.carga = True

    def estado(self):
        print("es electrico", "\n cargada: " , self.carga)

class BiciE(VElectrico, Vehiculos): #se da mas importancia a la clase que esta mas a la izquierda
    
    def estado(self):
        print("bici electrica")

#bici = BiciE()
#bici.estado()


un_vehiculo = Moto("Honda", "gt")
un_vehiculo.acelerar()
un_vehiculo.estado()

