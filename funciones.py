def sumar(a = 0, b = 0 ) -> int:
    return a + b

def restar(a:int = 0, b:int = 0 ) -> int:
    return a - b

# La convención es *args (arguments)
def imprimir_tupla(*tupla_nombre):
    for nombre in tupla_nombre:
        print('-', nombre)

# La convención es **kwargs (keyword arguments)
def imprimir_diccionario(**diccionario_nombre):
    for llave, valor in diccionario_nombre.items():
        print(llave, '-', valor)

    print('\n')
    for llave in diccionario_nombre.keys():
        print('-', llave)

    print('\n')
    for valor in diccionario_nombre.values():
        print('-', valor)
    

print(f'el resultado de sumar a+b es: {sumar(1, 1)}\n')
print(f'el resultado de restar a-b es: {restar(1, 1)}\n')
print('el resultado de imprimir nombres es:')
imprimir_tupla('gean', 'carlos')
print('\n')
imprimir_diccionario(primer='gean', segundo_nombre='carlos')
print('\n')