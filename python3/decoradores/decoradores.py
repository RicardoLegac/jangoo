def funcion_decoradora(funcion_recibida):
    def funcion_interior():
        print("vamos a realizar el siguiente calculo: ")
        funcion_recibida()
        print("terminamos el calculo")
    return funcion_interior()

@funcion_decoradora
def suma():
    print (20+25)

