from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print("Creacion del objeto clase Cuadrado".center(50,"_"))
cuadrado1 = Cuadrado(5, "Azul")
cuadrado1.alto = -10
cuadrado1.ancho =23
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")

# Metodo MRO = Method Resolution Order
#print(Cuadrado.mro())

print(cuadrado1)
print("Creacion del objeto clase Rectangulo".center(50,"_"))
rectangulo1 = Rectangulo(5, 8, 'Verde')
rectangulo1.ancho = 15
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#figura1 = FiguraGeometrica() No se puede instanciar
print(Cuadrado.mro())