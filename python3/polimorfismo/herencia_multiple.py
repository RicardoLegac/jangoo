class A:
    def __init__(self):
        print ('clase A')
    def a(self):
        print('soy un metodo de la clase A')

class B:
    def __init__(self):
        print ('clase B')
    def a(self):
        print('soy un metodo de la clase B')\

class C(A,B): #se le da mas importancia a la que esta mas a la izquierda
    def c(self):
        print('soy un metodo de C')
    

c1 = C() 