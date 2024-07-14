from src.database.db import db

class Departamento(db.Model):
  id_dep = db.Column(db.Integer, primary_key = True)
  departamento = db.Column(db.String(50))

  def __init__(self, departamento) -> None:
    self.departamento = departamento
    
  def to_json(self):
    return {
      'id_dep': self.id_dep,
      'departamento' : self.departamento
    }