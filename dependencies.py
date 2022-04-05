from injector import singleton
from database.db_connection import DBConnection

# Vinculación de las dependencias inyectables
def configure(binder):
    binder.bind(DBConnection, to=DBConnection, scope=singleton)