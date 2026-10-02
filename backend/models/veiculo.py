from database import obter_conexao

def inserir_veiculo(placa, modelo, categoria_requerida, capacidade_carga_kg):
    conexao = obter_conexao()
    try:
        with conexao.cursor() as cursor:
          
            sql = """
                INSERT INTO veiculo (placa, modelo, categoria_requerida, capacidade_carga_kg, status_ve) 
                VALUES (%s, %s, %s, %s, 'disponivel')
            """
            cursor.execute(sql, (placa, modelo, categoria_requerida, capacidade_carga_kg))
            conexao.commit()
            return True
            
    except Exception as e:
        print(f"Erro ao inserir veiculo: {e}")
        return False
        
    finally:
        conexao.close()



def buscar_veiculo_por_id(id_veiculo):
    conexao = obter_conexao()
    try:
        sql = "SELECT * FROM Veiculo WHERE id_veiculo = %s"
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_veiculo,))
            veiculo = cursor.fetchone()
            return veiculo

    except Exception as e:
        print(f"Erro ao buscar veículo: {e}")
        return None

    finally:
        conexao.close()

def listar_todos_veiculos():
    conexao = obter_conexao()
    try:
        sql = "SELECT * FROM Veiculo"
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao listar veículos: {e}")
        return []
    finally:
        conexao.close()

def atualizar_status_veiculo(id_veiculo, novo_status_ve):
    conexao = obter_conexao()
    try:
        sql = "UPDATE Veiculo SET status_ve = %s WHERE id_veiculo = %s"
        with conexao.cursor() as cursor:
            cursor.execute(sql, (novo_status_ve, id_veiculo))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao atualizar status do veículo: {e}")
        return False
    finally:
        conexao.close()


def atualizar_veiculo_banco(id_veiculo: int, modelo: str, placa: str, categoria_requerida: str, capacidade_carga_kg: float):
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        sql = """
            UPDATE Veiculo
            SET modelo = %s, placa = %s, categoria_requerida = %s, capacidade_carga_kg = %s 
            WHERE id_veiculo = %s
        """
        cursor.execute(sql, (modelo, placa, categoria_requerida, capacidade_carga_kg, id_veiculo))
        
        conexao.commit()
        linhas_afetadas = cursor.rowcount
        
        cursor.close()
        conexao.close()
        return linhas_afetadas > 0
    except Exception as erro:
        print(f"Erro ao atualizar veículo: {erro}")
        return False

def deletar_veiculo_banco(id_veiculo: int):
    conexao = obter_conexao()
    try:
        with conexao.cursor() as cursor:
            
            sql = "DELETE FROM veiculo WHERE id_veiculo = %s"
            cursor.execute(sql, (id_veiculo,))
            conexao.commit()
            
            
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao deletar veículo: {e}")
        return False
    finally:
        conexao.close()