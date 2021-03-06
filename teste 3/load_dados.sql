# 'C:/Program Files/MySQL/';
# '*.csv /b';

CREATE DATABASE banco_ans;

USE banco_ans;

CREATE TABLE IF NOT EXISTS t_dados(
    D_DATA text null,
    REG_ANS int null,
    CD_CONTA_CONTABIL text null,
    DESCRICAO text null,
    VL_SALDO_FINAL text null,
    id int auto_increment primary key
);

# LOAD dos arquivos 1t 2020
LOAD DATA INFILE 'C:/dados/1T2020.csv'
INTO TABLE t_dados
character set 'latin1'
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(D_DATA,REG_ANS,CD_CONTA_CONTABIL,DESCRICAO,VL_SALDO_FINAL);

# LOAD dos arquivos 2t 2020
LOAD DATA INFILE 'C:/dados/2T2020.csv'
INTO TABLE t_dados
character set 'latin1'
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(D_DATA,REG_ANS,CD_CONTA_CONTABIL,DESCRICAO,VL_SALDO_FINAL);

# LOAD dos arquivos 3t 2020
LOAD DATA INFILE 'C:/dados/3T2020.csv'
INTO TABLE t_dados
character set 'latin1'
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(D_DATA,REG_ANS,CD_CONTA_CONTABIL,DESCRICAO,VL_SALDO_FINAL);

# LOAD dos arquivos 4t 2020
LOAD DATA INFILE 'C:/dados/4T2020.csv'
INTO TABLE t_dados
character set 'latin1'
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(D_DATA,REG_ANS,CD_CONTA_CONTABIL,DESCRICAO,VL_SALDO_FINAL);

# LOAD dos arquivos 1t 2021
LOAD DATA INFILE 'C:/dados/1T2021.csv'
INTO TABLE t_dados
character set 'latin1'
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(D_DATA,REG_ANS,CD_CONTA_CONTABIL,DESCRICAO,VL_SALDO_FINAL);

# LOAD dos arquivos 2t 2021
LOAD DATA INFILE 'C:/dados/2T2021.csv'
INTO TABLE t_dados
character set 'latin1'
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(D_DATA,REG_ANS,CD_CONTA_CONTABIL,DESCRICAO,VL_SALDO_FINAL);

# LOAD dos arquivos 3t 2021
LOAD DATA INFILE 'C:/dados/3T2021.csv'
INTO TABLE t_dados
character set 'latin1'
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(D_DATA,REG_ANS,CD_CONTA_CONTABIL,DESCRICAO,VL_SALDO_FINAL);

