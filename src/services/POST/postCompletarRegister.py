from src.database.db import connection

def postCompletarRegister(id_pers, nombre, paterno, materno, num_documento, sexo, edad, num_celular, id_ubi):
  try:
    conn = connection()
    
    inst =  '''
            update persona set nombres = %(nombre)s, paterno = %(paterno)s, materno = %(materno)s,
                num_documento = %(num_documento)s, sexo = %(sexo)s, edad = %(edad)s, num_celular = %(num_celular)s, id_ubi = %(id_ubi)s
              where id_pers = %(id_pers)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'nombre': nombre, 'paterno':paterno, 'materno':materno, 'num_documento':num_documento, 'sexo':sexo, 'edad':edad, 'num_celular':num_celular, 'id_ubi':id_ubi, 'id_pers':id_pers})
      conn.commit()
      cursor.close()
    conn.close()
    
    return True
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return False