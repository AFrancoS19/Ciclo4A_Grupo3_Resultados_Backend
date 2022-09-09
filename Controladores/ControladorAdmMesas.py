from Modelos.Mesa import Mesa
from db import db


class ControladorAdmMesas():
    def __init__(self):
        print("Creando ControladorAdmMesas")

    def index(self):
        resultado = Mesa.query.all()
        lista=[]
        for i in resultado:
            lista.append(i.res())
        return lista

    def create(self,infoMesa):
        n = infoMesa['n_mesa']
        cant = infoMesa['cant_inscritos']
        mesa = Mesa(n_mesa=n, cant_inscritos=cant)
        db.session.add(mesa)
        db.session.commit()
        print("Mesa creada correctamente")
        return {"mensaje": "Mesa creada correctamente"}

    def show(self, id):
        resultado = Mesa.query.get(id)
        print (resultado)
        return resultado.res()

    def delete(self,id):
        resultado=Mesa.query.get(id)
        db.session.delete(resultado)
        db.session.commit()
        print("Mesa "+ id+" eliminada")
        return {"mensaje": "Mesa eliminada correctamente"}

    def update(self,id,infoMesa):
        n = infoMesa.get('n_mesa')
        cant = infoMesa.get('cant_inscritos')
        resultado = Mesa.query.get(id)
        resultado.n_mesa = n
        resultado.cant_inscritos = cant
        db.session.add(resultado)
        db.session.commit()
        print (resultado)
        print("Mesa "+ id+" actualizada")
        return {"mensaje": "Mesa actualizada correctamente"}



