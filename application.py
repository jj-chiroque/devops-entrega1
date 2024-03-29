import os
from flask import Flask
from model.init import instantiate_db
from flask_injector import FlaskInjector
from model.model import Base

# Instancia de la aplicación en Flask
application = Flask(__name__)

application.config.from_object('config.default.Config')

with application.app_context():
    from database.db_connection import db
    db.Model = Base

from dependencies import configure

from api.default import default_api
application.register_blueprint(default_api, url_prefix='/')

from api.blacklists import blacklists_api
application.register_blueprint(blacklists_api, url_prefix='/blacklists')

# Agregamos el inyector de dependencias 
FlaskInjector(app=application, modules=[configure])

with application.app_context():
    db.create_all()

# Punto de arranque: servidor de desarrollo
if __name__ == "__main__":
    application.run(host = "0.0.0.0", port = 5000, debug = True)
