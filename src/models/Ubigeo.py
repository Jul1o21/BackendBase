from src.database.db import db

class Ubigeo(db.Model):
  id_ubi = db.Column(db.Integer, primary_key = True)
  numero = db.Column(db.Integer)
  distrito = db.Column(db.String(50))
  poblacion = db.Column(db.Integer)
  superficie = db.Column(db.Float)
  x = db.Column(db.Float)
  y = db.Column(db.Float)

  def __init__(self, numero, distrito, poblacion,superficie,x,y) -> None:
    self.numero = numero
    self.distrito = distrito
    self.poblacion = poblacion
    self.superficie = superficie
    self.x = x
    self.y = y
    
    
  def to_json(self):
    return {
      'id_ubi': self.id_ubi,
      'numero': self.numero,
      'distrito': self.distrito,
      'poblacion': self.poblacion,
      'superficie': self.superficie,
      'x': self.x,
      'y': self.y
    }