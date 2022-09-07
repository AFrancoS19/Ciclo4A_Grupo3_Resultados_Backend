from Modelos.Partido import Partidos, PartidoSchema

class clasePartidoController():
    def __init__(self):
        self.partido_schema = PartidoSchema()
        self.partidos_schema = PartidoSchema(many=True)
    
    def list(self):
        all_partidos = Partidos.query.all()
        result = self.partidos_schema.dump(all_partidos)
        return result

    def create(self, request):
        nombre = request.json['nombre']
        lema = request.json['lema']

        new_Partido = Partidos(nombre, lema)
        Partidos.db.session.add(new_Partido)
        Partidos.db.session.commit()
        return self.partido_schema.jsonify(new_Partido)

    def update(self, request, id):
        partido = Partidos.query.get(id)

        nombre = request.json['nombre']
        lema = request.json['lema']
        partido.nombre = nombre
        partido.lema = lema
        Partidos.db.session.commit()
        return self.partido_schema.jsonify(partido)

    def search(self, id):
        partido = Partidos.query.get(id)
        return self.partido_schema.jsonify(partido)
    
    def delete(self, id):
        partido = Partidos.query.get(id)
        Partidos.db.session.delete(partido)
        Partidos.db.session.commit()
        return self.partido_schema.jsonify(partido)