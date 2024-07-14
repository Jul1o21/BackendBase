from src.database.db import connection
from src.models.Departamento import Departamento

def getObtenerDepartamentos():
  try:
    conn = connection()
    
    departamentos = []
    inst =  '''
            select d.*
              from departamento d
              order by d.departamento;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        depart = Departamento(row[1])
        depart.id_dep = row[0]
        departamentos.append(depart.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    
    return departamentos
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''