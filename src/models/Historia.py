from src.database.db import db

class Historia(db.Model):
  id_hist = db.Column(db.Integer, primary_key = True)
  apertura_hist = db.Column(db.String(50))
  estado_hist = db.Column(db.String(50))
  alta_hist = db.Column(db.String(50))

  def __init__(self, apertura_hist, estado_hist, alta_hist) -> None:
    self.estado_hist = estado_hist
    self.apertura_hist = apertura_hist
    self.alta_hist = alta_hist
    
  def to_json(self):
    return {
      'id_hist': self.id_hist,
      'estado_hist' : self.estado_hist,
      'apertura_hist' : self.apertura_hist,
      'alta_hist' : self.alta_hist
    }