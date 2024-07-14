from src.database.db import db

class Pregunta(db.Model):
  id_preg = db.Column(db.Integer, primary_key = True)
  descripcion = db.Column(db.Text)
  puntaje_minimo = db.Column(db.Integer)
  puntaje_maximo = db.Column(db.Integer)

  def __init__(self, descripcion, puntaje_minimo, puntaje_maximo) -> None:
    self.descripcion = descripcion
    self.puntaje_minimo = puntaje_minimo
    self.puntaje_maximo = puntaje_maximo
  
  def to_json(self):
    return {
      'id_preg': self.id_preg,
      'descripcion': self.descripcion,
      'puntaje_minimo': self.puntaje_minimo,
      'puntaje_maximo': self.puntaje_maximo
    }