# 🚚 ExpressLog

Sistema de gerenciamento de **motoristas, veículos e viagens**, desenvolvido como projeto de estudo e portfólio durante minha formação em **Análise e Desenvolvimento de Sistemas** e **Back-End**.

O objetivo do ExpressLog é simular situações reais de uma transportadora, aplicando regras de negócio no Back-End e integrando **Front-End, API REST e banco de dados**.

<p align="center">
  <a href="https://paulovstack.github.io/ExpressLog/">🎮 ACESSAR SISTEMA</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="https://github.com/paulovstack/ExpressLog">💻 VER CÓDIGO</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="https://expresslog-pwur.onrender.com/docs">📖 SWAGGER</a>
</p>

---

## 🟢 MISSÃO PRINCIPAL — ExpressLog

Criar um sistema de logística capaz de organizar a operação de uma frota e aplicar regras antes de permitir um agendamento.

Atualmente o sistema permite:

- 👨‍✈️ Cadastrar, editar, consultar e excluir motoristas
- 🚛 Cadastrar, editar, consultar e excluir veículos
- 🗓️ Criar e acompanhar viagens
- ▶️ Iniciar rotas
- ✅ Concluir viagens
- ❌ Cancelar viagens
- 🔎 Pesquisar e filtrar informações no painel
- 📊 Acompanhar informações da operação pelo dashboard

---

## 🆕 ATUALIZAÇÕES RECENTES

O ExpressLog recebeu novas melhorias no Back-End e no Front-End:

### 🚛 Ano do veículo

Agora cada veículo possui também o campo **ano**.

O ano é enviado para a API, validado pelo Back-End e armazenado no banco de dados.

### 👨‍✈️ Motorista identificado pelo nome

No novo agendamento não é mais necessário trabalhar apenas visualmente com o ID.

O sistema apresenta:

`ID — Nome do motorista`

O ID continua sendo utilizado internamente pela API e pelo banco de dados.

### 🚚 Veículo com modelo e ano

Na seleção de veículos para uma viagem, o sistema apresenta:

`ID — Modelo — Ano`

Isso facilita a identificação do veículo antes de criar o agendamento.

### 🗺️ Origem e destino com estados brasileiros

Os campos de **Origem** e **Destino** agora possuem busca pelos estados brasileiros.

Ao começar a digitar, o sistema filtra os estados correspondentes.

Exemplo ao digitar `R`:

- Rio de Janeiro - RJ
- Rio Grande do Norte - RN
- Rio Grande do Sul - RS
- Rondônia - RO
- Roraima - RR

O usuário precisa selecionar um estado válido.

Além da validação no Front-End, a API também verifica os valores recebidos.

Também não é permitido cadastrar uma viagem com **origem e destino iguais**.

### 📊 Dashboard mais fácil de entender

O painel de viagens agora utiliza informações mais amigáveis:

- Nome do motorista
- Modelo do veículo
- Origem e destino
- Peso da carga
- Data de saída e chegada
- Status da viagem

O sistema continua utilizando os IDs internamente para manter os relacionamentos no banco de dados.

### 🔎 Busca aprimorada

A busca do painel também pode localizar viagens através de:

- ID
- Rota
- Nome do motorista
- Modelo do veículo

---

## ⚙️ REGRAS DE NEGÓCIO

O ExpressLog possui regras para evitar operações inválidas.

Entre elas:

- 🚫 Um motorista não pode ser utilizado em viagens conflitantes
- 🚫 Um veículo não pode ser utilizado em viagens conflitantes
- ⚖️ A carga não pode ultrapassar a capacidade do veículo
- 🪪 A categoria da CNH precisa ser compatível com o veículo
- 👨‍✈️ Motoristas inativos ou com pontuação acima da regra definida não podem ser alocados
- 🕒 Não é permitido criar um agendamento no passado
- 🗺️ Origem e destino precisam ser estados válidos
- 🔁 Origem e destino não podem ser iguais
- 🚛 O status do veículo é atualizado conforme a situação da viagem

---

## 🎒 INVENTÁRIO

### Back-End

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

### Banco de Dados

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

### Front-End

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

### Ferramentas

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 🗺️ MAPA DO SISTEMA

```text
Usuário
   │
   ▼
Front-End
GitHub Pages
   │
   │ HTTP / JSON
   ▼
API REST
FastAPI + Python
Render
   │
   ▼
Banco de Dados
MySQL
Aiven
```

A API funciona como intermediária entre a interface e o banco de dados.

As regras de negócio ficam no Back-End, evitando depender apenas das validações feitas no navegador.

---

## 🧠 O QUE ESTOU APRENDENDO COM O PROJETO

O ExpressLog também representa minha evolução como desenvolvedor.

Durante o desenvolvimento estou praticando:

- Programação Orientada a Objetos
- APIs REST
- FastAPI
- Validação de dados
- Pydantic
- SQL
- MySQL
- Relacionamentos e Foreign Keys
- JOIN entre tabelas
- Regras de negócio
- Integração Front-End e Back-End
- Git e GitHub
- Deploy de aplicações
- Debug através de logs e códigos HTTP

Erros encontrados durante o desenvolvimento também fazem parte do projeto, porque me ajudam a entender melhor como cada parte do sistema funciona.

---

## 🌐 PROJETO ONLINE

### 🎮 Sistema

https://paulovstack.github.io/ExpressLog/

### 💻 Repositório

https://github.com/paulovstack/ExpressLog

### 📖 Documentação da API

https://expresslog-pwur.onrender.com/docs

> O Back-End utiliza uma instância gratuita no Render. Por isso, o primeiro acesso pode levar alguns segundos enquanto o serviço é iniciado.

---

## 👨‍💻 Desenvolvedor

**Paulo Victor**

Desenvolvedor Back-End em formação  
Análise e Desenvolvimento de Sistemas

Este projeto faz parte do meu portfólio e continuará recebendo melhorias conforme avanço nos estudos e adquiro novos conhecimentos.
