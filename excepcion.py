from excepcion_source import MiClaseExcepcion
from constante import DIVISOR_INVALIDO
# from constante import *


# divisor = DIVISOR_INVALIDO
divisor = 0
try:
    if divisor == DIVISOR_INVALIDO:
        raise Exception(f'No está permitido que el divisor sea {DIVISOR_INVALIDO}')
        # raise MiClaseExcepcion(f'MiClaseExcepcion:No está permitido que el divisor sea {DIVISOR_INVALIDO}')
    result = 100/divisor

# excepción de primer nivel
except ArithmeticError as e:
    print(f'ocurrio una excepción: {e} - {ValueError(e)}')

# excepción de segundo, etc nivel
except Exception as e:
    print(f'ocurrio una excepción: {e}')

# se ejecutará unicamente si no ocurrio alguna excepción
else:
    print('No ha ocurrido la excepción, siguiente sentencia..')

# se ejecutará siempre
finally:
    print('sentencia final')