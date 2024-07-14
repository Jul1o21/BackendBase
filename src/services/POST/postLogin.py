from src.database.db import connection
from src.models.UsuarioLog import UsuarioLog

def postLogin(correo, contra):
  try:
    conn = connection()
    
    usuarioLog = ''
    inst =  '''
            select u.id_usu, p.id_pers, p.nombres, p.paterno, p.materno, tu.rol
              from persona p, usuario u, tipo_usuario tu
              where p.id_pers = u.id_pers and u.id_tipo_usu = tu.id_tipo_usu
                and u.correo = %(email)s and u.contrasenia = %(contra)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'email': correo, 'contra':contra})
      for row in cursor.fetchall():
        usuarioLog = UsuarioLog(row[1], row[2], row[3], row[4], row[5])
        usuarioLog.id_usu = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    
    return usuarioLog.to_json()
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''