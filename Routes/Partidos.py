from flask import jsonify, Blueprint, request, make_response
from Controladores.partidoController import clasePartidoController
from Controladores.CustomExceptions import *

controlador = clasePartidoController()

partido = Blueprint('partido',__name__)

@partido.route('/partidos', methods=['POST'])
def createPartido():
    data = request.get_json()
    try:
        controlador.create(data)
        json = {}
        json["message"] = "El partido fue creado correctamente"
        return jsonify(json), 201
    except ObjectAlreadyDefined as ex:
        json = {}
        json["error"] = str(ex)
        return jsonify(json), 404


@partido.route('/partidos', methods=['GET'])
def listPartido():
    return jsonify(controlador.list())

@partido.route('/partidos/<id>', methods=['GET'])
def getPartido(id):
    try:
        partido = controlador.search(id)
        return jsonify(partido), 200
    except ObjectNotFound as ex:
        json = {}
        json["error"] = str(ex)
        return jsonify(json), 404

@partido.route('/partidos', methods=['PUT'])
def updatePartido():
    data = request.get_json()
    try:
        controlador.update(data)
        json = {}
        json["message"] = "Se ha modificado el partido correctamente"
        return jsonify(json), 200
    except ObjectNotFound as ex:
        json = {}
        json["error"] = str(ex)
        return jsonify(json), 404
    except DuplicateConstrainedValue as ex:
        json = {}
        json["error"] = str(ex)
        return jsonify(json), 400
    except AttributeError as ex:
        json = {}
        json["error"] = str(ex)
        return jsonify(json), 400

@partido.route('/partidos/<id>', methods=['DELETE'])
def deletePartido(id):
    try:
        controlador.delete(id)
        json = {}
        json["message"] = "Se ha eliminado el partido correctamente"
        return jsonify(json), 200
    except ObjectNotFound as ex:
        json = {}
        json["error"] = str(ex)
        return jsonify(json), 404