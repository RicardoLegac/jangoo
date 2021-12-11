def saludar(): 
    return 25, 'ricardo', 'leguizamon'
edad, nombre, apellido = saludar()
print (edad, nombre, apellido)

def saludo(nombre):
    return f'hola {nombre}'
nombre='ricardo'
print  (saludo (nombre))


def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma +=n
    return suma, kwargs

suma, valores = sumar(10,20, nombre='ricardo', edad= '24')
print (suma, valores)

borrar = '---------asas----------'
borrado=borrar.strip('-')
print (borrado)


