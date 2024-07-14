from src.database.db import db

class TestResumen(db.Model):
  id_test_det = db.Column(db.Integer, primary_key = True)
  tipo = db.Column(db.Text)
  descripcion = db.Column(db.Text)
  puntaje = db.Column(db.Integer)

  def __init__(self, tipo, descripcion, puntaje) -> None:
    self.tipo = tipo
    self.descripcion = descripcion
    self.puntaje = puntaje
    
    
  def to_json(self):
    return {
      'id_test_det': self.id_test_det,
      'tipo': self.tipo,
      'descripcion': self.descripcion,
      'puntaje': self.puntaje
    }