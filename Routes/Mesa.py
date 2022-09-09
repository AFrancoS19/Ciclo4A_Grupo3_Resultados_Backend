from flask import jsonify, Blueprint,request
from Controladores.ControladorAdmMesas import ControladorAdmMesas

cont = ControladorAdmMesas()

mesa = Blueprint('mesa', __name__)


@mesa.route("/",methods=['GET'])
def test():
    info = {}
    info["message"]="Server running ..."
    return jsonify(info)


@mesa.route("/mesas",methods=['GET'])
def getMesas():
    info = cont.index()
    return jsonify(info)


@mesa.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    info = cont.create(data)
    return jsonify(info)


@mesa.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    info = cont.show(id)
    return jsonify(info)


@mesa.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    info = cont.update(id,data)
    return jsonify(info)


@mesa.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    info = cont.delete(id)
    return jsonify(info)
