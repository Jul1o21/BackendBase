from src.database.db import db

class UbigeoEst(db.Model):
  id_usu = db.Column(db.Integer, primary_key = True)
  id_pers = db.Column(db.Integer)
  estudiante = db.Column(db.Text)
  id_ubi = db.Column(db.Integer)
  distrito = db.Column(db.Text)
  provincia = db.Column(db.Text)
  departamento = db.Column(db.Text)
  x = db.Column(db.Float)
  y = db.Column(db.Float)
  id_test_res = db.Column(db.Integer)
  fecha = db.Column(db.Text)
  tipo = db.Column(db.Text)
  nivel = db.Column(db.Text)

  def __init__(self, id_pers, estudiante, id_ubi, distrito, provincia, departamento, x, y, id_test_res, fecha, tipo, nivel) -> None:
    self.id_pers = id_pers
    self.estudiante = estudiante
    self.id_ubi = id_ubi
    self.distrito = distrito
    self.provincia = provincia
    self.departamento = departamento
    self.x = x
    self.y = y
    self.id_test_res = id_test_res
    self.fecha = fecha
    self.tipo = tipo
    self.nivel = nivel
    
    
  def to_json(self):
    return {
      'id_usu': self.id_usu,
      'id_pers': self.id_pers,
      'estudiante': self.estudiante,
      'id_ubi': self.id_ubi,
      'distrito': self.distrito,
      'provincia': self.provincia,
      'departamento': self.departamento,
      'x': self.x,
      'y': self.y,
      'id_test_res': self.id_test_res,
      'fecha': self.fecha,
      'tipo': self.tipo,
      'nivel': self.nivel
    }