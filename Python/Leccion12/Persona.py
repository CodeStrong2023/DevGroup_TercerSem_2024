class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other): # Other significa = otro
        return f'{self.nombre} + {other.nombre}'
    
    def __sub__(self, otro): # sub significa = substracción (resta)
        return self.edad - otro.edad
    
persona1 = Persona('Gabriel', 19)
persona2 = Persona('Gonzalez', 1)

# persona1.__add__(persona2) Sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)