def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra_invertida == palabra:
        return True
    else:
        return False
def main():
    palabra = input('ingrese una palabra: ')
    es_palindromo= palindromo(palabra)
    if es_palindromo:
        print('es palindromo')
    else:
        print('no es palindromo')

if __name__ == '__main__':
    main() 