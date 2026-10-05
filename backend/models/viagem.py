from database import obter_conexao


def inserir_viagem(id_motorista, id_veiculo,peso_carga_kg, origem, destino, data_hora_saida=None, data_hora_chegada=None):
    conexao = obter_conexao()
    try:
        
        sql = """
            INSERT INTO Viagem (id_motorista, id_veiculo, peso_carga_kg, origem, destino, data_hora_saida, data_hora_chegada, status_vi)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        with conexao.cursor() as cursor:
            dt_saida = data_hora_saida if data_hora_saida else None
            dt_chegada = data_hora_chegada if data_hora_chegada else None
            peso_numerico = float(peso_carga_kg) if peso_carga_kg is not None else 0.0
            
            
            cursor.execute(sql, (
                id_motorista, 
                id_veiculo, 
                peso_numerico,
                origem, 
                destino,  
                dt_saida, 
                dt_chegada, 
                'agendada'
            ))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao inserir viagem: {e}")
        return False
    finally:
        conexao.close()

def buscar_viagem_por_id(id_viagem):
    conexao = obter_conexao()
    try:
        sql = """ SELECT * FROM Viagem WHERE id_viagem = %s 
        """
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_viagem,))
            viagem = cursor.fetchone()
            return viagem
    
    except Exception as e:
        print(f"Erro ao buscar viagem: {e}")
        return None
    
    finally:
        conexao.close()

def verificar_viagem_existente(id_veiculo, id_motorista, data_hora_saida):
    conexao = obter_conexao()
    try:
        sql = """
            SELECT * FROM Viagem 
            WHERE (id_veiculo = %s OR id_motorista = %s) AND data_hora_saida = %s
        """
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_veiculo, id_motorista, data_hora_saida))    
            viagem_existente = cursor.fetchone()
            return viagem_existente is not None 

    except Exception as e:
        print(f"Erro ao verificar viagem existente: {e}")
        return False

    finally:
        conexao.close()

def listar_todas_viagens(): 
    conexao = obter_conexao()
    try:
        sql = """SELECT
            Viagem.*,
            Motorista.nome AS nome_motorista,
            Veiculo.modelo AS modelo_veiculo
        FROM Viagem 
        JOIN Motorista ON Viagem.id_motorista = Motorista.id_motorista
        JOIN Veiculo ON Viagem.id_veiculo = Veiculo.id_veiculo"""
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao listar viagens: {e}")
        return []
    finally:
        conexao.close()

def atualizar_viagem_concluida(id_viagem, novo_status, nova_data_chegada):
    conexao = obter_conexao()
    try:
        # A query agora atualiza as duas colunas ao mesmo tempo
        sql = "UPDATE Viagem SET status_vi = %s, data_hora_chegada = %s WHERE id_viagem = %s"
        with conexao.cursor() as cursor:
            cursor.execute(sql, (novo_status, nova_data_chegada, id_viagem))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao atualizar viagem: {e}")
        return False
    finally:
        conexao.close()

def deletar_viagem_banco(id_viagem):
    conexao = obter_conexao()
    try:
        sql = "DELETE FROM Viagem WHERE id_viagem = %s"
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_viagem,))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao deletar viagem: {e}")
        return False
    finally:
        conexao.close()

def motorista_em_viagem(id_motorista: int):
    conexao = obter_conexao()
    try:
        sql = """SELECT * FROM Viagem WHERE id_motorista = %s AND status = "em_andamento" """
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_motorista,))
            resultado = cursor.fetchone()
            if resultado:
              return True
            else:
                return False

    except Exception as e:
        print(f"Motorista em viagem e não pode alterar: {e}")
          return False
    finally:
        conexao.close()
       
               
