# ExpressLog

Sistema de gerenciamento de transporte desenvolvido para praticar conceitos de **Back-End, APIs REST, banco de dados e integração com Front-End**.

O ExpressLog permite cadastrar motoristas e veículos, criar viagens e acompanhar as operações da frota por meio de um painel.

## Sobre o projeto

O projeto surgiu durante meus estudos de **Análise e Desenvolvimento de Sistemas** e da minha formação em **Back-End**.

A ideia é desenvolver uma aplicação completa e, ao mesmo tempo, colocar em prática assuntos que venho estudando, como:

- Python e Programação Orientada a Objetos
- FastAPI
- APIs REST
- MySQL
- Regras de negócio
- Validação de dados
- Integração entre Front-End, API e banco de dados
- Git e GitHub
- Deploy de aplicações

O projeto continua em desenvolvimento e novas funcionalidades serão adicionadas conforme avanço nos estudos.

## Tecnologias utilizadas

### Back-End
- Python
- FastAPI
- Pydantic
- PyMySQL

### Banco de dados
- MySQL
- Aiven

### Front-End
- HTML
- CSS / Tailwind CSS
- JavaScript

### Deploy
- Render — API
- GitHub Pages — Front-End

## Funcionalidades

### Motoristas
- Cadastro de motoristas
- Consulta dos motoristas cadastrados
- Edição dos dados
- Alteração de status
- Controle de pontos da CNH
- Validação da categoria da CNH
- Exclusão de registros

### Veículos
- Cadastro de veículos
- Consulta da frota
- Edição dos dados
- Controle de capacidade de carga
- Categoria de CNH exigida
- Controle de status do veículo
- Cadastro do ano do veículo
- Exclusão de registros

### Viagens
- Criação de novos agendamentos
- Associação entre motorista e veículo
- Definição de origem e destino
- Controle do peso da carga
- Data e horário de saída
- Início, conclusão e cancelamento de viagens
- Controle automático do status do veículo
- Validação de conflitos de motorista e veículo

## Novas atualizações

Nesta versão, o ExpressLog recebeu melhorias principalmente no cadastro de veículos, no agendamento e no painel de viagens.

### Ano do veículo

Agora cada veículo possui também o campo **ano**. O dado é salvo no banco e utilizado durante a seleção do veículo no agendamento.

### Motorista identificado pelo nome

No novo agendamento, não é mais necessário trabalhar apenas olhando o ID do motorista. A seleção apresenta o **ID junto com o nome**, facilitando a identificação.

Exemplo:

```text
#4 — Marino Junior
```

### Veículo identificado pelo modelo e ano

A seleção do veículo apresenta informações mais fáceis de reconhecer:

```text
#4 — Mercedes Actros — 2024
```

O ID continua sendo utilizado internamente pela API para relacionar os registros.

### Origem e destino por estados brasileiros

Os campos de origem e destino agora trabalham com os estados brasileiros no formato:

```text
Rio de Janeiro - RJ
São Paulo - SP
Minas Gerais - MG
```

Ao começar a digitar, o sistema filtra os estados correspondentes. Por exemplo, ao digitar `R`, são apresentadas opções como Rio de Janeiro, Rio Grande do Norte, Rio Grande do Sul, Rondônia e Roraima.

O usuário precisa selecionar um estado válido e o Back-End também faz a validação dos dados recebidos.

O sistema ainda impede que **origem e destino sejam iguais**.

### Painel de viagens mais fácil de entender

O painel passou a apresentar o **nome do motorista** e o **modelo do veículo**, em vez de mostrar somente os respectivos IDs.

Isso foi feito no Back-End utilizando relacionamento entre as tabelas para retornar informações mais completas sobre cada viagem.

### Busca aprimorada

A pesquisa do painel pode localizar viagens utilizando informações como:

- ID da viagem
- Origem
- Destino
- Nome do motorista
- Modelo do veículo

## Algumas regras de negócio

O ExpressLog possui validações para evitar operações incorretas. Entre elas:

- O motorista precisa possuir categoria de CNH compatível com o veículo.
- Motoristas inativos ou que não atendam às regras de pontuação não podem ser utilizados normalmente em viagens.
- O peso da carga não pode ultrapassar a capacidade cadastrada do veículo.
- Um motorista não pode ser utilizado em viagens conflitantes no mesmo horário.
- Um veículo não pode ser utilizado em viagens conflitantes no mesmo horário.
- Origem e destino precisam ser estados brasileiros válidos.
- Origem e destino não podem ser iguais.
- Veículos envolvidos em uma viagem têm seu status controlado pelo sistema.

## Estrutura geral

De forma simplificada, o sistema funciona assim:

```text
Usuário
   ↓
Front-End
   ↓
API FastAPI
   ↓
Regras de negócio
   ↓
MySQL
```

O Front-End envia as informações para a API. A API valida os dados e as regras de negócio antes de realizar as operações no banco de dados.

## Banco de dados

O projeto trabalha principalmente com três entidades:

```text
Motorista
   │
   └──── Viagem ──── Veículo
```

A tabela de viagens relaciona um motorista e um veículo, permitindo manter o histórico das operações.

## Executando o projeto

Para executar o Back-End localmente, instale as dependências do projeto e configure as variáveis de ambiente utilizadas na conexão com o banco de dados.

Depois, execute a aplicação FastAPI com Uvicorn.

Exemplo:

```bash
uvicorn app:app --reload
```

A documentação interativa da API ficará disponível pelo Swagger da aplicação.

## Objetivo

O ExpressLog é um projeto de estudo e portfólio. Meu objetivo é continuar evoluindo o sistema enquanto desenvolvo meus conhecimentos em **Back-End**, principalmente com Python, APIs REST, banco de dados e regras de negócio.

Além de implementar novas funcionalidades, procuro entender os erros encontrados durante o desenvolvimento e o motivo de cada solução aplicada.

## Autor

**Paulo Victor Carneiro Tavares**  
Desenvolvedor Back-End em formação

GitHub: paulovstack  
LinkedIn: paulovtavares
