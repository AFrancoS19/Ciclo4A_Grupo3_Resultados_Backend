from Modelos.Partido import Partido
from db import db
from Controladores.CustomExceptions import *

class clasePartidoController:
    def __init__(self):
        pass
    
    def list(self):
        resultado = Partido.query.all()

        lista = []
        for i in resultado:
            lista.append(i.dict_repr())
        return lista

    def create(self, data: dict):
        busqueda = Partido.query.filter_by(nombre=data["nombre"]).first()
        if busqueda is not None:
            raise ObjectAlreadyDefined("Ya existe un partido con el mismo nombre en base de datos")
        partido = Partido(data)
        db.session.add(partido)
        db.session.commit()

    def update(self, data):
        try:
            id = data.pop("id")
            resultado = Partido.query.get(id)
        except KeyError:
            raise AttributeError("No se ha suministrado el id para la modificacion")
        if resultado is None:
            raise ObjectNotFound("No existe un partido con el id suministrado")
        if "nombre" in data.keys():
            partidoConNombre = Partido.query.filter_by(nombre=data["nombre"]).first()
            if partidoConNombre is not None:
                raise DuplicateConstrainedValue(
                    "Ya existe un partido con ese nombre en la base de datos, no es posible realizar esta modificacion")
        resultado.modify(data)

    def search(self, id):
        resultado = Partido.query.get(id)
        if resultado is None:
            raise ObjectNotFound("No existe el partido con el id suministrado")
        return resultado.dict_repr()
    
    def delete(self, id):
        resultado = Partido.query.get(id)
        if resultado is None:
            raise ObjectNotFound("No existe un candidato con el id suministrado")
        db.session.delete(resultado)
        db.session.commit()