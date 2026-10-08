from database import obter_conexao

def buscar_usuario_por_email(email):
    conexao = None

    try:
        conexao = obter_conexao()
        
        sql= """SELECT * FROM Usuarios WHERE email = %s"""

        with conexao.cursor() as cursor:
             cursor.execute(sql, (email,))
             return cursor.fetchone()
    
    except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            raise
    
    finally:
        if conexao is not None:
            conexao.close()
    