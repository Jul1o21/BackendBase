from src.database.db import db

class TestEvaluable(db.Model):
  id_test_res = db.Column(db.Integer, primary_key = True)
  estudiante = db.Column(db.Text)
  tipo = db.Column(db.Text)
  puntaje_total = db.Column(db.Integer)
  fecha = db.Column(db.Text)
  nivel = db.Column(db.Text)
  descripcion = db.Column(db.Text)
  resultado = db.Column(db.Text)
  recomend = db.Column(db.Text)

  def __init__(self, estudiante, tipo, puntaje_total, fecha, nivel, descripcion, resultado, recomend) -> None:
    self.estudiante = estudiante
    self.tipo = tipo
    self.puntaje_total = puntaje_total
    self.fecha = fecha
    self.nivel = nivel
    self.descripcion = descripcion
    self.resultado = resultado
    self.recomend = recomend
    
    
    
  def to_json(self):
    return {
      'id_test_res': self.id_test_res,
      'estudiante' : self.estudiante,
      'tipo' : self.tipo,
      'puntaje_total' : self.puntaje_total,
      'fecha' : self.fecha,
      'nivel' : self.nivel,
      'descripcion' : self.descripcion,
      'resultado' : self.resultado,
      'recomend' : self.recomend
    }