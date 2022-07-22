from io import SEEK_CUR, SEEK_SET
import pickle 
class Persona:
    def __init__(self,nombre,edad,genero):
        self.nombre =nombre
        self.edad = edad
        self.genero = genero
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.edad, self.genero)

class AgregarPersona:
    personas =[]
    def __init__(self):
        listapersona = open("listapersona", "ab+")
        listapersona.seek(SEEK_SET)
        try: 
            self.personas = pickle.load(listapersona)
            print(" se cargaron {} objetos ".format(len(self.personas)))
        except: 
            print("el fichero esta vacio")
        finally:
            listapersona.close()
            del listapersona
    def agregarPersonas(self,persona):
        self.personas.append(persona)
    
    def mostrarPersona(self):
        for c in self.personas:
            print(c)

    def guardarPersonas(self):
        listapersonas = open("listapersona","wb")
        pickle.dumb(self.personas,listapersonas)
        listapersonas.close()
        del listapersonas

    def mostrarDatos(self):
        print("\nse cargaron: ")
        for p in self.personas:
            print (p)

p1 = Persona("Ricardo",24,"M")
p2 = Persona("Marlyn",24,"F")
lista = AgregarPersona()
lista.agregarPersonas(p1)
lista.agregarPersonas(p2)
lista.mostrarPersona()
lista.mostrarDatos()
#print(p1.__str__())