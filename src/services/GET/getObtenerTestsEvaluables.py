from src.database.db import connection
from src.models.TestEvaluable import TestEvaluable

def getObtenerTestsEvaluables():
  try:
    conn = connection()
    
    tests = []
    inst =  '''
            select distinct tr.id_test_res, concat(p.nombres, ' ', p.paterno, ' ', p.materno) as estudiante, t.tipo, tr.puntaje_total,
                tr.fecha, r.nivel, d.descripcion, d.resultado, d.recomend
              from test_resuelto tr, persona p, usuario u, estudiante_historia eh, historia_test_resuelto htr, test_resuelto_detalle trd, 
                test_detalle td, test_pregunta tp, test t, test_rango tra, rango r, diag_automatico_test_rango datr, diag_automatico da,
                diagnostico d
              where u.id_pers = p.id_pers and eh.id_est = u.id_usu and eh.id_hist = htr.id_hist and htr.id_test_res = tr.id_test_res
                and trd.id_test_res = tr.id_test_res and td.id_test_det = trd.id_test_det and tp.id_test_preg = td.id_test_preg
                and tp.id_test = t.id_test and tr.id_test_res not in (select detr.id_test_res from diag_especialista_test_resuelto detr)
                and tra.id_ran = r.id_ran and datr.id_test_ran = tra.id_test_ran  and datr.id_dauto = da.id_dauto and da.id_diag = d.id_diag
                and r.minimo <= tr.puntaje_total and r.maximo >= tr.puntaje_total and tra.id_test = t.id_test
              order by puntaje_total desc, tipo desc;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        test = TestEvaluable(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        test.id_test_res = row[0]
        tests.append(test.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    
    return tests
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''