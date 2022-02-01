valor = True
# python2 and python3
result = 'afirmativo' if valor else 'negativo'
print(result)

# python3
print('afirmativo') if valor else print('negativo')

result = ('negativo', 'afirmativo')[valor]
print(result)

# result = None
# if not valor:
#     result = 'it is my result'

# print('result:', result)