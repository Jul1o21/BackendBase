from src.database.db import connection
from src.models.TestResumen import TestResumen

def postObtenerTestDetalle(id_test_res):
  try:
    conn = connection()
    
    respuestas = []
    
    inst =  '''
            select td.id_test_det, t.tipo, p.descripcion, td.puntaje
              from test_resuelto tr, test_resuelto_detalle trd, test_detalle td, test_pregunta tp, pregunta p, test t 
              where tr.id_test_res = trd.id_test_res and trd.id_test_det = td.id_test_det and td.id_test_preg = tp.id_test_preg and tp.id_preg = p.id_preg
                and t.id_test = tp.id_test and trd.id_test_res = %(id_test_res)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test_res':id_test_res})
      for row in cursor.fetchall():
        test = TestResumen(row[1], row[2], row[3])
        test.id_test_det = row[0]
        respuestas.append(test.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    
    return respuestas
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''