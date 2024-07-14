from src.database.db import connection
from src.models.Test import Test
from src.models.Pregunta import Pregunta

def postObtenerTest(id_test):
  try:
    conn = connection()
    
    test = ''
    preguntas = []
    inst =  '''
            select p.*
              from pregunta p, test_pregunta tp
              where p.id_preg = tp.id_preg and tp.id_test = %(id_test)s
              order by p.id_preg;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test': id_test})
      for row in cursor.fetchall():
        pregunta = Pregunta(row[1], row[2], row[3])
        pregunta.id_preg = row[0]
        preguntas.append(pregunta.to_json())
      cursor.close()
    
    inst =  '''
            select * from test where id_test = %(id_test)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test': id_test})
      for row in cursor.fetchall():
        test = Test(row[1], row[2], row[3])
        test.id_test = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    
    result = {'test':test.to_json(), 'preguntas':preguntas}
    
    return result
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''