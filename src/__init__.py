from flask import Flask
from flask_cors import CORS

# Routes
from .routes import Users

app = Flask(__name__, instance_relative_config=True)

CORS(app,resources={"*":{"origins":"localhost:5000"}}) # Modificar el puerto a seleccion

# Blueprints
app.register_blueprint(Users.main, url_prefix='/api/v01/users')


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


# Manejo de errores
app.register_error_handler(404, page_not_found)
