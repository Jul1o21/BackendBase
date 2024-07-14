from src.database.db import connection
from src.models.DiagnosticoEsp import DiagnosticoEsp

def postObtenerDiagEspTestResuelto(id_test_res):
  try:
    conn = connection()
    
    diagnostico = ''
    
    inst =  '''
            select d.id_diag, d.descripcion, d.resultado, d.recomend, de.tratamiento_desp, de.notas_seg_desp_not
              from diagnostico d, diag_especialista de, diag_especialista_test_resuelto detr
              where d.id_diag = de.id_diag and de.id_desp = detr.id_desp and detr.id_test_res = %(id_test_res)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test_res':id_test_res})
      for row in cursor.fetchall():
        diagnostico = DiagnosticoEsp(row[1], row[2], row[3], row[4], row[5])
        diagnostico.id_diag = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    
    return diagnostico
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''