# ExpressLog

Sistema de gerenciamento de frota e viagens desenvolvido com FastAPI, MySQL e HTML/JavaScript.

## Estrutura do projeto

```text
ExpressLog/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── requirements.txt
│   ├── controllers/
│   │   └── controller.py
│   └── models/
│       ├── motorista.py
│       ├── veiculo.py
│       └── viagem.py
├── frontend/
│   └── index.html
├── database/
│   └── express_bd.sql
├── .gitignore
└── README.md
```

## Rodando localmente

### 1. Banco de dados

Importe `database/express_bd.sql` no MySQL.

### 2. Backend

Entre na pasta:

```bash
cd backend
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure no sistema as variáveis:

- `DB_HOST`
- `DB_PORT`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

Depois execute:

```bash
uvicorn app:app --reload
```

A API ficará em `http://127.0.0.1:8000`.

A documentação automática do FastAPI ficará em `http://127.0.0.1:8000/docs`.

## Front-end

Abra `frontend/index.html` no navegador durante o desenvolvimento local.

Para publicar, altere a constante `API_URL` do arquivo para o endereço público da API.

## Deploy do backend

Exemplo de configuração no Render:

- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

Cadastre as variáveis do banco no painel do serviço de hospedagem. Nunca coloque a senha real no GitHub.

## Observação de segurança

O arquivo `.env` está ignorado pelo Git. O `.env.example` contém somente exemplos e pode ser publicado.
