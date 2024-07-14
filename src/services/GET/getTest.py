from src.database.db import connection
from src.models.Test import Test

def getTests():
  try:
    conn = connection()
    tests = []
    inst =  '''
              select * from test;
            '''
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        test = Test(row[1], row[2], row[3])
        test.id_test = row[0]
        tests.append(test.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    return tests
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''