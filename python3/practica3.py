#colecciones de datos
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