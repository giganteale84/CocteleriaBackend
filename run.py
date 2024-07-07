from flask import Flask, request
from app.database import init_app
from app.views import *
from app.models import Registro
from flask_cors import CORS


app = Flask(__name__)

init_app(app) #le pasamos la app a "init app"
#permitir solicitudes desde cualquier origen
CORS(app)
app.route("/apis/favoritos", methods = ["POST"])(GetFavoritos) 

app.route("/apis/favoritos/add", methods = ["POST"])(AddFavorito)

app.route("/apis/Usuario/upd", methods = ["POST"])(UpdateCorreo)

app.route("/apis/favoritos", methods = ["DELETE"])(DelFavorito)

app.route("/apis/cocteles", methods = ["GET"])(GetCocteles)
 
app.route("/apis/sesion", methods = ["POST"])(iniciarSesion)

@app.route("/apis/registro", methods = ["POST"])
def Registrar():
    data = request.json
    return Registrarse(data)
    
if __name__ == "__main__":
    app.run(debug = True)
    