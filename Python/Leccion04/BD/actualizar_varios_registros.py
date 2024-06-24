import psycopg2 #Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)
try:
    with conexion:
       with conexion.cursor() as cursor:
         sentencia = 'UPDATEA persona SET nombre=%s, apellido=$s,email=%s WHERE id_persona=%s' # Placeholder
         valores = (('Romina', 'Ayala','ayalar@mail.com',5),
         ('Juan','Perez','jperez@mail.com',4)) #Es una tupla 
         cursor.executemany(sentencia,valores) #De esta manera ejecutamos la sentencia
         registros_actualizados = cursor.rowcount  #Recuperamos todos los registros que serán una lista
         print(f'Los registros actualizados son: {registros_actualizados}')   
        
except Exception as e:
        print(f'Ocurrio un error: {e}')
finally:
  conexion.close()