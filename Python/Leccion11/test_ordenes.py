from Orden import Orden
from Producto import Producto

Producto1 = Producto('Camiseta', 100.00)
Producto2 = Producto('Pantalon', 150.00)
Producto3 = Producto('Camisa', 200.00)
Producto4 = Producto('Campera', 250.00)
Producto5 = Producto('Medias', 75.00)
Producto6 = Producto('Zapatillas', 300.00)


Productos1 = [Producto1, Producto2] # Lista de productos
orden1 = Orden(Productos1) # Primer objeto pasando la lista de productos
orden1.agregar__producto(Producto5)
orden1.agregar__producto(Producto3)
print(orden1)
print(f'Total de la orden 1: {orden1.calcular_total()}')

Productos2 = [Producto3, Producto4]
orden2 = Orden(Productos2)
orden2.agregar__producto(Producto6)
orden2.agregar__producto(Producto2)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')
