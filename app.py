from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores import ControladorAdmMesas
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app=Flask(__name__)

cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:delfin07@localhost:5432/registraduria'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db=SQLAlchemy(app)
ma = Marshmallow(app)

class Partidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    lema = db.Column(db.String(255))

    def __init__(self, nombre, lema):
        self.nombre = nombre
        self.lema = lema

db.create_all()

class PartidoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'lema')

partido_schema = PartidoSchema()
partidos_schema = PartidoSchema(many=True)

def loadFileConfig():
 with open('config.json') as f:
     data = json.load(f)
     return data


# Parte de partidos

@app.route("/partidos", methods=['POST'])
def createPartidos():
    nombre = request.json['nombre']
    lema = request.json['lema']

    new_Partido = Partidos(nombre, lema)
    db.session.add(new_Partido)
    db.session.commit()

    return partido_schema.jsonify(new_Partido)

@app.route("/partidos", methods=['GET'])
def getPartidos():
    all_Partidos = Partidos.query.all()
    result = partidos_schema.dump(all_Partidos)
    return jsonify(result)

@app.route("/partidos/<id>", methods=['GET'])
def getPartido(id):
    partido = Partidos.query.get(id)
    return partido_schema.jsonify(partido)

@app.route("/partidos/<id>", methods=['PUT'])
def updatePartido(id):
    partido = Partidos.query.get(id)

    nombre = request.json['nombre']
    lema = request.json['lema']
    partido.nombre = nombre
    partido.lema = lema

    db.session.commit()
    return partido_schema.jsonify(partido)

@app.route("/partidos/<id>", methods=['DELETE'])
def deletePartido(id):
    partido = Partidos.query.get(id)
    db.session.delete(partido)
    db.session.commit()

    return partido_schema.jsonify(partido)

# Parte de mesas

@app.route("/",methods=['GET'])
def test():
 json = {}
 json["message"]="Server running ..."
 return jsonify(json)

@app.route("/mesas",methods=['GET'])
def getMesa():
  json=ControladorAdmMesas.index()
  return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = ControladorAdmMesas.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['GET'])
def getMesas(id):
  json= ControladorAdmMesas.show(id)
  return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
  data = request.get_json()
  json= ControladorAdmMesas.update(id,data)
  return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
  json= ControladorAdmMesas.delete(id)
  return jsonify(json)


if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])




