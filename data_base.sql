CREATE TABLE operadoras_ativas (
    id SERIAL PRIMARY KEY,              -- ID único da operadora
    registro_ans VARCHAR(20) NOT NULL,  -- Registro único na ANS
    nome VARCHAR(255) NOT NULL,         -- Nome da operadora
    cnpj VARCHAR(20) UNIQUE NOT NULL,   -- CNPJ da operadora
    modalidade VARCHAR(100),            -- Tipo de plano (Ex: Medicina de grupo)
    uf CHAR(2),                         -- Estado onde opera
    municipio VARCHAR(100),             -- Cidade onde opera
    data_registro DATE                   -- Data de registro na ANS
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,              -- ID único do registro
    registro_ans VARCHAR(20) NOT NULL,  -- Registro ANS da operadora
    ano INT NOT NULL,                   -- Ano da demonstração contábil
    trimestre INT NOT NULL,             -- Trimestre do ano
    despesas_eventos_saude NUMERIC(15,2), -- Despesas médicas/hospitalares
    despesas_outros NUMERIC(15,2)       -- Outras despesas
);

ALTER TABLE demonstracoes_contabeis
ADD CONSTRAINT fk_registro_ans
FOREIGN KEY (registro_ans)
REFERENCES operadoras_ativas(registro_ans);