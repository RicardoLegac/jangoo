def excepciones():
    max = 10
    i=0
    for i in range(max):
        #print(i)
        try:
            n = int(input('ingrese un numero: '))
        except:
            print('ingrese solo numeros enteros: ')



def main():
    excepciones()

if __name__ == '__main__':
    main()