from src.database.db import db

class Test(db.Model):
  id_test = db.Column(db.Integer, primary_key=True)
  tipo = db.Column(db.Text)
  descripcion = db.Column(db.Text)
  recomendacion = db.Column(db.Text)

  def __init__(self, tipo, descripcion, recomendacion) -> None:
    self.tipo = tipo
    self.descripcion = descripcion
    self.recomendacion = recomendacion
  
  def to_json(self):
    return {
      'id_test': self.id_test,
      'tipo' : self.tipo,
      'descripcion' : self.descripcion,
      'recomendacion' : self.recomendacion
    }