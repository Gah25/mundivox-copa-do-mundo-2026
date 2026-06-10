CREATE TABLE equipes (
    nome VARCHAR2(50) PRIMARY KEY,
    gols_marcados NUMBER,
    gols_sofridos NUMBER
);
 
CREATE TABLE partidas (
    id NUMBER PRIMARY KEY,
    fase VARCHAR2(20),
    time1 VARCHAR2(50),
    time2 VARCHAR2(50),
    gols1 NUMBER,
    gols2 NUMBER,
    vencedor VARCHAR2(50)
);
 