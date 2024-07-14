from src.database.db import db

class DiagnosticoEsp(db.Model):
  id_diag = db.Column(db.Integer, primary_key = True)
  descripcion = db.Column(db.Text)
  resultado = db.Column(db.Text)
  recomendacion = db.Column(db.Text)
  tratamiento = db.Column(db.Integer)
  notas_seguim = db.Column(db.Text)

  def __init__(self, descripcion, resultado, recomendacion, tratamiento, notas_seguim) -> None:
    self.descripcion = descripcion
    self.resultado = resultado
    self.recomendacion = recomendacion
    self.tratamiento = tratamiento
    self.notas_seguim = notas_seguim
    
  def to_json(self):
    return {
      'id_diag': self.id_diag,
      'descripcion' : self.descripcion,
      'resultado' : self.resultado,
      'recomendacion' : self.recomendacion,
      'tratamiento' : self.tratamiento,
      'notas_seguim' : self.notas_seguim
    }