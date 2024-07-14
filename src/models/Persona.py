from src.database.db import db

class Persona(db.Model):
  id_pers = db.Column(db.Integer, primary_key = True)
  nombre = db.Column(db.String(50))
  materno = db.Column(db.String(50))
  paterno = db.Column(db.String(50))
  num_documento = db.Column(db.Integer)
  sexo = db.Column(db.String(50))
  edad = db.Column(db.Integer)
  num_celular = db.Column(db.Integer)
  id_ubi = db.Column(db.Integer)

  def __init__(self, nombre, paterno, materno, num_documento, sexo, edad, num_celular, id_ubi) -> None:
    self.nombre = nombre
    self.materno = materno
    self.paterno = paterno
    self.num_documento = num_documento
    self.sexo = sexo
    self.edad = edad
    self.num_celular = num_celular
    self.id_ubi = id_ubi
    
    
    
  def to_json(self):
    return {
      'id_pers': self.id_pers,
      'nombre' : self.nombre,
      'materno' : self.materno,
      'paterno' : self.paterno,
      'num_documento' : self.num_documento,
      'sexo' : self.sexo,
      'edad' : self.edad,
      'num_celular' : self.num_celular,
      'id_ubi' : self.id_ubi
    }