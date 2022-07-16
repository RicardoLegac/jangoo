from io import SEEK_SET, open

archivo = open("texto.txt","w")
frase= "cualquiera\nxd"
archivo.write(frase)
archivo.close()
entrada = open("texto.txt","r")
texto = entrada.read()
entrada.seek(SEEK_SET) #el argumento recorre la cantidad de caracteres
texto_en_lista = entrada.readlines()
print("entrada en listas = ", texto_en_lista, "\n")
print(texto)
entrada.close()