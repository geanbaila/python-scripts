# from modulo_source import sumar
# from modulo_source import sumar as miclasesuma
# from modulo_source import sumar, restar
from modulo_source import *

print('__name__ ::', __name__)
if __name__ == '__main__':
    resultado = sumar(5, 5)
    print(resultado)

    resultado = restar(5, 5)
    print(resultado)