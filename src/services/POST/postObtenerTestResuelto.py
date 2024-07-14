from src.database.db import connection
from src.models.TestResuelto import TestResuelto

def postObtenerTestResuelto(id_test_res):
  try:
    conn = connection()
    
    test = ''
    
    inst =  '''
            select distinct tr.id_test_res, t.tipo, tr.puntaje_total, d.resultado, to_char(tr.fecha, 'DD-MM-YYYY') as fecha, eh.id_hist
              from test_resuelto tr, persona p, usuario u, estudiante_historia eh, historia_test_resuelto htr, test_resuelto_detalle trd, 
                test_detalle td, test_pregunta tp, test t, test_rango tra, rango r, diag_automatico_test_rango datr, diag_automatico da,
                diagnostico d
              where u.id_pers = p.id_pers and eh.id_est = u.id_usu and eh.id_hist = htr.id_hist and htr.id_test_res = tr.id_test_res
                and trd.id_test_res = tr.id_test_res and td.id_test_det = trd.id_test_det and tp.id_test_preg = td.id_test_preg
                and tp.id_test = t.id_test
                and tra.id_ran = r.id_ran and datr.id_test_ran = tra.id_test_ran  and datr.id_dauto = da.id_dauto and da.id_diag = d.id_diag
                and r.minimo <= tr.puntaje_total and r.maximo >= tr.puntaje_total and tra.id_test = t.id_test
                and tr.id_test_res = %(id_test_res)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test_res':id_test_res})
      for row in cursor.fetchall():
        test = TestResuelto(row[1], row[2], row[3], row[4], row[5])
        test.id_test_res = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    
    return test
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''