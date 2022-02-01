from manejo_archivos_source import MyContextManage


# caso 1
archivo = open('archivo.txt', 'w', encoding='utf8')
for i in range(5):
    archivo.write(f'{i}. crear archivo.txt si no existe. vuelca el contenido y escribe. \n')
archivo.close()

# caso 2
archivo = open('archivo.txt', '+a', encoding='utf8')
for i in range(5, 10):
    archivo.write(f'{i}. crear archivo.txt si no existe. escribe en la siguiente línea. \n')
archivo.close()

# caso 3
archivo = open('archivo.txt', 'r', encoding='utf8')
while linea := archivo.read():
    print(linea)
archivo.close()

# caso 4
archivo = open('archivo.txt', 'r', encoding='utf8')
prg_linea = archivo.readlines()
for linea in prg_linea:
    print(linea)
archivo.close()

# caso 5
archivo = open('archivo.txt', 'r', encoding='utf8')
while linea := archivo.readline():
    print(linea)
archivo.close()

# caso 6
archivo = open('archivo.txt', 'r', encoding='utf8')
linea_sin_espacio = [linea.rstrip() for linea in archivo]
print('......', linea_sin_espacio)
archivo.close()

# caso 7
with open('archivo.txt', 'r', encoding='utf8') as archivo:
    while linea := archivo.readline():
        print(linea)

# caso 8
with MyContextManage('archivo.txt') as archivo:
    while linea := archivo.read():
        print(linea)