from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self): 
        self.conexion =  None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with y __enter__') 
        self.conexion =  Conexion.obtenerConexion()
        self._cursor = self.conexion.cursor()
        return self._cursor
            
    def __exit__(self,tipo_exception, valor_exception, detalle_exception):
        log.debug('Se ejecuta el método exit')
        if valor_exception:
            self.conexion.rollback()
            log.debug(f'Ocurrió una exepción: '{valor_exception})
        else:
            self.conexion.commit()
            log.debug('Commit de la transacción')
        self.cursor.close()
        Conexion.liberarConexion(self._conexion)
        #