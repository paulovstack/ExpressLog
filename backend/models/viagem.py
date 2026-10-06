from database import obter_conexao
from models.motorista import atualizar_status_motorista_banco


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

def buscar_viagem_por_id(id_viagem, conexao=None):
    conexao_propria = False
    if conexao is None:
        conexao = obter.conexao()
        conexao_propria = True
    
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
        if conexao_propria == True:
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
        viagem = buscar_viagem_por_id(id_viagem, conexao)
        if not viagem:
            return False
        id_motorista = viagem["id_motorista"]
        novo_status_m = None

        if novo_status == "em_andamento":
            novo_status_m = "em_rota"
        
        elif novo_status in ["concluida", "cancelada"]:
            novo_status_m = "disponivel"
        
        if novo_status_m is not None:
            sucesso = atualizar_status_motorista_banco(id_motorista, novo_status_m, conexao)
            if not sucesso:
                conexao.rollback()
                return False
    
        sql = "UPDATE Viagem SET status_vi = %s, data_hora_chegada = %s WHERE id_viagem = %s"
        with conexao.cursor() as cursor:
            cursor.execute(sql, (novo_status, nova_data_chegada, id_viagem))
        
        conexao.commit()
        return True
    except Exception as e:
        conexao.rollback()
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
        sql = """SELECT * FROM Viagem WHERE id_motorista = %s AND status_vi = %s """
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_motorista, "em_andamento",))
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
       
               
