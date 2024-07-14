from src.database.db import connection
from src.models.Historia import Historia

def postObtenerUnaHistoriaT(id_usu, id_test_res):
  try:
    conn = connection()
    
    historia = ''
    inst =  '''
            select h.id_hist, to_char(h.apertura, 'DD-MM-YYYY') as apertura, h.estado, to_char(h.alta , 'DD-MM-YYYY') as alta
              from historia h, estudiante_historia eh, historia_test_resuelto htr
              where eh.id_est = %(id_usu)s and eh.id_hist = h.id_hist and htr.id_hist = h.id_hist and htr.id_test_res = %(id_test_res)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_usu': id_usu, 'id_test_res': id_test_res})
      for row in cursor.fetchall():
        historia = Historia(row[1], row[2], row[3])
        historia.id_hist = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    
    return historia
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''