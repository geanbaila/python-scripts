valor = True
# python2 and python3
result = 'result from if sentence' if valor else 'result from else sentence'
print(result)

# python3
print('result from if sentence') if valor else print('result from else sentence')

result = None
if not valor:
    result = 'it is my result'

print('result:', result)