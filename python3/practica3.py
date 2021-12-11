#colecciones de datos, diccionarios
numeros = {
    'uno': 1,
    'dos': 2
}
print(numeros.get('cuatro','no se encontro'))
print(numeros.keys())
print(numeros.values())
print(numeros.items())
for numero in numeros:
    print (numero)

for numero in numeros.values():
    print (numero)

#conjuntos no puede almacenar un valor que se repita

a = set()
a = {'a','b','c'}
print (a)
ingresado = input("ingrese su palabra: ")
ingresado = set(ingresado)
print (ingresado)
