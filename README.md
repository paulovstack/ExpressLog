# 🚚 ExpressLog

### Sistema web para gerenciamento de frota e controle de viagens

O **ExpressLog** é um projeto desenvolvido para facilitar o gerenciamento de **motoristas, veículos e viagens** em uma única aplicação.

O sistema possui uma interface web integrada a uma API desenvolvida com **FastAPI** e utiliza **MySQL** para armazenamento dos dados. O projeto também foi publicado na nuvem, permitindo acessar o sistema diretamente pelo navegador.

> Projeto desenvolvido com foco em praticar desenvolvimento **Full Stack**, integração com banco de dados, criação de API REST e deploy de uma aplicação web.

---

## 🌐 Sistema online

🔗 **Acesse o ExpressLog:**  
https://paulovstack.github.io/ExpressLog/

🔗 **Documentação da API (Swagger):**  
https://expresslog-pwur.onrender.com/docs

> **Observação:** o backend utiliza hospedagem gratuita no Render. Por isso, após algum tempo sem uso, a primeira requisição pode levar alguns segundos enquanto o serviço é iniciado novamente.

---

## 📌 Funcionalidades

### 👨‍✈️ Motoristas
- Cadastro de motoristas
- Consulta dos motoristas cadastrados
- Edição de informações
- Alteração de status
- Exclusão de registros
- Controle de categoria da CNH

### 🚛 Veículos
- Cadastro de veículos
- Consulta da frota
- Edição dos dados
- Controle de capacidade de carga
- Controle de categoria exigida
- Alteração de status
- Exclusão de registros

### 🗺️ Viagens
- Criação de novos agendamentos
- Definição de origem e destino
- Associação entre motorista e veículo
- Registro do peso da carga
- Controle da data e hora de saída
- Início da rota
- Conclusão ou cancelamento da viagem
- Registro da chegada
- Consulta e filtro das viagens por status

### 📊 Painel
- Total de viagens
- Motoristas ativos
- Veículos em viagem
- Busca de viagens
- Filtros por status

---

## 📱 Interface responsiva

A interface foi preparada para funcionar em **computadores e dispositivos móveis**.

No desktop, o sistema utiliza o painel completo com tabelas. Em telas menores, a navegação é adaptada para um menu mobile e as informações são organizadas para facilitar a consulta pelo celular.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
| --- | --- |
| **Python** | Linguagem utilizada no backend |
| **FastAPI** | Desenvolvimento da API REST |
| **MySQL** | Banco de dados relacional |
| **PyMySQL** | Comunicação entre Python e MySQL |
| **HTML** | Estrutura da interface |
| **CSS / Tailwind CSS** | Estilização e responsividade |
| **JavaScript** | Integração do frontend com a API |
| **Git / GitHub** | Versionamento e armazenamento do projeto |
| **GitHub Pages** | Hospedagem do frontend |
| **Render** | Hospedagem da API |
| **Aiven** | Hospedagem do banco MySQL |

---

## ⚙️ Como o projeto funciona

```text
Usuário
   │
   ▼
Frontend
GitHub Pages
   │
   │ Requisições HTTP
   ▼
API REST
FastAPI / Render
   │
   ▼
Banco de Dados
MySQL / Aiven
```

O navegador envia as solicitações para a API. O backend processa as regras do sistema, acessa o banco MySQL e devolve as informações para a interface.

---

## 📁 Estrutura do projeto

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
├── database/
│   └── express_bd.sql
├── index.html
├── .gitignore
└── README.md
```

---

## 💻 Executando localmente

### 1. Banco de dados

Importe o arquivo:

```text
database/express_bd.sql
```

em um servidor MySQL.

### 2. Backend

Entre na pasta do backend:

```bash
cd backend
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente:

```text
DB_HOST
DB_PORT
DB_USER
DB_PASSWORD
DB_NAME
```

Depois execute:

```bash
uvicorn app:app --reload
```

A API estará disponível localmente em:

```text
http://127.0.0.1:8000
```

A documentação automática do FastAPI poderá ser acessada em:

```text
http://127.0.0.1:8000/docs
```

---

## ☁️ Deploy

O ExpressLog utiliza serviços separados para cada parte da aplicação:

```text
Frontend  → GitHub Pages
Backend   → Render
Database  → Aiven MySQL
```

No Render, o backend utiliza:

```text
Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT
```

As credenciais do banco são configuradas através de **variáveis de ambiente**, evitando armazenar senhas diretamente no código.

---

## 🔒 Segurança

Arquivos com credenciais e informações sensíveis não devem ser enviados ao GitHub.

O projeto utiliza variáveis de ambiente para os dados de conexão com o banco. O arquivo `.env` deve permanecer ignorado pelo Git, enquanto um `.env.example` pode ser utilizado apenas como modelo de configuração.

---

## 🎯 Objetivo do projeto

O ExpressLog foi desenvolvido como projeto de estudo para colocar em prática conhecimentos de:

- Desenvolvimento backend com Python
- Criação de APIs REST
- Integração entre frontend e backend
- Banco de dados MySQL
- Operações de cadastro, consulta, edição e exclusão
- Regras de negócio
- Desenvolvimento de interface web
- Responsividade para dispositivos móveis
- Versionamento com Git e GitHub
- Deploy de uma aplicação completa na nuvem

---

## 🚀 Próximas melhorias

O projeto pode continuar evoluindo com recursos como autenticação de usuários, relatórios, histórico detalhado da frota e novas funcionalidades de gerenciamento.

---

## 👨‍💻 Autor

Desenvolvido por **Paulo Victor** como projeto de estudo e evolução em desenvolvimento de software.
