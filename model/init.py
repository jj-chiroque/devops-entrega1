from sqlalchemy.exc import IntegrityError
import os

def instantiate_db(db) -> None:
    """
    Permite instanciar la base de datos
    Dado a que con gunicorn instanciamos varios workers,
    estos al iniciar intentaran volver a crear la base de datos.
    Lo anterior causara un error que vamos a suprimir
    :param db: Conexion a la base de datos
    """
    try:
        db.create_all()
    except IntegrityError:
        pass
    