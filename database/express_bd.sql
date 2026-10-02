create database Explog_db;
use Explog_db;

create table Motorista (id_motorista INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR (100) NOT NULL,
cnh VARCHAR (20) UNIQUE NOT NULL,
categoria_cnh ENUM('A','B','C','D','E','AB','AC','AD','AE') NOT NULL,
pontos_cnh INT DEFAULT 0,
status_m ENUM('ativo','inativo')
);

create table Veiculo (id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
placa VARCHAR(10) NOT NULL UNIQUE,
modelo VARCHAR (50) NOT NULL,
categoria_requerida ENUM('A','B','C','D','E') NOT NULL,
capacidade_carga_kg FLOAT,
status_ve ENUM('disponivel','em_manutencao','em_viagem')
);

create table Viagem (id_viagem INT AUTO_INCREMENT PRIMARY KEY,
id_motorista INT NOT NULL,
id_veiculo INT NOT NULL,
peso_carga_kg DECIMAL(10,2) NOT NULL,
origem VARCHAR(200) NOT NULL,
destino VARCHAR (200) NOT NULL,
data_hora_saida DATETIME,
data_hora_chegada DATETIME,
status_vi ENUM('agendada','em_andamento','concluida', 'cancelada'),
FOREIGN KEY (id_motorista) REFERENCES Motorista(id_motorista),
FOREIGN KEY (id_veiculo) REFERENCES Veiculo(id_veiculo)
);




SELECT * From Motorista;
SELECT * FROM Viagem;

SELECT id_motorista, status_m, pontos_cnh FROM Motorista;
SELECT id_veiculo, capacidade_carga_kg FROM Veiculo;
SELECT * FROM Viagem;

DELETE FROM Veiculo;
