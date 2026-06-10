SELECT nome, gols_marcados
FROM equipes
ORDER BY gols_marcados DESC
FETCH FIRST 1 ROWS ONLY;


SELECT nome, gols_sofridos
FROM equipes
ORDER BY gols_sofridos ASC
FETCH FIRST 1 ROWS ONLY;


SELECT fase, COUNT(*) AS total_partidas
FROM partidas
GROUP BY fase;


SELECT vencedor AS campeao
FROM partidas
WHERE fase = 'Final';