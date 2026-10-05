from fastapi import FastAPI, HTTPException, status, Body
from pydantic import BaseModel, Field, field_validator
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import re

from controllers.controller import agendar_viagem
from models.motorista import inserir_motorista_banco, buscar_motorista_por_id_banco, atualizar_motorista_banco, atualizar_status_motorista_banco, listar_todos_motoristas_banco, deletar_motorista_banco
from models.veiculo import listar_todos_veiculos, inserir_veiculo, atualizar_veiculo_banco, atualizar_status_veiculo,buscar_veiculo_por_id, deletar_veiculo_banco, listar_todos_veiculos, deletar_veiculo_banco
from models.viagem import listar_todas_viagens, atualizar_viagem_concluida, deletar_viagem_banco, buscar_viagem_por_id

app = FastAPI(title="ExpressLog API", description="API de Gerenciamento de Viagens")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


class ViagemSchema(BaseModel):
    id_motorista: int
    id_veiculo: int
    peso_carga_kg: float = Field(..., gt=0, description="Peso da carga em kg")
    origem: str = Field(..., min_length=2, description="Origem da viagem")
    destino: str = Field(..., min_length=2, description="Destino da viagem")
    data_hora_saida: str = Field(None, description="Data de saída YYYY-MM-DD")
    data_hora_chegada: str = Field(None, description="Data de chegada YYYY-MM-DD")

class StatusPatchSchema(BaseModel):
    status_vi: str
    data_hora_chegada: Optional[str] = None

class MotoristaSchema(BaseModel):
    nome: str
    cnh: str
    categoria_cnh: str
    pontos_cnh: int = Field(0, ge=0, description="Pontos da CNH do motorista")
    

    @field_validator("cnh")
    @classmethod
    def validar_cnh(cls, v: str) -> str:
        v = v.strip()
        if not re.match(r"^\d{9}$", v):
            raise ValueError("CNH inválida! Deve conter exatamente 9 dígitos numéricos.")
        return v
    

class VeiculoSchema(BaseModel):
    modelo: str
    placa: str 
    categoria_requerida: Optional[str] = None
    capacidade_carga_kg: Optional[float] = Field(None, gt=0, description="Capacidade de carga em kg")
    ano: int
    @field_validator("placa")
   
    @classmethod
    def validar_placa(cls, v: str) -> str:
        v = v.strip().upper().replace(" ", "")
        if "-" not in v and len(v) == 7:
            v = v[:3] + "-" + v[3:]
        if not re.match(r"^[A-Z]{3}-\d{4}$", v):
            raise ValueError("Placa inválida! Use o padrão tradicional brasileiro: ABC-1234.")
        return v

    @field_validator("ano")
    @classmethod
    def validar_ano(cls, ano: int) -> int:
        
        if ano < 2010 or ano > 2027:
            raise ValueError ("O ano do veículo deve estar entre 2010 e 2027.")
        
        return ano


@app.get("/trips")
def obter_viagens():
    return listar_todas_viagens()

@app.post("/trips", status_code=status.HTTP_201_CREATED)
def criar_viagem(dados: ViagemSchema):
    
    resultado, status_http = agendar_viagem(
        id_motorista=dados.id_motorista,
        id_veiculo=dados.id_veiculo,
        peso_carga_kg=dados.peso_carga_kg,
        origem=dados.origem,
        destino=dados.destino,
        data_hora_saida=dados.data_hora_saida,
        data_hora_chegada=dados.data_hora_chegada
    )
    
    
    if status_http >= 400:
        raise HTTPException(status_code=status_http, detail=resultado.get("erro"))
        
    return resultado

@app.patch("/trips/{id_viagem}")
def modificar_status_viagem(id_viagem: int, dados: StatusPatchSchema):
    status_permitidos = ["agendada", "em_andamento", "concluida", "cancelada"]
    if dados.status_vi not in status_permitidos:
        raise HTTPException(
            status_code=400,
            detail=f"Status inválido! Escolha entre: {status_permitidos}"
        )

    viagem = buscar_viagem_por_id(id_viagem)
    if not viagem:
        raise HTTPException(status_code=404, detail="Viagem não encontrada.")

    sucesso = atualizar_viagem_concluida(
        id_viagem,
        dados.status_vi,
        dados.data_hora_chegada
    )
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao atualizar status da viagem.")

    # Status do veículo é automático:
    # agendada/em andamento -> em viagem
    # concluída/cancelada   -> disponível
    if dados.status_vi in ["agendada", "em_andamento"]:
        status_veiculo = "em_viagem"
    else:
        status_veiculo = "disponivel"

    if not atualizar_status_veiculo(viagem["id_veiculo"], status_veiculo):
        raise HTTPException(status_code=500, detail="Erro ao atualizar status do veículo.")

    return {"mensagem": "Viagem e veículo atualizados com sucesso!"}


@app.delete("/trips/{id_viagem}")
def remover_viagem(id_viagem: int):
    sucesso = deletar_viagem_banco(id_viagem)
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao tentar deletar a viagem do banco de dados.")
    return {"mensagem": f"Viagem ID {id_viagem} deletada com sucesso!"}


@app.post("/drivers/cadastrar", status_code=status.HTTP_201_CREATED)
def rota_inserir_motorista(dados: MotoristaSchema):
    sucesso = inserir_motorista_banco(
        nome=dados.nome,
        cnh=dados.cnh,
        categoria_cnh=dados.categoria_cnh,
        pontos_cnh=dados.pontos_cnh
    )
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao cadastrar motorista no banco.")
    return {"mensagem": "Motorista cadastrado com sucesso!"}


@app.get("/drivers")
def rota_listar_todos_motoristas():
    
    return listar_todos_motoristas_banco()

@app.get("/drivers/buscar/{id_motorista}")
def rota_buscar_motorista_por_id(id_motorista: int):
    
    motorista = buscar_motorista_por_id_banco(id_motorista)
    if not motorista:
        raise HTTPException(status_code=404, detail="Motorista não encontrado.")
    
    return motorista



@app.patch("/drivers/alterar/{id_motorista}")
def rota_atualizar_motorista(id_motorista: int, dados: MotoristaSchema):
    sucesso = atualizar_motorista_banco(
        id_motorista=id_motorista,
        nome=dados.nome,
        cnh=dados.cnh,
        categoria_cnh=dados.categoria_cnh,
        pontos_cnh=dados.pontos_cnh
    )
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao atualizar dados do motorista.")
    return {"mensagem": f"Motorista ID {id_motorista} atualizado com sucesso!"}



@app.patch("/drivers/{id_motorista}/status")
def rota_atualizar_status_motorista(id_motorista: int, novo_status_m: str = Body(embed=True)):
    status_permitidos = ['ativo', 'inativo']
    if novo_status_m not in status_permitidos:
        raise HTTPException(status_code=400, detail=f"Status inválido! Escolha entre: {status_permitidos}")
        
    sucesso = atualizar_status_motorista_banco(id_motorista, novo_status_m)
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao atualizar status do motorista.")
    return {"mensagem": "Status do motorista updated com sucesso!"}


@app.delete("/drivers/deletar/{id_motorista}")
def rota_deletar_motorista(id_motorista: int):
    sucesso = deletar_motorista_banco(id_motorista)
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao tentar deletar o motorista do banco de dados.")
    return {"mensagem": f"Motorista ID {id_motorista} deletado com sucesso!"}



@app.get("/vehicles")
def obter_veiculos():
    return listar_todos_veiculos()

@app.get("/vehicles/buscar/{id_veiculo}")
def obter_veiculo(id_veiculo: int):
    veiculo = buscar_veiculo_por_id(id_veiculo)
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")
    return veiculo

@app.post("/vehicles/cadastrar", status_code=status.HTTP_201_CREATED)
def cadastrar_veiculo(dados: VeiculoSchema):
    sucesso = inserir_veiculo(modelo=dados.modelo, placa=dados.placa, categoria_requerida=dados.categoria_requerida, capacidade_carga_kg=dados.capacidade_carga_kg, ano=dados.ano)
    
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao cadastrar veículo no banco de dados.")
        
    return {"mensagem": "Veículo cadastrado com sucesso!"}

@app.patch("/vehicles/alterar/{id_veiculo}")
def atualizar_veiculo(id_veiculo: int, dados: VeiculoSchema):
    sucesso = atualizar_veiculo_banco(id_veiculo, modelo=dados.modelo, placa=dados.placa, categoria_requerida=dados.categoria_requerida, capacidade_carga_kg=dados.capacidade_carga_kg, ano=dados.ano)
    
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao atualizar veículo ou ID não encontrado.")
        
    return {"mensagem": f"Veículo ID {id_veiculo} atualizado com sucesso."}

@app.patch("/vehicles/{id_veiculo}/status")
def rota_atualizar_status_veiculo(id_veiculo: int, novo_status_ve: str = Body(embed=True)):
    status_permitidos = ['disponivel', 'em_manutencao']
    if novo_status_ve not in status_permitidos:
        raise HTTPException(status_code=400, detail=f"Status inválido! Escolha entre: {status_permitidos}")
        
    sucesso = atualizar_status_veiculo(id_veiculo, novo_status_ve)
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao atualizar status no banco de dados.")
    return {"mensagem": "Status do veículo atualizado com sucesso!"}


@app.delete("/vehicles/deletar/{id_veiculo}")
def remover_veiculo(id_veiculo: int):
    sucesso = deletar_veiculo_banco(id_veiculo)
    if not sucesso:
        raise HTTPException(status_code=500, detail="Erro ao tentar deletar o veículo do banco de dados.")
    return {"mensagem": f"Veículo ID {id_veiculo} deletado com sucesso!"}



