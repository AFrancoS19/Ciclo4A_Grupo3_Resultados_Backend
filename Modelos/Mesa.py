from db import db


class Mesa(db.Model):
    __tablename__ = "Mesa"

    id = db.Column(db.Integer,primary_key=True)
    n_mesa = db.Column(db.Integer())
    cant_inscritos = db.Column(db.Integer())

    def __init__(self,n_mesa=None,cant_inscritos=None):
        self.n_mesa = n_mesa
        self.cant_inscritos = cant_inscritos

    def res(self):
        return {
            "id":self.id,
            "n_mesa": self.n_mesa,
            "cant_inscritos":self.cant_inscritos
        }



    def __repr__(self):
        return f"Id: {self.id}, num mesa : {self.n_mesa}, Cantidad de inscritos : {self.cant_inscritos}"