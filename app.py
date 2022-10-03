from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from db import db
from Routes.Candidato import candidato
from Routes.Partido import partido
from Routes.Mesa import mesa
from Routes.ResultadoCandidato import resultadocandidato
from Routes.Reportes import reportes
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)

cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ["DB"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

app.register_blueprint(candidato)
app.register_blueprint(partido)
app.register_blueprint(mesa)
app.register_blueprint(resultadocandidato)
app.register_blueprint(reportes)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
