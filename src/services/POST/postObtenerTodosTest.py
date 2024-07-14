from src.database.db import connection
from src.services.POST.postObtenerTestResuelto import postObtenerTestResuelto
from src.services.POST.postObtenerDiagAutoTestResuelto import postObtenerDiagAutoTestResuelto
from src.services.POST.postObtenerDiagEspTestResuelto import postObtenerDiagEspTestResuelto

def postObtenerTodosTest(id_hist):
  try:
    conn = connection()
    
    id_test_res_array = []
    
    inst1 =  '''
            select htr.id_test_res from historia_test_resuelto htr where htr.id_hist = %(id_hist)s order by id_test_res;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst1, {'id_hist':id_hist})
      for row in cursor.fetchall():
        id_test_res_array.append(row[0])
      conn.commit()
      cursor.close()
    conn.close()
    
    results = []
    
    for id_test_res in id_test_res_array:
      test = postObtenerTestResuelto(id_test_res)
      dauto = postObtenerDiagAutoTestResuelto(id_test_res)
      desp = postObtenerDiagEspTestResuelto(id_test_res)
      if test != '':
        test = test.to_json()
      if dauto != '':
        dauto = dauto.to_json()
      if desp != '':
        desp = desp.to_json()
      result = [test, dauto, desp]
      results.append(result)
    
    return results
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''