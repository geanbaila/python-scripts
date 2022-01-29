valor = 0
while valor <3:
    valor += 1
    print(valor)
else:
    print('Te aviso que ya terminó el while. valor =>'+str(valor))
print('\n')

# str() o un list() de char()
saludo = 'hola'
for word in saludo:
    print(word)
else:
    print('Te aviso que ya terminó el for. word =>'+word)
print('\n')

for word in saludo:
    if word=='o':
        break
else:
    print('Esta línea ya no se va ejecutar porque usaste un break')
print('\n')

# for permite iterar list()
saludo = ('hola', 'chau')
for word in saludo:
    print(word)
print('\n')

# for permite iterar tuple()
saludo = ['hola', 'chau']
for word in saludo:
    print(word)
print('\n')

contador = 0
for i in range(2,5):
    print(i)
    contador +=i
    continue
    break
else:
    print('Te aviso que ya terminó el for. contador =>'+str(contador))
print('\n')