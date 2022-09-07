from flask import jsonify
from flask import request
import json
from waitress import serve
#from Controladores import ControladorAdmMesas
import appconfig
from Controladores.partidoController import clasePartidoController

myPartidoController = clasePartidoController()

app = appconfig.appdatabase.app

# Parte de partidos

@app.route("/partidos", methods=['POST'])
def createPartidos():
    return myPartidoController.create(request)

@app.route("/partidos", methods=['GET'])
def getPartidos():
    return jsonify(myPartidoController.list())

@app.route("/partidos/<id>", methods=['GET'])
def getPartido(id):
    return myPartidoController.search(id)

@app.route("/partidos/<id>", methods=['PUT'])
def updatePartido(id):
    return myPartidoController.update(request, id)

@app.route("/partidos/<id>", methods=['DELETE'])
def deletePartido(id):
    return myPartidoController.delete(id)

# Parte de mesas

# @app.route("/",methods=['GET'])
# def test():
#  json = {}
#  json["message"]="Server running ..."
#  return jsonify(json)

# @app.route("/mesas",methods=['GET'])
# def getMesa():
#   json=ControladorAdmMesas.index()
#   return jsonify(json)

# @app.route("/mesas",methods=['POST'])
# def crearMesa():
#     data = request.get_json()
#     json = ControladorAdmMesas.create(data)
#     return jsonify(json)

# @app.route("/mesas/<string:id>",methods=['GET'])
# def getMesas(id):
#   json= ControladorAdmMesas.show(id)
#   return jsonify(json)

# @app.route("/mesas/<string:id>",methods=['PUT'])
# def modificarMesa(id):
#   data = request.get_json()
#   json= ControladorAdmMesas.update(id,data)
#   return jsonify(json)

# @app.route("/mesas/<string:id>",methods=['DELETE'])
# def eliminarMesa(id):
#   json= ControladorAdmMesas.delete(id)
#   return jsonify(json)


def loadFileConfig():
 with open('config.json') as f:
     data = json.load(f)
     return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])




