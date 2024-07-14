from src.database.db import db

class UsuarioLog(db.Model):
  id_usu = db.Column(db.Integer, primary_key = True)
  id_pers = db.Column(db.Integer)
  nombres = db.Column(db.String(50))
  paterno = db.Column(db.String(50))
  materno = db.Column(db.String(50))
  rol = db.Column(db.String(50))

  def __init__(self, id_pers, nombres, paterno, materno, rol) -> None:
    self.id_pers = id_pers
    self.nombres = nombres
    self.paterno = paterno
    self.materno = materno
    self.rol = rol
    
  def to_json(self):
    return {
      'id_usu': self.id_usu,
      'id_pers' : self.id_pers,
      'nombres' : self.nombres,
      'paterno' : self.paterno,
      'materno' : self.materno,
      'rol' : self.rol
    }