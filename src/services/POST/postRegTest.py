from src.database.db import connection
from src.models.DiagnosticoAuto import DiagnosticoAuto

def postRegTest(id_est, matrizPreg):
  try:
    conn = connection()
    
    id_hist = 0
    id_test_res = 0
    id_test_det_array = []
    puntaje_completo = 0
    diagnostico = ''
    
    inst =  '''
            select max(h.id_hist) as id_hist from historia h, estudiante_historia eh
	            where h.id_hist = eh.id_hist and h.estado = 'abierto' and eh.id_est = %(id_est)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_est': id_est})
      for row in cursor.fetchall():
        id_hist = row[0]
      cursor.close()
    
    if (id_hist == 0 or id_hist == None):
      print('No se encontró id_hist, se creará')
      inst =  '''
              insert into historia(apertura, estado)
                values(to_date(current_date::text, 'YYYY-MM-DD'), 'abierto')
                returning id_hist;
              '''
      with conn.cursor() as cursor:
        cursor.execute(inst, )
        for row in cursor.fetchall():
          id_hist = row[0]
        cursor.close()
      
      inst =  '''
              insert into estudiante_historia(id_est, id_hist)
	              values(%(id_est)s, %(id_hist)s);
              '''
      with conn.cursor() as cursor:
        cursor.execute(inst, {'id_est': id_est, 'id_hist': id_hist})
        cursor.close()
    
    print('Se encontró la história con ID:', id_hist)
    
    inst =  '''
            insert into test_resuelto (puntaje_total, fecha)
              values(0, to_date(current_date::text, 'YYYY-MM-DD'))
              returning id_test_res;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        id_test_res = row[0]
      cursor.close()
    
    inst =  '''
            insert into historia_test_resuelto(id_hist, id_test_res)
	            values(%(id_hist)s, %(id_test_res)s);
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_hist':id_hist, 'id_test_res':id_test_res})
      cursor.close()
    
    result = ''
    
    for fila in matrizPreg:
      result += "\n"
      id_pregunta = fila[0]
      puntaje = fila[1]
      result += f'((select id_test_preg from test_pregunta where id_preg = {id_pregunta}), {puntaje}),'
      
    result = result.rstrip(result[-1]) + "\n"
    
    inst =  'insert into test_detalle(id_test_preg, puntaje)\n values ' + result + '\nreturning id_test_det;'
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        id_test_det_array.append(row[0])
      cursor.close()
    
    print(id_test_det_array)
    
    result = ''
    
    for id in id_test_det_array:
      result += "\n"
      result += f'({id_test_res}, {id}),'
    
    result = result.rstrip(result[-1]) + "\n"
    
    inst =  'insert into test_resuelto_detalle(id_test_res, id_test_det)\n values ' + result + ';'
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      cursor.close()
    
    inst =  '''
            update test_resuelto
              set puntaje_total = (select sum(td.puntaje) from test_detalle td, test_resuelto_detalle trd
                where td.id_test_det = trd.id_test_det and trd.id_test_res = %(id_test_res)s)
              where id_test_res = %(id_test_res)s
              returning puntaje_total;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test_res': id_test_res})
      for row in cursor.fetchall():
        puntaje_completo = row[0]
      cursor.close()
    
    inst =  '''
            select d.*, tr2.puntaje_total, concat('[', r.minimo, ', ', r.maximo, ']') as rango
              from diag_automatico da, diagnostico d, test t, test_rango tr, rango r, diag_automatico_test_rango datr,
                test te, test_pregunta tp, test_detalle td, test_resuelto_detalle trd, test_resuelto tr2
              where d.id_diag = da.id_diag and t.id_test = tr.id_test and tr.id_ran = r.id_ran and tr.id_test_ran = datr.id_test_ran 
                and datr.id_dauto = da.id_dauto and te.id_test = tp.id_test and tp.id_test_preg = td.id_test_preg and te.id_test = tr.id_test
                and td.id_test_det = trd.id_test_det and trd.id_test_res = %(id_test_res)s and tr2.id_test_res = trd.id_test_res 
                and r.minimo <= %(puntaje_completo)s and r.maximo >= %(puntaje_completo)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'puntaje_completo': puntaje_completo, 'id_test_res':id_test_res})
      for row in cursor.fetchall():
        diagnostico = DiagnosticoAuto(row[1], row[2], row[3], row[4], row[5])
        diagnostico.id_diag = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    
    return diagnostico
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''