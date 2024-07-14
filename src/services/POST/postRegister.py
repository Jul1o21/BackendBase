from src.database.db import connection

def postRegister(nombre, paterno, materno, correo, contra, tipo):
  try:
    conn = connection()
    
    id_pers = ''
    inst =  '''
            insert into persona(nombres, paterno, materno)
              values(%(nombre)s, %(paterno)s, %(materno)s)
              returning id_pers;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'nombre': nombre, 'paterno':paterno, 'materno':materno})
      for row in cursor.fetchall():
        id_pers = row[0]
      cursor.close()
    
    inst =  '''insert into usuario(correo, contrasenia, id_pers, id_tipo_usu)
              values(%(correo)s, %(contra)s, %(id_pers)s, %(tipo)s);
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'correo':correo, 'contra':contra, 'id_pers':id_pers, 'tipo':tipo})
      conn.commit()
      cursor.close()
    conn.close()
    
    return True
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return False