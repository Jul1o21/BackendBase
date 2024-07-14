from src.database.db import connection
from src.models.Persona import Persona

def postObtenerPersona(id_pers):
  try:
    conn = connection()
    
    persona = ''
    inst =  '''
            select * from persona where id_pers = %(id_pers)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_pers': id_pers})
      for row in cursor.fetchall():
        persona = Persona(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        persona.id_pers = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    
    return persona
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''