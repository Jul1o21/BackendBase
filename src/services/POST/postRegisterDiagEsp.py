from src.database.db import connection

def postRegisterDiagEsp(id_esp, id_test_res, descripcion, resultado, recomendacion, tratamiento, notas):
  try:
    conn = connection()
    
    id_diag = 0
    id_desp = 0
    
    inst =  '''
            insert into diagnostico(descripcion, resultado, recomend)
              values(%(descripcion)s, %(resultado)s, %(recomendacion)s)
              returning id_diag;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'descripcion': descripcion, 'resultado': resultado, 'recomendacion':recomendacion})
      for row in cursor.fetchall():
        id_diag = row[0]
      cursor.close()
    
    inst =  '''
            insert into diag_especialista(recomend_adic_desp, tratamiento_desp, notas_seg_desp_not, fecha, id_diag)
              values('-', %(tratamiento)s, %(notas)s, to_date(current_date::text, 'YYYY-MM-DD'), %(id_diag)s)
              returning id_desp;
            '''

    with conn.cursor() as cursor:
      cursor.execute(inst, {'tratamiento': tratamiento, 'notas': notas, 'id_diag':id_diag})
      for row in cursor.fetchall():
        id_desp = row[0]
      cursor.close()
    
    inst =  '''
            insert into especialista_diag_especialista(id_esp, id_desp)
	            values(%(id_esp)s, %(id_desp)s);
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_esp': id_esp, 'id_desp':id_desp})
      cursor.close()
    
    inst =  '''
            insert into diag_especialista_test_resuelto(id_desp, id_test_res)
	            values(%(id_desp)s, %(id_test_res)s);
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_desp': id_desp, 'id_test_res':id_test_res})
      conn.commit()
      cursor.close()
    conn.close()
    
    return True
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return False