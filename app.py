from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from db import db
from Routes.Mesa import mesa
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/registraduria'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

migrate = Migrate(app,db)

app.register_blueprint(mesa)



def loadFileConfig():
    with open('../ProyRegistraduria/config.json') as f:
        data = json.load(f)
        return data


with app.app_context():
    db.create_all()

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])




