from db import db
import inspect
from Controladores.CustomExceptions import IncorrectAttribute

class Partido(db.Model):
    __tablename__ = "partidos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    lema = db.Column(db.String(255))

    def __init__(self, data, **kwargs):
        self.nombre = data["nombre"]
        self.lema = data["lema"]

    def dict_repr(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "lema": self.lema
        }

    def modify(self, data: dict):
        keys = data.keys()
        atributos = self.getAttributes()
        toDoModifications = []
        for key in keys:
            if key not in atributos:
                raise IncorrectAttribute(f"El atributo {key} no se encuentra definido para el partido")
            currentValue = getattr(self, key)
            newValue = data[key]
            if currentValue != newValue:
                toDoModifications.append((key, newValue))

        for modification in toDoModifications:
            setattr(self, modification[0], modification[1])
        db.session.commit()

    def getAttributes(self):
        resultado = []
        for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    resultado.append(i[0])
        return resultado

    def __repr__(self):
        return f"Partido: {self.id}, Nombre del partido: {self.nombre}, Lema del partido: {self.lema}"