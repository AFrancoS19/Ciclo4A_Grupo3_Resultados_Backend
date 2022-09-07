import appconfig

class Partidos(appconfig.appdatabase.db.Model):
    __tablename__ = "partidos"

    db = appconfig.appdatabase.db

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    lema = db.Column(db.String(255))

    def __init__(self, nombre, lema):
        self.nombre = nombre
        self.lema = lema

class PartidoSchema(appconfig.appdatabase.ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'lema')