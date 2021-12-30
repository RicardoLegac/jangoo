from io import open 
from os import path 
def escribir_archivo():
    archivo = open('text.txt','w+')
    archivo.write('hola')
    archivo.close()
def escribir_archivo():
    archivo = open('text.txt','r')
    if path.isfile('text.txt'):
        archivo = open('text.txt','r')
        textos =archivo.read()
        #archivo.readlines devuelve una lista por salto de linea 
        archivo.close()
        print(textos)
    else:
        print('no existe el archivo')
def main():
    escribir_archivo()

if __name__ == '__main__':
    main()