class Persona_DAO:
    """
        DAO significa: Data Access Object
        CRUD significa: Create Read Update Delete
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHER id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
