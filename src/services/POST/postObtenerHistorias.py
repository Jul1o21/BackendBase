from src.database.db import connection
from src.models.Historia import Historia

def postObtenerHistorias(id_usu):
  try:
    conn = connection()
    
    historias = []
    inst =  '''
            select h.id_hist, to_char(h.apertura, 'DD-MM-YYYY') as apertura, h.estado, to_char(h.alta , 'DD-MM-YYYY') as alta
              from historia h, estudiante_historia eh
              where eh.id_est = %(id_usu)s and eh.id_hist = h.id_hist;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_usu': id_usu})
      for row in cursor.fetchall():
        historia = Historia(row[1], row[2], row[3])
        historia.id_hist = row[0]
        historias.append(historia.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    
    return historias
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''