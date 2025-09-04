CREATE DATABASE IF NOT EXISTS bds_fabricantes;
USE bds_fabricantes;

CREATE TABLE IF NOT EXISTS fabricantes (
    id_fabricantes INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    imagem VARCHAR(200) NOT NULL,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS modelos (
    id_modelos INT PRIMARY KEY AUTO_INCREMENT,
    id_fabricantes INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    imagem VARCHAR(200) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_fabricantes) REFERENCES fabricantes(id_fabricantes)
);

CREATE TABLE IF NOT EXISTS arquivos (
    id_arquivos INT PRIMARY KEY AUTO_INCREMENT,
    tipo_arquivo ENUM('IMAGEM', 'DOCUMENTO') NOT NULL,
    descricao TEXT,
    id_modelos INT,
    data_upload DATETIME DEFAULT CURRENT_TIMESTAMP,
    categoria VARCHAR(50),
    link VARCHAR(200),
    FOREIGN KEY (id_modelos) REFERENCES modelos(id_modelos)
);