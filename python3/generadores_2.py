def devuelve_ciudades(*ciudades): #va a recibir un numero indeterminado de elementos en forma de tupla
    for elemento in ciudades:
        for subE in elemento: 
            yield subE
        # yield elemento 
        #yield from elemento =  otro for; for subElemento in elemento 

ciudades_devueltas = devuelve_ciudades("Madrid","Asuncion","Buenos Aires");
print(next(ciudades_devueltas));