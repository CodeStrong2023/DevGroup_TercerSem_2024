
resultado = None
a = '10'
b = 0
try:
    resultado = a/b #modificamos
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')

print(f'El resultado es: {resultado}')
print(f'seguimos....')