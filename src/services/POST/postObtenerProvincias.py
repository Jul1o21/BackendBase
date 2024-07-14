from src.database.db import connection
from src.models.Provincia import Provincia

def postObtenerProvincias(id_dep):
  try:
    conn = connection()
    
    provincias = []
    inst =  '''
            select p.*
              from provincia p, departamento_provincia dp
              where dp.id_prov = p.id_prov and dp.id_dep = %(id_dep)s
              order by p.provincia;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_dep': id_dep})
      for row in cursor.fetchall():
        provincia = Provincia(row[1])
        provincia.id_prov = row[0]
        provincias.append(provincia.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    
    return provincias
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''