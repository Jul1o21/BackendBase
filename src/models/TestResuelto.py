from src.database.db import db

class TestResuelto(db.Model):
  id_test_res = db.Column(db.Integer, primary_key = True)
  tipo = db.Column(db.Text)
  puntaje_total = db.Column(db.Integer)
  resultado = db.Column(db.Text)
  fecha = db.Column(db.Text)
  id_hist = db.Column(db.Integer)

  def __init__(self, tipo, puntaje_total, resultado, fecha, id_hist) -> None:
    self.tipo = tipo
    self.puntaje_total = puntaje_total
    self.resultado = resultado
    self.fecha = fecha
    self.id_hist = id_hist
    
    
  def to_json(self):
    return {
      'id_test_res': self.id_test_res,
      'tipo': self.tipo,
      'puntaje_total': self.puntaje_total,
      'resultado': self.resultado,
      'fecha': self.fecha,
      'id_hist': self.id_hist
    }