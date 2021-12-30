from io import open 
def escribir_archivo():
    archivo = open('text.txt','w+')
    archivo.write('hola')
    archivo.close()

def main():
    escribir_archivo()

if __name__ == '__main__':
    main()