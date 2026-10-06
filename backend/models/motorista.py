from database import obter_conexao

def inserir_motorista_banco(nome: str, cnh: str, categoria_cnh: str, pontos_cnh: int):
    conexao = obter_conexao()
    try:
        with conexao.cursor() as cursor:
            sql = """
                INSERT INTO Motorista (nome, cnh, categoria_cnh, pontos_cnh, status_m) 
                VALUES (%s, %s, %s, %s, 'ativo')
            """
            cursor.execute(sql, (nome, cnh, categoria_cnh, pontos_cnh))
            conexao.commit()
            return True
    except Exception as e:
        print(f"Erro ao inserir motorista: {e}")
        return False
    finally:
        conexao.close()


def buscar_motorista_por_id_banco(id_motorista: int):
    conexao = obter_conexao()
    
    try:
        with conexao.cursor() as cursor:
            sql = "SELECT id_motorista, nome, cnh, categoria_cnh, pontos_cnh, status_m FROM Motorista WHERE id_motorista = %s"
            cursor.execute(sql, (id_motorista,))
            return cursor.fetchone()
    except Exception as e:
        print(f"Erro ao buscar motorista por ID: {e}")
        return None
    finally:
        conexao.close()


def atualizar_motorista_banco(id_motorista: int, nome: str, cnh: str, categoria_cnh: str, pontos_cnh: int):
    conexao = obter_conexao()
    try:
        with conexao.cursor() as cursor:
            sql = """
                UPDATE Motorista 
                SET nome = %s, cnh = %s, categoria_cnh = %s, pontos_cnh = %s 
                WHERE id_motorista = %s
            """
            cursor.execute(sql, (nome, cnh, categoria_cnh, pontos_cnh, id_motorista))
            conexao.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar motorista: {e}")
        return False
    finally:
        conexao.close()


def atualizar_status_motorista_banco(id_motorista: int, novo_status_m: str, conexao=None):
    conexao_propria=False

    if conexao is None:
        conexao = obter.conexao()
        conexao_propria=True
    
    try:
        with conexao.cursor() as cursor:
            sql = "UPDATE Motorista SET status_m = %s WHERE id_motorista = %s"
            cursor.execute(sql, (novo_status_m, id_motorista))
            if conexao_propria:
                conexao.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar status do motorista: {e}")
        return False
    finally:
        if conexao_propria == True:
            conexao.close()


def listar_todos_motoristas_banco():
    conexao = obter_conexao()
    try:
        with conexao.cursor() as cursor:
            # CORREÇÃO: Ajustado a sintaxe do cursor padrão para evitar quebras
            sql = "SELECT id_motorista, nome, cnh, categoria_cnh, pontos_cnh, status_m FROM Motorista"
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao listar motoristas no banco: {e}")
        return []
    finally:
        conexao.close()


def deletar_motorista_banco(id_motorista: int):
    conexao = obter_conexao()
    try:
        with conexao.cursor() as cursor:
            # CORREÇÃO: Sintaxe limpa para a remoção
            sql = "DELETE FROM Motorista WHERE id_motorista = %s"
            cursor.execute(sql, (id_motorista,))
            conexao.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao deletar motorista: {e}")
        return False
    finally:
        conexao.close()
