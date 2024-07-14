from src.database.db import connection
from src.models.UbigeoEst import UbigeoEst

def postObtenerUbigeosEst():
  try:
    conn = connection()
    
    ubigeos = []
    inst =  '''
            select us.id_usu, p.id_pers, concat(p.nombres, ' ', p.paterno, ' ', p.materno) as estudiante,
                u.id_ubi, u.distrito, pr.provincia, d.departamento , u.x, u.y
              from ubigeo u, persona p, usuario us, departamento d, departamento_provincia dp, provincia pr, provincia_ubigeo pu, tipo_usuario tu
              where p.id_ubi = u.id_ubi and us.id_pers = p.id_pers and d.id_dep = dp.id_dep and dp.id_prov = pr.id_prov and tu.id_tipo_usu = us.id_tipo_usu 
                and pr.id_prov = pu.id_prov and pu.id_ubi = u.id_ubi and tu.rol = 'estudiante';
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        ubigeo = UbigeoEst(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], '', '', '', '')
        ubigeo.id_usu = row[0]
        ubigeos.append(ubigeo)
      cursor.close()
    
    for ubigeo in ubigeos:
      inst1 =  '''
            select distinct max(tr.id_test_res)
              from test_resuelto tr, usuario u, estudiante_historia eh, historia_test_resuelto htr
              where eh.id_est = u.id_usu and eh.id_hist = htr.id_hist and htr.id_test_res = tr.id_test_res
                and u.id_usu = %(id_usu)s;
            '''
      with conn.cursor() as cursor:
        cursor.execute(inst1, {'id_usu':ubigeo.id_usu})
        for row in cursor.fetchall():
          ubigeo.id_test_res = row[0]
        cursor.close()
      
      if ubigeo.id_test_res == None:
        ubigeo.id_test_res = 0
    
    for ubigeo in ubigeos:
      inst2 =  '''
            select distinct tr.id_test_res, to_char(tr.fecha, 'DD-MM-YYYY'), t.tipo, r.nivel
              from test_resuelto tr, persona p, usuario u, estudiante_historia eh, historia_test_resuelto htr, test_resuelto_detalle trd, 
                test_detalle td, test_pregunta tp, test t, test_rango tra, rango r, diag_automatico_test_rango datr, diag_automatico da,
                diagnostico d
              where u.id_pers = p.id_pers and eh.id_est = u.id_usu and eh.id_hist = htr.id_hist and htr.id_test_res = tr.id_test_res
                and trd.id_test_res = tr.id_test_res and td.id_test_det = trd.id_test_det and tp.id_test_preg = td.id_test_preg
                and tp.id_test = t.id_test
                and tra.id_ran = r.id_ran and datr.id_test_ran = tra.id_test_ran  and datr.id_dauto = da.id_dauto and da.id_diag = d.id_diag
                and r.minimo <= tr.puntaje_total and r.maximo >= tr.puntaje_total and tra.id_test = t.id_test and tr.id_test_res = %(id_test_res)s;
            '''
      with conn.cursor() as cursor:
        cursor.execute(inst2, {'id_test_res':ubigeo.id_test_res})
        for row in cursor.fetchall():
          ubigeo.fecha = row[1]
          ubigeo.tipo = row[2]
          ubigeo.nivel = row[3]
        cursor.close()
    
    ubigeos_json = []
    
    for ubigeo in ubigeos:
      ubigeos_json.append(ubigeo.to_json())
    
    return ubigeos_json
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''