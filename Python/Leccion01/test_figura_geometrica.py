from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion de objeto clase Cuadrado'.center(50, '_'))
Cuadrado1 = Cuadrado(8, "azul")
Cuadrado1.alto = 7
Cuadrado1.ancho = 7
# prinr(cuadrado1.ancho)
# prinr(cuadrado1.alto)
print(Cuadrado1.ancho)
print(Cuadrado1.alto)
print(f'calculo del area del cuadrado: {Cuadrado1.calcular_area()}')

#MRO = Method Resolution Orden
#print(Cuadrado.mro())

print(Cuadrado1)
print('Creacion de objeto clase Restagulo'.center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'verde')
rectangulo1.ancho = 8
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
