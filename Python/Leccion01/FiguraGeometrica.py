class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
         self.ancho = ancho
        else:
         self._ancho = 0 
         print(f'valor erroneo para el ancho: {ancho}')       
        if self._Validar_Valores(alto):
         self._alto = alto
        else:
         self._alto = 0
         print(f'Valor erroeno para el alto: {alto}')
        
@property
def ancho(self):
    return self._ancho  

@ancho.setter
def ancho(self, ancho):
    if self._validar_valores(ancho):
        self._ancho = ancho
    else:
        print(f'valor erroneo ancho: {ancho}')
        
@property
def alto(self):
    return self._alto

@alto.setterdef 
def alto(self, alto):
    if self._validar_valores(alto):
        self._alto = alto
    else:
        print(f'valor erroneo alto: {alto}')
    
def __str__(self):
    return f'FiguraGeometrica [Ancho: {self.ancho}, Alto: {self._alto}]'

def _validar_valores(self, valor):
    return True if 0 < 10 else False # Metodo encapsulado
    