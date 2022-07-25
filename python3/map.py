class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $ ".format(self.nombre, self.cargo,self.salario)

listaempleados = [
    Empleado("ricardo","xdlol",54554),
    Empleado("marcelo","3xdlol",544)

]

def calculos_comision(empleado):
    empleado.salario = empleado.salario * 1.03
    return empleado

listasEmpleadoComision = map(calculos_comision, listaempleados )

for e in listasEmpleadoComision:
    print (e)