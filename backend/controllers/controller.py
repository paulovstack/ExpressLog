from models.motorista import buscar_motorista_por_id_banco
from models.veiculo import buscar_veiculo_por_id
from models.viagem import inserir_viagem, verificar_viagem_existente
from datetime import datetime, timezone
import dateutil.parser

#ZONA DE CONTROLER

def agendar_viagem(id_motorista, id_veiculo, peso_carga_kg, origem, destino, data_hora_saida=None, data_hora_chegada=None):
    # ETAPA 1: Verificar se o motorista realmente existe.
    motorista = buscar_motorista_por_id_banco(id_motorista)
    if not motorista:
        return{"erro": "Motorista não encontrado"},404

    # ETAPA 2: Verificar se o veículo realmente existe.
    veiculo = buscar_veiculo_por_id(id_veiculo)
    if not veiculo:     
        return {"erro": "Veículo não encontrado"},404

    try:
        if isinstance(data_hora_saida, str):
            data_saida_convertida = dateutil.parser.parse(data_hora_saida)
        else:
            data_saida_convertida = data_hora_saida

        if data_saida_convertida.tzinfo is not None:
            data_saida_convertida = data_saida_convertida.replace(tzinfo=None)
    
    except Exception as e:
        return {"erro": "Formato de data e hora de saída inválido."}, 400

    data_atual = datetime.now()

    # RN01:Compatilibilidade entre a categoria da CNH do motorista e a categoria requerida pelo veículo.
    cat_mot = motorista['categoria_cnh']
    cat_vei = veiculo['categoria_requerida']
    pesos_cnh = {"B": 2, "C": 3, "D": 4, "E": 5}
    if pesos_cnh.get(cat_mot, 0) < pesos_cnh.get(cat_vei, 0):
            return {"erro": f"Compatibilidade inválida! Motorista possui CNH {cat_mot} mas veículo requer {cat_vei}"},400
      
    
    #Validação extra de segurança:
    if peso_carga_kg is None or float(peso_carga_kg) <= 0:
        return {"erro": "O peso da carga deve ser informado e ser maior do que zero!"}, 400
    
    # RN02: Limite de Capacidade de Carga.
    if float (peso_carga_kg) > float(veiculo['capacidade_carga_kg']):
        return {"erro": f"Capacidade de {peso_carga_kg}kg excede a capacidade máxima do veículo ({veiculo['capacidade_carga_kg']}kg)!"}, 400

    # RN03 - BloqueiO por CNH/Status do Motorista.
    if motorista['status_m'] == "inativo" or motorista["pontos_cnh"] >= 20:
        return {"erro": "Agendamento não permitido! Motorista está inativo ou possui 20 ou mais pontos na CNH."}, 400

    # RN04 - Exclusividade de Alocação
    if verificar_viagem_existente(id_veiculo, id_motorista, data_hora_saida):
        return {"erro": "Agendamento não permitido! Motorista ou veículo já estão alocados em outra viagem."}, 400

    if data_saida_convertida < data_atual:
        return {"erro":"Falha ao agendar: Não é permitido realizar agendamentos com data e hora retroativas."}, 400

    # ETAPA 3: Se todas as validações forem bem-sucedidas, insira a viagem no banco de dados.
    sucesso = inserir_viagem(id_motorista, id_veiculo,peso_carga_kg, origem, destino, data_hora_saida, data_hora_chegada)
    if sucesso:
        return {"mensagem": "Viagem agendada com sucesso!"}, 201

    return {"erro": "Falha ao agendar viagem."}, 500
      
