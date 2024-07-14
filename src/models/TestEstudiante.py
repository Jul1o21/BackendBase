from src.database.db import db

class TestEstudiante(db.Model):
  id_test_res = db.Column(db.Integer, primary_key=True)
  puntaje_total = db.Column(db.Integer)
  tipo_test = db.Column(db.Text)
  desc_test = db.Column(db.Text)

  def __init__(self, puntaje_total, tipo_test, desc_test) -> None:
    self.puntaje_total = puntaje_total
    self.tipo_test = tipo_test
    self.desc_test = desc_test
  
  def to_json(self):
    return {
      'id_test_res': self.id_test_res,
      'puntaje_total' : self.puntaje_total,
      'tipo_test' : self.tipo_test,
      'desc_test' : self.desc_test
    }