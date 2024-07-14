from src.database.db import connection
from src.models.Ubigeo import Ubigeo

def postObtenerUbigeos(id_prov):
  try:
    conn = connection()
    
    ubigeos = []
    inst =  '''
            select u.*
              from ubigeo u, provincia_ubigeo pu, provincia p
              where u.id_ubi = pu.id_ubi and pu.id_prov = p.id_prov and p.id_prov = %(id_prov)s
              order by u.distrito;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_prov': id_prov})
      for row in cursor.fetchall():
        ubigeo = Ubigeo(row[1], row[2], row[3], row[4], row[5], row[6])
        ubigeo.id_ubi = row[0]
        ubigeos.append(ubigeo.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    
    return ubigeos
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''