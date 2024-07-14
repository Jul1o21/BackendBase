from src.database.db import db

class DiagnosticoAuto(db.Model):
  id_diag = db.Column(db.Integer, primary_key = True)
  descripcion = db.Column(db.Text)
  resultado = db.Column(db.Text)
  recomendacion = db.Column(db.Text)
  puntaje_total = db.Column(db.Integer)
  rango = db.Column(db.Text)

  def __init__(self, descripcion, resultado, recomendacion, puntaje_total, rango) -> None:
    self.descripcion = descripcion
    self.resultado = resultado
    self.recomendacion = recomendacion
    self.puntaje_total = puntaje_total
    self.rango = rango
    
  def to_json(self):
    return {
      'id_diag': self.id_diag,
      'descripcion' : self.descripcion,
      'resultado' : self.resultado,
      'recomendacion' : self.recomendacion,
      'puntaje_total' : self.puntaje_total,
      'rango' : self.rango
    }