from flask import Flask , render_template , request
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_restful import Api
from models.perro import Perro
from models.boa_constrictor import Boa_Constrictor
from models.gato import Gato
from models.huron import Huron
import os

load_dotenv()

secret_key = os.urandom(24)
print(secret_key.hex())

app= Flask(__name__)

app.config["SECRET_KEY"] = secret_key
#db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)


@login_manager.user_loader

@app.route("/")
def home(): 
    ms = "BIENVENIDOS - SONIDOS DE ANIMALES"
    return render_template("index.html" , ms=ms)

@app.route("/sonido_perro")
def sonido_perro():
     return 'El Perro hace' + '  ' +  Perro.hacer_sonido()


@app.route("/sonido_huron")
def sonido_huron():
     return 'El Huron hace' + '  ' +  Huron.hacer_sonido()
 

@app.route("/sonido_gato")
def sonido_gato():
     return  'El Gato hace' + '  ' + Gato.hacer_sonido()



@app.route("/sonido_boa")
def sonido_boa():
     return 'La Boa hace' + '  '  + Boa_Constrictor.hacer_sonido()


